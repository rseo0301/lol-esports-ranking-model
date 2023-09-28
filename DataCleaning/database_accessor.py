# Contains all functionality relating to database access
# Expects that the database exists, and "__db_user" has permissions on that database
# Migrating up sets up database, and is idempotent (eg. does nothing if database is already set up)
# Migrate down to reset database

import string
from mysql.connector import MySQLConnection, connect
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