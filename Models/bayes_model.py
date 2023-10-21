from typing import List
import json
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ranking_model_interface import Ranking_Model
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline, Pipeline
import pandas as pd
import numpy as np

from dao.util import getCumulativeStatsForAllTeams 
from dao.database_accessor import Database_Accessor
from collections import defaultdict

class BayesModel(Ranking_Model):
    def __init__(self) -> None:
        self.model_trained = False
        self.pipeline: Pipeline = None
        super().__init__()
    
    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        """
        Return the top `n_teams` teams in the global rankings
        """

        if not self.model_trained: self.fit_model()

        db_accessor = Database_Accessor(
            db_name="games",
            db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
            db_user="data_cleaner",
        )

        # to account for red-side/blue-side bias that might be picked up by 
        # our training model, for each match involving team A and team B,
        # we should assign team A to team 1 and team B to team 2 and predict,
        # AND flip it around to assign team A -> team 2 and team B -> team 1.
        # However, due to time constraints, we are only rolling with performing
        # the first prediction outlined above. Should we have some time remaining,
        # we should re-visit this and resolve this issue.
        cum_stats_all_teams = getCumulativeStatsForAllTeams(db_accessor, n_teams)

        # ISSUES WITH getCumulativeStatsForAllTeams?
        # - when passed n_teams ranging from [23, 50], only returns 23 teams
        # - doesn't seem to skip teams without a region (try running the method without specifying n_teams)

        cum_stats_formatted = []

        for k, v in cum_stats_all_teams.items():
            v["team_id"] = k
            cum_stats_formatted.append(v)
            
        expected_wins = defaultdict(int)

        def parse_team_cumulative_data(container: dict, raw_data: dict, key_prefix: str):
            for k, v in raw_data.items():
                if k == "team_id": continue
                new_key = f"{key_prefix}_{k}"

                if isinstance(v, (int, float)):
                    container[new_key] = v
                elif isinstance(v, list):
                    container[new_key] = v[0]
                else:
                    print(f"UNKNOWN VALUE TYPE ENCOUNTERED! type: {type(v)}; value: {v}")

        total_matches_considered = 0
        for i in range(len(cum_stats_formatted)):
            team_1 = cum_stats_formatted[i]

            for j in range(i + 1, len(cum_stats_formatted)):
                team_2 = cum_stats_formatted[j]
                # print(team_1['team_id'], team_2['team_id'])

                data_dict = {}
                parse_team_cumulative_data(data_dict, team_1, "team_1")
                parse_team_cumulative_data(data_dict, team_2, "team_2")
                data_df = pd.DataFrame(data_dict, index=[0])
                predictions = self.pipeline.predict_proba(data_df)[0]
                print(f"expected outcome between {team_1['team_id']} and {team_2['team_id']}: {predictions}")
                
                expected_wins[team_1['team_id']] += predictions[0]
                expected_wins[team_2['team_id']] += predictions[1]
                total_matches_considered += 1
        

        def fetch_team_info(team_id: str, expected_wins: float) -> dict:
            db_data = db_accessor.getDataFromTable(
                "teams", 
                ["team"], 
                where_clause=f"id = '{team_id}'",
            )

            if not db_data[0][0]:
                print(f"team with team id {team_id} doesn't exist in Teams table")
                return { "expected_wins": expected_wins }

            team_data = json.loads(db_data[0][0])
            return {
                "team_id": team_id,
                "team_code": team_data["acronym"],
                "team_name": team_data["name"],
                "expected_wins": expected_wins
            }
        
        ret = [fetch_team_info(k, v) for k, v in sorted(expected_wins.items(), key=lambda i: i[1], reverse=True)]
            
        for i in range(len(ret)): ret[i]["rank"] = i + 1

        # print(f"total_matches_considered: {total_matches_considered}")
        # print(len(cum_stats_formatted))
        # print(ret)

        return ret
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        return super().get_tournament_rankings(tournament_id, stage)
    
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        return super().get_custom_rankings(teams)
    
    def separate_xy(self, df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
        return (df.drop(columns=["winner"]), df["winner"])
    
    def fit_model(self, X_train: pd.DataFrame = None, y_train: pd.DataFrame = None) -> None:
        # for speeding up development only; call self.get_training_testing_datasets() later.
        with open("bruh-0.json", "r") as f:
            self.raw_data_dict = json.loads(f.read())
        df = pd.DataFrame(self.raw_data_dict)
        df["winner"] = np.where(df["winner"] == 100, "BLUSIDE", "REDSIDE")
        
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=123) # 80-20 split
        X_train, y_train = self.separate_xy(train_df)
        X_test, y_test = self.separate_xy(test_df)

        scaler = StandardScaler()
        ohe = OneHotEncoder(dtype=int, sparse_output=False)
        cols = list(X_train.columns)
        ohe_feats = ["team_1_region", "team_2_region"]
        numeric_feats = list(filter(lambda c: c not in ohe_feats, cols))

        preprocessor = make_column_transformer(
            (scaler, numeric_feats),
            (ohe, ohe_feats),
        )

        pipeline = make_pipeline(preprocessor, GaussianNB())
        cv_score = cross_validate(pipeline, X_train, y_train, return_train_score=True, cv=10)

        print("CROSS VALIDATION RESULTS (VALIDATION)\t ===> ", cv_score["test_score"].mean())
        print("CROSS VALIDATION RESULTS (TRAIN)\t ===> ", cv_score["train_score"].mean())

        pipeline.fit(X_train, y_train)
        self.pipeline = pipeline
        self.model_trained = True

        print("---")
        print("FINAL TEST SCORE\t\t\t ===> ", pipeline.score(X_test, y_test))


bm = BayesModel()
bm.get_global_rankings(38)