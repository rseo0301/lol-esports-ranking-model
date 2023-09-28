# Runs migration on the specified database
# Given a directory filled with game data json objects
# Clean it and upload it to the database
import os
import json
import argparse
from cleaners import cleanGameData
from database_accessor import Database_accessor

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
    match args.migrate:
        case 'up':
            db_accessor.migrateUp()
        case 'down':
            db_accessor.resetDatabase()
    
    # WIP
    if args.clean_game_data and args.game_data_dir:
        filePath = os.path.abspath(args.game_data_dir)
        with open(filePath, "r") as json_file:
            game_data = json.load(json_file)
            game, stats = cleanGameData(game_data)
            print(game)