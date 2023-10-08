# Contains all functionality relating to database access
# Expects that the database exists, and "__db_user" has permissions on that database
# Migrating up sets up database, and is idempotent (eg. does nothing if database is already set up)
# Migrate down to reset database

import os
import sys
current_script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_script_directory)
from datetime import datetime
import pytz
from typing import List
from mysql.connector import connect
import json
from cleaners import game_cleaner
from pathlib import Path

class Database_Accessor:
    def __init__(self,
                db_name: str = None, 
                db_host: str = None,
                db_port: int = None,
                db_user: str = None,
                db_password: str = None):
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


    def executeSqlCommand(self, command, args: List[str] = []) -> any:
        db = self.db
        output = None
        with db.cursor() as cursor:
            cursor.execute(command, args)
            output = cursor.fetchall()
            cursor.close()
            db.commit()
        return output
    

    def migrateUp(self) -> None:
        def _createCumulativeDataTable():
            command = """
            CREATE TABLE IF NOT EXISTS cumulative_data
            (
                id VARCHAR(128) PRIMARY KEY,
                scale_by_90 JSON
            )
            """
            self.executeSqlCommand(command=command)

            command = """
                SELECT NULL FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
                WHERE CONSTRAINT_SCHEMA = DATABASE()
                AND TABLE_NAME = 'cumulative_data'
                AND CONSTRAINT_NAME = 'match_game_id';
            """
            matchGameIdConstraintExists = self.executeSqlCommand(command=command)
            if not matchGameIdConstraintExists:
                command = """
                    ALTER TABLE cumulative_data
                    ADD CONSTRAINT match_game_id
                    FOREIGN KEY (id)
                    REFERENCES games (id)
                """
                self.executeSqlCommand(command=command)

        def _createMappingTable():
            command = """
            CREATE TABLE IF NOT EXISTS mapping_data
            (
                id VARCHAR(128) PRIMARY KEY,
                mapping JSON
            )
            """
            self.executeSqlCommand(command=command)

        def _createGamesTable():
            command = """
            CREATE TABLE IF NOT EXISTS games
            (
                id VARCHAR(128) PRIMARY KEY,
                eventTime DATETIME,
                info JSON,
                stats_update JSON
            )
            """
            self.executeSqlCommand(command=command)
            command = """
                SELECT NULL FROM INFORMATION_SCHEMA.STATISTICS
                WHERE table_schema = DATABASE() AND table_name = 'games' AND index_name = 'eventTime'
            """
            eventTimeIndexExists = self.executeSqlCommand(command=command)
            if not eventTimeIndexExists:
                command = """
                    ALTER TABLE games
                    ADD INDEX eventTime (eventTime);
                """
                self.executeSqlCommand(command=command)

        def _createLeaguesTable():
            command = """
            CREATE TABLE IF NOT EXISTS leagues
            (
                id VARCHAR(128) PRIMARY KEY,
                league JSON
            )
            """
            self.executeSqlCommand(command=command)

        def _createPlayersTable():
            command = """
            CREATE TABLE IF NOT EXISTS players
            (
                id VARCHAR(128) PRIMARY KEY,
                player JSON
            )
            """
            self.executeSqlCommand(command=command)

        def _createTeamsTable():
            command = """
            CREATE TABLE IF NOT EXISTS teams
            (
                id VARCHAR(128) PRIMARY KEY,
                team JSON
            )
            """
            self.executeSqlCommand(command=command)

        def _createTournamentsTable():
            command = """
            CREATE TABLE IF NOT EXISTS tournaments
            (
                id VARCHAR(128) PRIMARY KEY,
                tournament JSON
            )
            """
            self.executeSqlCommand(command=command)

        def _createTeamRegionMappingTable():
            command = """
            CREATE TABLE IF NOT EXISTS team_region_mapping
            (
                id VARCHAR(128) PRIMARY KEY,
                region VARCHAR(128)
            )
            """
            self.executeSqlCommand(command=command)

        _createLeaguesTable()
        _createMappingTable()
        _createPlayersTable()
        _createTeamsTable()
        _createTournamentsTable()
        _createGamesTable()
        _createCumulativeDataTable()
        _createTeamRegionMappingTable()
        print("Finished migrating up")


    def resetDatabase(self) -> None:
        command = "SET FOREIGN_KEY_CHECKS=0;"
        self.executeSqlCommand(command=command)
        command = "SHOW TABLES;"
        tables = self.executeSqlCommand(command=command)
        for table in tables:
            command = "DROP TABLE IF EXISTS " + table[0] + ";"
            self.executeSqlCommand(command=command)
 
    
    # Insert a row into the table `tableName`, with the specified columns, and associated values.
    # If the row already exists, will replace it if "replaceOnDuplicate" is specified
    def addRowToTable(self, tableName: str, columns: List[str], values: List[dict | int | str], replaceOnDuplicate=True) -> None:
        if len(columns) != len(values):
            raise ValueError("Number of columns does not match number of values.")
        
        # Need to stringify any dicts and dateTimes
        for index in range(len(values)):
            value = values[index]
            if isinstance(value, dict):
                values[index] = json.dumps(value)
            elif isinstance(value, datetime):
                # Convert time to UTC 0 time and then convert to string
                values[index] = pytz.timezone('UTC').localize(value).strftime("%Y-%m-%d %H:%M:%S")
        
        columns = ', '.join(columns)
        valuesPlaceholder = ', '.join(['%s'] * len(values))
        query = ""
        if (replaceOnDuplicate):
             query = "REPLACE INTO {} ({}) VALUES ({});"
        else:
            query = "INSERT IGNORE INTO {} ({}) VALUES ({});"
        query = query.format(tableName, columns, valuesPlaceholder)
        self.executeSqlCommand(command=query, args=tuple(values))


    # Get "columns" from table "tableName"
    # "where_clause" is MYSQL formatted "WHERE" command, to filter results. Example: "id='ESPORTSTMNT03:3197025'"
    # "order_clause" is MYSql formatted "ORDER BY" clause, to order results.
    def getDataFromTable(self, tableName: str, 
    columns: List[str], 
    where_clause: str = None,
    order_clause: str = None,
    limit: int = None,
    offset: int = None) -> List[tuple]:
        query = "SELECT {} FROM {}".format(', '.join(columns), tableName)
        if where_clause:
            query += f" WHERE {where_clause}"
        if order_clause:
            query += f" ORDER BY {order_clause}"
        if limit:
            query += f" LIMIT {limit}"
        if offset:
            query += f" OFFSET {offset}"
        return self.executeSqlCommand(query)


    def __del__(self):
        self.db.close()


# This is for testing:
if __name__ == "__main__":
    dao = Database_Accessor()
    directory_path = Path(os.path.abspath("/Users/matthewwu/Desktop/RiotData/games"))

    # Getting data
    result = dao.getDataFromTable("games", ["id", "info"])
    print(dao.getDataFromTable(tableName="games", columns=["id"], where_clause="id='ESPORTSTMNT03:3199178'", limit=1))

"""
    for file_path in directory_path.iterdir():
        if not file_path.is_file():
            continue
        with open(file_path, "r") as json_file:
            game_data = json.load(json_file)
            game, stats, eventTime = game_cleaner.cleanGameData(game_data)
            primary_key = game["game_info"]["platformGameId"]
            print(primary_key)
            dao.addRowToTable(tableName="games", columns=["id", "info", "stats_update", "eventTime"], values=[primary_key, game, stats, eventTime])
"""