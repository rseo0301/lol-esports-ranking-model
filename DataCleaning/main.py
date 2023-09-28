# Runs migration on the specified database
# Given a directory filled with game data json objects
# Clean it and upload it to the database
import argparse
from database_accessor import Database_accessor

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--migrate', choices=['up', 'down'], default='up', help='Migrate up to set up the database, migrate down to reset database')
    parser.add_argument('--db_host', help='database host')
    parser.add_argument('--db_port', type=int, help='database port')
    parser.add_argument('--db_user', help='database user')
    parser.add_argument('--db_password', help='database user password')
    parser.add_argument('--db_name', help='database name')
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