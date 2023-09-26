from mysql.connector import MySQLConnection, connect
import argparse

__db = None
__db_host = "localhost"
__db_port = 3306
__db_user = "data_cleaner"
__db_password = ""
__db_name = "games"

def getDb() -> MySQLConnection:
    global __db, __db_host, __db_port, __db_user, __db_password, __db_name
    if __db == None:
        __db = connect(
            host=__db_host,
            user=__db_user,
            port=__db_port,
            password=__db_password,
            database=__db_name
        )
    return __db

def migrateUp() -> None:
    db = getDb()
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
        db.commit()

def resetDatabase() -> None:
    db = getDb()
    with db.cursor() as cursor:
        command = "SHOW TABLES;"
        cursor.execute(command)
        command = "SET FOREIGN_KEY_CHECKS=0;"
        for table in cursor:
            command += "DROP TABLE IF EXISTS " + table[0] + ";"
            print(command)
        cursor.execute(command)
        db.commit()

def initDbVars(args: argparse.Namespace):
    global __db_host, __db_port, __db_user, __db_password, __db_name
    __db_host = args.db_host if args.db_host is not None else __db_host
    __db_port = args.db_port if args.db_port is not None else __db_port
    __db_user = args.db_user if args.db_user is not None else __db_user
    __db_password = args.db_password if args.db_password is not None else __db_password
    __db_name = args.db_name if args.db_name is not None else __db_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--migrate', choices=['up', 'down'], default='up', help='Migrate up to set up the database, migrate down to reset database')
    parser.add_argument('--db_host', help='database host')
    parser.add_argument('--db_port', type=int, help='database port')
    parser.add_argument('--db_user', help='database user')
    parser.add_argument('--db_password', help='database user password')
    parser.add_argument('--db_name', help='database name')
    args = parser.parse_args()
    
    initDbVars(args)
    match args.migrate:
        case 'up':
            migrateUp()
        case 'down':
            resetDatabase()