# Main utility script for all "data cleaning" related tasks
# This includes migration, cleaning, and uploading to database
# This script is meant to be run from the command line
# See arguments for usage, or run 'python main.py --help'
import os
import sys
from typing import List
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, ".."))
from distutils.log import error
from logging import warning
import json
import argparse
import time
from datetime import datetime
from pathlib import Path
import shutil
from cleaners.esports_data_cleaner import Esports_Cleaner
from dao.util import getWinningTeam, getTeamIdsFromGameInfo
from cumulativeStats.cumulative_data_builder import Cumulative_Stats_Builder
from cleaners.game_cleaner import Game_Cleaner
from cleaners.esports_data_cleaner import Esports_Cleaner
from dao.database_accessor import Database_Accessor
from dataRetrieval.getData import download_esports_files, download_games

_db_accessor: Database_Accessor = None
LEAGUES_SHORTLIST = [
    "LPL",
    "LEC",
    "LCK",
    "LCS",
    "PCS",
    "VCS",
    "CBLOL",
    "LJL",
    "LLA",
    "MSI",
    "Worlds",
]

# Assuming that dbAccessor will be initialized in "main" (after command line args are parsed)
def getDbAccessor() -> Database_Accessor:
    global _db_accessor
    return _db_accessor


def addGamesToDb(games_directory: str):
    def addGameToDb(game: dict, stats: dict, eventTime: datetime) -> None:
        db_accessor: Database_Accessor = getDbAccessor()
        primary_key = game["game_info"]["platformGameId"]
        gameName = game["game_info"]["gameName"]
        mapping_data = db_accessor.getDataFromTable(tableName="mapping_data", columns=["mapping"], where_clause=f"id='{primary_key}'")
        esportsGameId = json.loads(mapping_data[0][0])['esportsGameId']
        print(f"Adding game {primary_key} to database")
        db_accessor.addRowToTable(tableName="games", columns=["id", "gameName", "esportsGameId", "info", "stats_update", "eventTime"], values=[primary_key, gameName, esportsGameId, game, stats, eventTime])

    directory_path = Path(games_directory)
    game_cleaner: Game_Cleaner = Game_Cleaner()
    for file_path in directory_path.iterdir():
        if not file_path.is_file():
            continue
        with open(file_path, "r") as json_file:
            game_data = json.load(json_file)
            game, stats, eventTime = game_cleaner.cleanGameData(game_data)
            addGameToDb(game=game, stats=stats, eventTime=eventTime)


