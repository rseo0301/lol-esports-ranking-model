# Main utility script for all "data cleaning" related tasks
# This includes migration, cleaning, and uploading to database
# This script is meant to be run from the command line
# See arguments for usage, or run 'python main.py --help'
from logging import warning
import os
import json
import argparse
import time
from datetime import datetime
from pathlib import Path
import shutil
from util import getWinningTeam
from util import getTeamIdsFromGameInfo
from cumulativeStats.cumulative_data_builder import Cumulative_Stats_Builder
from cleaners import game_cleaner, esports_data_cleaner
from database_accessor import Database_Accessor
from dataRetrieval.getData import download_esports_files, download_games

_db_accessor: Database_Accessor = None

# Assuming that dbAccessor will be initialized in "main" (after command line args are parsed)
def getDbAccessor() -> Database_Accessor:
    global _db_accessor
    return _db_accessor


def addGamesToDb(games_directory: str):
    def addGameToDb(game: dict, stats: dict, eventTime: datetime) -> None:
        db_accessor: Database_Accessor = getDbAccessor()
        primary_key = game["game_info"]["platformGameId"]
        print(f"Adding game {primary_key} to database")
        db_accessor.addRowToTable(tableName="games", columns=["id", "info", "stats_update", "eventTime"], values=[primary_key, game, stats, eventTime])

    directory_path = Path(games_directory)
    for file_path in directory_path.iterdir():
        if not file_path.is_file():
            continue
        with open(file_path, "r") as json_file:
            game_data = json.load(json_file)
            game, stats, eventTime = game_cleaner.cleanGameData(game_data)
            addGameToDb(game=game, stats=stats, eventTime=eventTime)


def addEsportsDataToDb(esports_data_directory: str):
    def addLeaguesToDb(data: dict):
        db_accessor: Database_Accessor = getDbAccessor()
        primary_key = data["id"]
        print(f"Adding League {primary_key} to database")
        db_accessor.addRowToTable(tableName="leagues", columns=["id", "league"], values=[primary_key, data])

    def addMappingToDb(data: dict):
        db_accessor: Database_Accessor = getDbAccessor()
        primary_key = data["platformGameId"]
        print(f"Adding mapping {primary_key} to database")
        db_accessor.addRowToTable(tableName="mapping_data", columns=["id", "mapping"], values=[primary_key, data])

    def addPlayerToDb(data: dict):
        db_accessor: Database_Accessor = getDbAccessor()
        primary_key = data["player_id"]
        print(f"Adding player {primary_key} to database")
        db_accessor.addRowToTable(tableName="players", columns=["id", "player"], values=[primary_key, data])

    def addTeamToDb(data: dict):
        db_accessor: Database_Accessor = getDbAccessor()
        primary_key = data["team_id"]
        print(f"Adding team {primary_key} to database")
        db_accessor.addRowToTable(tableName="teams", columns=["id", "team"], values=[primary_key, data])

    def addTournamentToDb(data: dict):
        db_accessor: Database_Accessor = getDbAccessor()
        primary_key = data["id"]
        print(f"Adding tournament {primary_key} to database")
        db_accessor.addRowToTable(tableName="tournaments", columns=["id", "tournament"], values=[primary_key, data])



    directory_path = Path(esports_data_directory)
    for file_path in directory_path.iterdir():
        if not file_path.is_file():
            continue
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            match (file_path.name):
                case 'leagues.json':
                    cleaned_data = esports_data_cleaner.cleanLeaguesData(data)
                    for entry in cleaned_data:
                        addLeaguesToDb(data=entry)
                case 'mapping_data.json':
                    cleaned_data = esports_data_cleaner.cleanMappingData(data)
                    for entry in cleaned_data:
                        addMappingToDb(data=entry)
                case 'players.json':
                    cleaned_data = esports_data_cleaner.cleanPlayersData(data)
                    for entry in cleaned_data:
                        addPlayerToDb(data=entry)
                case 'teams.json':
                    cleaned_data = esports_data_cleaner.cleanTeamsData(data)
                    for entry in cleaned_data:
                        addTeamToDb(data=entry)
                case 'tournaments.json':
                    cleaned_data = esports_data_cleaner.cleanTournamentsData(data)
                    for entry in cleaned_data:
                        addTournamentToDb(data=entry)



