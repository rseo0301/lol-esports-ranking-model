# Contains all functionality relating to database access
# Expects that the database exists, and "__db_user" has permissions on that database
# Migrating up sets up database, and is idempotent (eg. does nothing if database is already set up)
# Migrate down to reset database

import string
from mysql.connector import MySQLConnection, connect
import argparse
class Database_accessor:
    def __init__(self,
                db_name: string, 
                db_host: string,
                db_port: int,
                db_user: string,
                db_password: string):
        self.db_name = db_name if db_name else "games"
        self.db_host = db_host if db_host else "localhost"
        self.db_port = db_port if db_port else 3306
        self.db_user = db_user if db_user else "data_cleaner"
        self.db_password = db_password if db_password else ""
        self.db = connect(database=self.db_name,
                            host=self.db_host,
                            user=self.db_user,
                            port=self.db_port,
                            password=self.db_password
                            )
        
    def migrateUp(self) -> None:
        db = self.db
        with db.cursor() as cursor:
            command = """
            CREATE TABLE IF NOT EXISTS games
            (
                id INT PRIMARY KEY,
                info JSON,
                stats_update JSON
            )
            """
            cursor.execute(command)
            cursor.close()
            db.commit()

    def resetDatabase(self) -> None:
        db = self.db
        with db.cursor() as cursor:
            command = "SET FOREIGN_KEY_CHECKS=0;"
            cursor.execute(command)
            command = "SHOW TABLES;"
            cursor.execute(command)
            for table in cursor.fetchall():
                command = "DROP TABLE IF EXISTS " + table[0] + ";"
                cursor.execute(command)
            cursor.close()
            db.commit()
    
    def __del__(self):
        self.db.close()
            
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