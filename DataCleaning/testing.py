# Matthew's custom script with various functionality for testing
import os
import json
import argparse
from pathlib import Path

from dao.database_accessor import Database_Accessor


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--game_data_dir', help='Stub')
    parser.add_argument('--esports_data_dir', help='If specified, shorten all data files in esports data directory to first 50 elements')
    parser.add_argument('--show_cumulative_data', help='Prints out cumulative data', action='store_true')

    args = parser.parse_args()
    db_accessor: Database_Accessor = Database_Accessor(db_name = 'games', 
    db_host = 'riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com', 
    db_user = 'data_cleaner')
    
    
    # Shorten data objects in esports data directory
    if args.esports_data_dir:
        directory_path = Path(os.path.abspath(args.esports_data_dir))
        for file_path in directory_path.iterdir():
            if not file_path.is_file():
                continue

            with open(file_path, "r") as json_file:
                arr=json.load(json_file)
                arr=arr[:50]
                with open(file_path, 'w') as json_file:
                    json.dump(arr, json_file)
                    print(f"{file_path} written")

    if True or args.show_cumulative_data:
        gameCount: int = 0
        while(True):
            cumulative_stats = db_accessor.getDataFromTable(tableName="cumulative_data", columns=["id", "scale_by_90"], limit=10, offset=gameCount)
            if not cumulative_stats:
                break
            for id, stats in cumulative_stats:
                stats = json.loads(stats)
                print(stats)
            gameCount += len(cumulative_stats)