def buildTeamRegionMapping() -> None:
    db_accessor = getDbAccessor()
    # First, build up mapping from tournament -> region
    tournament_to_region: dict = {}
    n_leagues: int = 0
    print("Starting to build region mapping table")
    while(True):
        leagues_data = db_accessor.getDataFromTable(tableName="leagues", columns=["league"], limit=10, offset=n_leagues)
        if len(leagues_data) == 0:
            break
        n_leagues += len(leagues_data)
        for league_data in leagues_data:
            league = json.loads(league_data[0])
            region = league['region']
            for tournament in league['tournaments']:
                tournament_to_region[tournament['id']] = region
        
        # Second, build up mapping from team -> region
    team_to_region: dict = {}
    n_tournaments: int = 0
    while(True):
        tournaments_data = db_accessor.getDataFromTable(tableName="tournaments", columns=["tournament"], limit=10, offset=n_tournaments)
        if len(tournaments_data) == 0:
            break
        n_tournaments += len(tournaments_data)
        for tournament_data in tournaments_data:
            if tournament['id'] not in tournament_to_region:
                warning(f"Can not find region/league associated with tournament:\n   Tournament ID: {tournament['id']}\n   Tournament name: {tournament['name']}")
                continue
            region = tournament_to_region[tournament['id']]
            tournament = json.loads(tournament_data[0])
            for stage in tournament['stages']:
                for section in stage['sections']:
                    for matches in section['matches']:
                        for team in matches['teams']:
                            team_to_region[team['id']] = region
        
        # Lastly, write {teamID: region} to database
    for id, region in team_to_region.items():
        db_accessor.addRowToTable(tableName="team_region_mapping", columns=["id", "region"], values=[id, region])
    print("Finished building region mapping table")