def addEsportsDataToDb(esports_data_directory: str, league_shortlist_only: bool = False):
    db_accessor: Database_Accessor = getDbAccessor()
    directory_path = Path(esports_data_directory)
    esports_data_cleaner: Esports_Cleaner = Esports_Cleaner()
    shortlist_tournaments: List[str] = []
    tournament_league_mapping: dict = {}
    tournament_region_mapping: dict = {}
    team_to_region: dict = {}
    team_to_league: dict = {}

    def inLeagueShortlist(league: str) -> bool:
        for x in LEAGUES_SHORTLIST:
            if league.capitalize().strip().replace('-','').replace('_','') == x.capitalize().strip().replace('-','').replace('_',''):
                return True
        return False
    
    def addLeaguesToDb(league_data: dict):
        nonlocal shortlist_tournaments
        primary_key = league_data["id"]
        if league_shortlist_only and not inLeagueShortlist(league_data['name']):
            return
        print(f"Adding League {league_data['name']} ({primary_key}) to database")
        shortlist_tournaments += [obj['id'] for obj in league_data['tournaments']]
        for tournament in league_data['tournaments']:
            tournament_league_mapping[tournament['id']] = league_data['name']
            tournament_region_mapping[tournament['id']] = league_data['region']
        db_accessor.addRowToTable(tableName="leagues", columns=["id", "league"], values=[primary_key, league_data])

    def addMappingToDb(data: dict):
        primary_key = data["platformGameId"]
        print(f"Adding mapping {primary_key} to database")
        db_accessor.addRowToTable(tableName="mapping_data", columns=["id", "mapping"], values=[primary_key, data])

    def addPlayerToDb(data: dict):
        primary_key = data["player_id"]
        print(f"Adding player {data['handle']} ({primary_key}) to database")
        db_accessor.addRowToTable(tableName="players", columns=["id", "player"], values=[primary_key, data])

    # Expects that team_to_region and team_to_league are already built
    def addTeamToDb(data: dict):
        team_id = data["team_id"]
        if league_shortlist_only and not (team_id in team_to_league):
            return
        print(f"Adding team {data['name']} ({team_id}) to database")
        league = team_to_league.get(team_id)
        region = team_to_region.get(team_id)
        db_accessor.addRowToTable(tableName="teams", columns=["id", "team", "league", "region"], values=[team_id, data, league, region])

    def addTournamentToDb(data: dict):
        primary_key = data["id"]
        if league_shortlist_only and not (primary_key in shortlist_tournaments):
            return
        print(f"Adding tournament {data['name']} ({primary_key}) to database")
        db_accessor.addRowToTable(tableName="tournaments", columns=["id", "tournament"], values=[primary_key, data])

    # Expects tournament_league_mapping and tournament_region_mapping to already be built, and tournaments to be uploaded to db
    def buildRegionLeagueMapping() -> None:
        n_tournaments: int = 0
        while(True):
            tournaments_data = db_accessor.getDataFromTable(tableName="tournaments", columns=["tournament"], limit=10, offset=n_tournaments)
            if len(tournaments_data) == 0:
                break
            n_tournaments += len(tournaments_data)
            for tournament_data in tournaments_data:
                tournament = json.loads(tournament_data[0])
                if tournament['id'] not in tournament_region_mapping:
                    warning(f"Can not find region/league associated with tournament:\n   Tournament ID: {tournament['id']}\n   Tournament name: {tournament['name']}")
                    continue
                region = tournament_region_mapping[tournament['id']]
                league = tournament_league_mapping[tournament['id']]
                if region.lower() == "international":
                    continue
                for stage in tournament['stages']:
                    for section in stage['sections']:
                        for matches in section['matches']:
                            for team in matches['teams']:
                                team_to_region[team['id']] = region
                                team_to_league[team['id']] = league
            
        # Lastly, write to database
        for id, region in team_to_region.items():
            if not id:
                continue
            db_accessor.addRowToTable(tableName="team_region_mapping", columns=["id", "region"], values=[id, region])

    # Given a file name, reads it, calls the appropriate cleaner, and calls the appropriate handler to add it to the database
    def processFile(file_name: str):
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            match (file_name):
                case 'leagues.json':
                    cleaned_data = esports_data_cleaner.cleanLeaguesData(data)
                    for entry in cleaned_data:
                        addLeaguesToDb(league_data=entry)
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


    processFile("leagues.json")
    processFile("mapping_data.json")
    processFile("players.json")
    processFile("tournaments.json")
    buildRegionLeagueMapping()
    processFile("teams.json")







def buildCumulativeStats():
    db_accessor = getDbAccessor()
    gameCount: int = 0
    skippedGamesCount: int = 0
    cumulative_stats_builder: Cumulative_Stats_Builder = Cumulative_Stats_Builder(db_accessor=db_accessor)
    # Keep track of the current cumulative stats of each team
    teams_cumulative_stats = {}
    # Write to cumulative_data table
    while(True):
        games = db_accessor.getDataFromTable(tableName="games", columns=["id", "info", "stats_update"], order_clause="eventTime ASC", limit=10, offset=gameCount)
        if len(games) == 0:
            break
        for game_id, game_info, stats_update in games:
            try:
                game_info, stats_update = json.loads(game_info), json.loads(stats_update)
                team1_id, team2_id = getTeamIdsFromGameInfo(db_accessor=db_accessor, game_info=game_info)

                # First, tell the database about each team's cumulative stats going into the game
                cumulative_stats = {}
                if team1_id in teams_cumulative_stats:
                    cumulative_stats['team_1'] = teams_cumulative_stats[team1_id]
                if team2_id in teams_cumulative_stats:
                    cumulative_stats['team_2'] = teams_cumulative_stats[team2_id]
                cumulative_stats['meta'] = {
                        'winning_team': getWinningTeam(game_info=game_info),
                        'team1_id': team1_id,
                        'team2_id': team2_id
                    }
                print(f"Writing cumulative stats for game {game_info['game_info']['platformGameId']}")
                db_accessor.addRowToTable(tableName='cumulative_data', columns=['id', 'scale_by_90'], values=[game_id, cumulative_stats], replaceOnDuplicate=True)

                # Then, update each team's cumulative stats after playing this game
                team1_cumulative_stats, team2_cumulative_stats = cumulative_stats_builder.addGamePlayed(game_info=game_info, stats_info=stats_update)
                teams_cumulative_stats[team1_id], teams_cumulative_stats[team2_id] = team1_cumulative_stats, team2_cumulative_stats
            except Exception as e:
                skippedGamesCount += 1
                warning(f"Error building cumulative stats for game {game_info['game_info']['platformGameId']} -- skipping game")
        gameCount += len(games)
        print(f"Processed cumulative stats for {gameCount} games.\n   {skippedGamesCount} games skipped so far.")
    # Write cumulative stats of each team's last game, to teams table
    for team_id, stats in teams_cumulative_stats.items():
        db_accessor.addRowToTable(tableName="teams", columns=["id", "latest_cumulative_stats"], values=[team_id, stats], replaceOnDuplicate=True)
    print(f"Processed cumulative stats for {gameCount} games.\n   Cumulative stats for {gameCount - skippedGamesCount} games successfully written.\n   {skippedGamesCount} games skipped.")

