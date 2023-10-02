# Matthew's custom script with various functionality for testing
import os
import json
import argparse
from pathlib import Path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--game_data_dir', help='Stub')
    parser.add_argument('--esports_data_dir', help='If specified, shorten all data files in esports data directory to first 50 elements')
    args = parser.parse_args()
    
    
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