def buildCumulativeStats():
    db_accessor = getDbAccessor()
    gameCount: int = 0
    cumulative_stats_builder: Cumulative_Stats_Builder = Cumulative_Stats_Builder(db_accessor=db_accessor)
        # Keep track of the current cumulative stats of each team
    teams_cumulative_stats = {}
    while(True):
        games = db_accessor.getDataFromTable(tableName="games", columns=["id", "info", "stats_update"], order_clause="eventTime ASC", limit=10, offset=gameCount)
        if len(games) == 0:
            break
        for game_id, game_info, stats_update in games:
            game_info, stats_update = json.loads(game_info), json.loads(stats_update)
            team1_id, team2_id = getTeamIdsFromGameInfo(db_accessor=db_accessor, game_info=game_info)

                # First, tell the database about each team's cumulative stats going into the game
            cumulative_stats = {}
            if team1_id in teams_cumulative_stats:
                cumulative_stats['team_1'] = teams_cumulative_stats[team1_id]
            if team2_id in teams_cumulative_stats:
                cumulative_stats['team_2'] = teams_cumulative_stats[team2_id]
            cumulative_stats['meta'] = {
                    'winning_team': getWinningTeam(game_info=game_info)
                }
            print(f"Writing cumulative stats for game {game_info['game_info']['platformGameId']}")
            db_accessor.addRowToTable(tableName='cumulative_data', columns=['id', 'scale_by_90'], values=[game_id, cumulative_stats], replaceOnDuplicate=True)

                # Then, update each team's cumulative stats after playing this game
            team1_cumulative_stats, team2_cumulative_stats = cumulative_stats_builder.addGamePlayed(game_info=game_info, stats_info=stats_update)
            teams_cumulative_stats[team1_id], teams_cumulative_stats[team2_id] = team1_cumulative_stats, team2_cumulative_stats
        gameCount += len(games)
        print(f"Written cumulative stats for {gameCount} games.")
    print(f"{gameCount} games written to cumulative stats table")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_host', help='database host')
    parser.add_argument('--db_port', type=int, help='database port')
    parser.add_argument('--db_user', help='database user')
    parser.add_argument('--db_password', help='database user password')
    parser.add_argument('--db_name', help='database name')
    parser.add_argument('-m', '--migrate', choices=['up', 'down', ''], default='', help='Migrate up to set up the database, migrate down to reset database')
    parser.add_argument('--game_data_dir', help='If specified, will clean all game files located in directory holding raw game data (json files)')
    parser.add_argument('--esports_data_dir', help='If specified, will clean all esports data files located in directory holding raw esports data (json files)')
    parser.add_argument('--download_and_clean', help='Will automatically download and clean all data. Deletes data after processing to save memory.', action="store_true", default=False)
    parser.add_argument('--download_and_clean_esports', help='Will automatically download and clean esports data (not game data).', action="store_true", default=False)
    parser.add_argument('--build_region_mapping', help='Build the region mapping table, using the data available in the database.', action="store_true", default=False)
    parser.add_argument('--build_cumulative_stats', help='Build the cumulative stats using the data available in the database.', action="store_true", default=False)
    args = parser.parse_args()
    
    _db_accessor = Database_Accessor(db_name = args.db_name, 
                                    db_host = args.db_host,
                                    db_port = args.db_port,
                                    db_user = args.db_user,
                                    db_password = args.db_password)
    # Testing db_accessor
    # _db_accessor = Database_Accessor(db_name = 'games', db_host = 'riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com', db_user = 'data_cleaner')
    db_accessor = getDbAccessor()
    download_directory = f"{Path(__file__).parent.resolve()}/dataRetrieval/temp"
    timings = {}


    # Migrations
    if args.migrate:
        start_time = time.time()
        match args.migrate:
            case 'up':
                db_accessor.migrateUp()
            case 'down':
                db_accessor.resetDatabase()
        timings['Migration'] = time.time() - start_time
            
    # Clean and upload games data in specified games data directory
    if args.game_data_dir:
        start_time = time.time()
        addGamesToDb(games_directory=args.game_data_dir)
        timings['Clean game data directory'] = time.time() - start_time
    
    # Clean and upload esports data in specified esports data directory
    if args.esports_data_dir:
        start_time = time.time()
        addEsportsDataToDb(esports_data_directory=args.esports_data_dir)
        timings['Clean esports data directory'] = time.time() - start_time
    
    # Automatically download and clean game data
    if args.download_and_clean:
        start_time = time.time()
        download_esports_files(destinationDirectory=download_directory)
        with open(f"{download_directory}/esports-data/tournaments.json", "r") as json_file:
            leagues_data = json.load(json_file)
            # Process games one tournament at a time, then remove them to save space
            for tournament in leagues_data:
                download_games(year=2023, tournament_id=tournament["id"], destination_directory=download_directory)
                addGamesToDb(games_directory=os.path.abspath(f"{download_directory}/games"))
                print(f"Clearing out games directory: {download_directory}/games")
                shutil.rmtree(f"{download_directory}/games")
        timings['Download and clean game data'] = time.time() - start_time

    # Automatically download and clean esports data
    if args.download_and_clean_esports or args.download_and_clean:
        start_time = time.time()
        download_esports_files(destinationDirectory=download_directory)
        addEsportsDataToDb(esports_data_directory=f"{download_directory}/esports-data")
        timings['Download and clean esports data'] = time.time() - start_time
    
    # Build region mapping table (map each team to a region)
    if args.build_region_mapping:
        start_time = time.time()
        buildTeamRegionMapping()
        timings['Build team-to-region mapping table'] = time.time() - start_time

    # Build cumulative stats
    if args.build_cumulative_stats:
        start_time = time.time()
        buildCumulativeStats()
        timings['Build cumulative stats table'] = time.time() - start_time
    

    print("Timings for tasks completed:")
    for task_name, timing in timings.items():
        n_spaces = max(40 - len(task_name), 0)
        print(f"{task_name}: " + (' '*n_spaces) + f"{timing:.2f} seconds")