# Expects that tournament data is already uploaded to db
def downloadAndCleanGames(download_directory: str) -> None:
    download_esports_files(destinationDirectory=download_directory)
    db_accessor: Database_Accessor = getDbAccessor()
    n_tournaments = 0
    while True:
        tournaments_data = db_accessor.getDataFromTable(tableName="tournaments", columns=["tournament"], limit=10, offset=n_tournaments)
        if len(tournaments_data) == 0:
            break
        n_tournaments += len(tournaments_data)
        # Process games one tournament at a time, then remove them to save space
        for tournament_data in tournaments_data:
            tournament = json.loads(tournament_data[0])
            for year in range(2019, 2024):
                n_retries = 0
                max_retries = 3
                while(n_retries < max_retries):
                    if os.path.exists(f"{download_directory}/games"):
                        print(f"Clearing out games directory: {download_directory}/games")
                        shutil.rmtree(f"{download_directory}/games")
                    try:
                        download_games(year=year, tournament_id=tournament["id"], destination_directory=download_directory)
                        addGamesToDb(games_directory=os.path.abspath(f"{download_directory}/games"))
                        break
                    except Exception as e:
                        n_retries += 1
                        warning(f"Encountered error while processing tournament {tournament['id']}, retrying: {e}")
                        if n_retries >= max_retries:
                            error(f"Max retries exceeded. Skipping tournament {tournament['id']}")


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
    parser.add_argument('--download_and_clean_games', help='Will automatically download and clean game data (not esports data. Assumed esports data is already set up).', action="store_true", default=False)
    parser.add_argument('--build_cumulative_stats', help='Build the cumulative stats using the data available in the database.', action="store_true", default=False)
    parser.add_argument('--league_shortlist_only', help='Only process leagues in the league shortlist (specified by hackathon) when processing esports data', action="store_true", default=False)
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

    try:
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
            addEsportsDataToDb(esports_data_directory=args.esports_data_dir, league_shortlist_only=args.league_shortlist_only)
            timings['Clean esports data directory'] = time.time() - start_time
        
        # Automatically download and clean esports data
        if args.download_and_clean_esports or args.download_and_clean:
            start_time = time.time()
            download_esports_files(destinationDirectory=download_directory)
            addEsportsDataToDb(esports_data_directory=f"{download_directory}/esports-data", league_shortlist_only=args.league_shortlist_only)
            timings['Download and clean esports data'] = time.time() - start_time
        

        # Automatically download and clean game data
        if args.download_and_clean or args.download_and_clean_games:
            start_time = time.time()
            downloadAndCleanGames(download_directory=download_directory)

            timings['Download and clean game data'] = time.time() - start_time


        # Build cumulative stats
        if args.build_cumulative_stats:
            start_time = time.time()
            buildCumulativeStats()
            timings['Build cumulative stats table'] = time.time() - start_time
    except Exception as e:
        error(e)
    finally:
        print("Timings for tasks completed:")
        for task_name, timing in timings.items():
            n_spaces = max(40 - len(task_name), 0)
            print(f"{task_name}: " + (' '*n_spaces) + f"{timing:.2f} seconds")
