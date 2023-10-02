# Runs migration on the specified database
# Given a directory filled with game data json objects
# Clean it and upload it to the database
import os
import json
import argparse
from datetime import datetime
from pathlib import Path
import shutil
from cleaners import game_cleaner
from database_accessor import Database_accessor
from dataRetrieval.getData import download_esports_files, download_games

def addGameToDb(db_accessor: Database_accessor, game: dict, stats: dict, eventTime: datetime) -> None:
    primary_key = game["game_info"]["platformGameId"]
    print(f"Adding game {primary_key} to database")
    db_accessor.addRowToTable(tableName="games", columns=["id", "info", "stats_update", "eventTime"], values=[primary_key, game, stats, eventTime])

def addGamesToDb(db_accessor: Database_accessor, games_directory: str):
    directory_path = Path(games_directory)
    for file_path in directory_path.iterdir():
        if not file_path.is_file():
            continue
        with open(file_path, "r") as json_file:
            game_data = json.load(json_file)
            game, stats, eventTime = game_cleaner.cleanGameData(game_data)
            addGameToDb(db_accessor=db_accessor, game=game, stats=stats, eventTime=eventTime)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_host', help='database host')
    parser.add_argument('--db_port', type=int, help='database port')
    parser.add_argument('--db_user', help='database user')
    parser.add_argument('--db_password', help='database user password')
    parser.add_argument('--db_name', help='database name')
    parser.add_argument('-m', '--migrate', choices=['up', 'down', ''], default='', help='Migrate up to set up the database, migrate down to reset database')
    parser.add_argument('--game_data_dir', help='If specified, will clean all game files located in directory holding raw game data (json files)')
    parser.add_argument('--download_and_clean', help='Will automatically download and clean all data. Deletes data after processing to save memory.', action="store_true", default=False)


    args = parser.parse_args()
    
    db_accessor = Database_accessor(db_name = args.db_name, 
                                    db_host = args.db_host,
                                    db_port = args.db_port,
                                    db_user = args.db_user,
                                    db_password = args.db_password)


    # Migrations
    match args.migrate:
        case 'up':
            db_accessor.migrateUp()
        case 'down':
            db_accessor.resetDatabase()
            
    # Manually specified games data directory
    if args.game_data_dir:
        addGamesToDb(db_accessor=db_accessor, games_directory=os.path.abspath(args.game_data_dir))
    
    # Automatically download and clean game data
    if args.download_and_clean:
        download_directory = f"{Path(__file__).parent.resolve()}/dataRetrieval/temp"
        download_esports_files(destinationDirectory=download_directory)
        with open(f"{download_directory}/esports-data/tournaments.json", "r") as json_file:
            tournaments_data = json.load(json_file)
            # Process games one tournament at a time, then remove them to save space
            for tournament in tournaments_data:
                download_games(year=2023, tournament_id=tournament["id"], destination_directory=download_directory)
                addGamesToDb(db_accessor=db_accessor, games_directory=os.path.abspath(f"{download_directory}/games"))
                print(f"Clearing out games directory: {download_directory}/games")
                shutil.rmtree(f"{download_directory}/games")
