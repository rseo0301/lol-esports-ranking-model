# Main utility script for all "data cleaning" related tasks
# This includes migration, cleaning, and uploading to database
# This script is meant to be run from the command line
# See arguments for usage, or run 'python main.py --help'
import os
import json
import argparse
from datetime import datetime
from pathlib import Path
import shutil
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
    parser.add_argument('--build_cumulative_stats', help='Build the cumulative stats using the data available in the database.', action="store_true", default=False)
    args = parser.parse_args()
    
    _db_accessor = Database_Accessor(db_name = args.db_name, 
                                    db_host = args.db_host,
                                    db_port = args.db_port,
                                    db_user = args.db_user,
                                    db_password = args.db_password)
    db_accessor = getDbAccessor()
    download_directory = f"{Path(__file__).parent.resolve()}/dataRetrieval/temp"


    # Migrations
    match args.migrate:
        case 'up':
            db_accessor.migrateUp()
        case 'down':
            db_accessor.resetDatabase()
            
    # Clean and upload games data in specified games data directory
    if args.game_data_dir:
        addGamesToDb(games_directory=args.game_data_dir)
    
    # Clean and upload esports data in specified esports data directory
    if args.esports_data_dir:
        addEsportsDataToDb(esports_data_directory=args.esports_data_dir)
    
    # Automatically download and clean game data
    if args.download_and_clean:
        download_esports_files(destinationDirectory=download_directory)
        with open(f"{download_directory}/esports-data/tournaments.json", "r") as json_file:
            tournaments_data = json.load(json_file)
            # Process games one tournament at a time, then remove them to save space
            for tournament in tournaments_data:
                download_games(year=2023, tournament_id=tournament["id"], destination_directory=download_directory)
                addGamesToDb(games_directory=os.path.abspath(f"{download_directory}/games"))
                print(f"Clearing out games directory: {download_directory}/games")
                shutil.rmtree(f"{download_directory}/games")
    
    # Automatically download and clean esports data
    if args.download_and_clean_esports or args.download_and_clean:
        download_esports_files(destinationDirectory=download_directory)
        addEsportsDataToDb(esports_data_directory=f"{download_directory}/esports-data")
    
    # Build cumulative stats
    if args.build_cumulative_stats:
        gameCount: int = 0
        db_accessor.getDataFromTable(tableName="games", columns=["id"], order_clause="eventTime ASC", limit=10, offset=gameCount)
    
    # TESTING this should be gated by args
    """
    db_accessor = Database_Accessor(db_name = "games", 
                                    db_host = "riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
                                    db_user = "data_cleaner")
    gameCount: int = 0
    cumulative_stats_builder: Cumulative_Stats_Builder = Cumulative_Stats_Builder(db_accessor=db_accessor)
    # Keep track of the current cumulative stats of each team
    teams_cumulative_stats = {}
    while(True):
        games = db_accessor.getDataFromTable(tableName="games", columns=["id", "info", "stats_update"], order_clause="eventTime ASC", limit=10, offset=gameCount)
        if len(games) == 0:
            break
        for id, game_info, stats_update in games:
            # Do some processing on the games
            # CUMULATIVE STATS BUILDER
            print(id)
        gameCount += len(games)
    print(games)
    """
