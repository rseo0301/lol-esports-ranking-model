# Runs migration on the specified database
# Given a directory filled with game data json objects
# Clean it and upload it to the database
import os
import json
import argparse
from datetime import datetime
from pathlib import Path
from cleaners import game_cleaner
from database_accessor import Database_accessor

def addGameToDb(db_accessor: Database_accessor, game: dict, stats: dict, eventTime: datetime) -> None:
    primary_key = game["game_info"]["platformGameId"]
    db_accessor.addRowToTable(tableName="games", columns=["id", "info", "stats_update", "eventTime"], values=[primary_key, game, stats, eventTime])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--migrate', choices=['up', 'down', ''], default='', help='Migrate up to set up the database, migrate down to reset database')
    parser.add_argument('--db_host', help='database host')
    parser.add_argument('--db_port', type=int, help='database port')
    parser.add_argument('--db_user', help='database user')
    parser.add_argument('--db_password', help='database user password')
    parser.add_argument('--db_name', help='database name')
    parser.add_argument('--game_data_dir', help='directory holding raw game data json files')
    parser.add_argument('--clean_game_data', help='will clean and upload all the game data stored in specified game_data_dir', action="store_true", default=False)
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
            
    # Cleaning data and uploading
    if args.clean_game_data and args.game_data_dir:
        directory_path = Path(os.path.abspath(args.game_data_dir))
        for file_path in directory_path.iterdir():
            if not file_path.is_file():
                continue
            with open(file_path, "r") as json_file:
                game_data = json.load(json_file)
                game, stats, eventTime = game_cleaner.cleanGameData(game_data)
                print(game)
                addGameToDb(db_accessor=db_accessor, game=game, stats=stats, eventTime=eventTime)
                