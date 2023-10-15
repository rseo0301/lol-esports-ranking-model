from typing import List
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database_accessor import Database_Accessor
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import OneHotEncoder

db_access = Database_Accessor(
    db_name="games",
    db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
    db_user="data_cleaner",
)

COLUMNS = [
    "region",                   # list[str], str ('region not found')
    "avg_kd_ratio",             # int/float
    "barons_per_game",          # int/float
    "gold_diff_at_14",          # int/float     
    "overall_winrate",          # int/float
    "avg_time_per_win",         # int/float
    "dragons_per_game",         # int/float
    "first_blood_rate",         # int/float
    "first_tower_rate",         # int/float
    "heralds_per_game",         # int/float
    "turrets_per_game",         # int/float
    "avg_time_per_loss",        # int/float
    "gold_diff_per_min",        # int/float
    "avg_assists_per_kill",     # int/float
    "vision_score_per_minute",  # int/float
]

class CumulativeDataParser:
    def __init__(self, testing = False) -> None:
        self.db_accessor = Database_Accessor(
            db_name="games",
            db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
            db_user="data_cleaner",
        )
        self.raw_data_dict = {}
        self.populate_dict()
        self.shuffle_state = 123
        self.testing = testing

    def populate_dict(self) -> None:
        for c in COLUMNS: 
            self.raw_data_dict[f"team_1_{c}"] = []
            self.raw_data_dict[f"team_2_{c}"] = []
        self.raw_data_dict["winner"] = []
    
    def parse_dict(self, data_to_parse: any) -> None:
        self.raw_data_dict['winner'].append(data_to_parse['meta']['winning_team'])
        teams = ["team_1", "team_2"]

        for team in teams:
            for k in data_to_parse[team].keys():
                new_key = f"{team}_{k}"
                val = data_to_parse[team][k]
                if isinstance(val, (int, float)):
                    self.raw_data_dict[new_key].append(val) # handle numeric fields
                elif isinstance(val, list):
                    self.raw_data_dict[new_key].append(val[0]) # handle regions
                elif val == "region not found": # handle unknown regions
                    self.raw_data_dict[new_key].append(None)
    
    def contains_keys(self, obj: dict) -> bool:
        has_meta = "meta" in obj
        has_team_1 = "team_1" in obj
        has_team_2 = "team_2" in obj
        return has_team_1 and has_team_2 and has_meta
    
    def fetch_data(self, limit: int, offset: int) -> List[tuple]:
        return self.db_accessor.getDataFromTable(
            tableName="cumulative_data", 
            columns=["id", "scale_by_90"], 
            limit=limit, 
            offset=offset,
        )
    
    def write_to_disk(self, skipped_rows: List[str]) -> None:
        f = open("bruh-0.json", "w")
        f.write(json.dumps(self.raw_data_dict, indent=4))
        f.close()

        f = open("skipped_rows.json", "w")
        f.write(json.dumps(skipped_rows, indent=4))
        f.close()

    def get_parsed_df_split(self, split_x_and_y = True, log_results = False) -> list:
        QUERY_LIMIT, count = 50, 0
        rows_parsed = 0
        skipped_row_ids = []

        cumulative_stats = self.fetch_data(limit=QUERY_LIMIT, offset=count * QUERY_LIMIT)

        while cumulative_stats:
            for row in cumulative_stats:
                stats = json.loads(row[1])
                if self.contains_keys(stats):
                    self.parse_dict(stats)
                    print(f"parsed row {row[0]}")
                    rows_parsed += 1
                else:
                    print(f"skipped row {row[0]}")
                    skipped_row_ids.append(row[0])
            count += 1
            cumulative_stats = self.fetch_data(limit=QUERY_LIMIT, offset=count * QUERY_LIMIT)

        if log_results: 
            print("Logging results + skipped row IDs...")
            self.write_to_disk(skipped_row_ids)

        print(f"parsed {rows_parsed} rows in total; skipped {len(skipped_row_ids)} rows")
        print(f"total: {rows_parsed + len(skipped_row_ids)} rows observed")

        df = pd.DataFrame(self.raw_data_dict)

        if split_x_and_y:
            # initialize encoder and fit data
            region = df[['team_1_region', 'team_2_region']].values.reshape(-1, 2)
            enc = OneHotEncoder()
            enc.fit(region)
            # transform data
            one_hot = enc.transform(region).todense()
            # turn one hot into dataframe
            one_hot_df = pd.DataFrame(one_hot, columns=enc.get_feature_names_out(["team_1_region", "team_2_region"]))
            # add one_hot features and remove initial region features
            X = pd.concat([df, one_hot_df], axis=1)
            X = X.drop(columns=["team_1_region", "team_2_region", "winner"])

            df["winner"] = np.where(df["winner"] == 100, 1, 0)
            y = df["winner"]
            # return X_train, X_test, y_train, y_test (4-item list)
            return train_test_split(X, y, test_size=0.2, random_state=self.shuffle_state)
        
        # return training and testing sets; X and y are attached together (2-item list)
        return train_test_split(df, test_size=0.2, random_state=self.shuffle_state)
    


# standalone function for simplicity!!
def get_training_and_test_datasets(split_x_and_y = True, log_results = False) -> list:
    c = CumulativeDataParser()
    return c.get_parsed_df_split(split_x_and_y=split_x_and_y, log_results=log_results)