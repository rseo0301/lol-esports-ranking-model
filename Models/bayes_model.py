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

from dao.util import (
    getCumulativeStatsForAllTeams, 
    getCumulativeDataForTournament,
    getCumulativeStatsForTeams,
)
from dao.database_accessor import Database_Accessor
from collections import defaultdict
from DataCleaning.datasetPrep.cumulative_df import get_training_and_test_datasets

class BayesModel(Ranking_Model):
    def __init__(self) -> None:
        self.model_trained = False
        self.pipeline: Pipeline = None
        self.db_accessor = Database_Accessor(
            db_name="games",
            db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
            db_user="data_cleaner",
        )
        super().__init__()
    
    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        """
        Return the top `n_teams` teams in the global rankings
        """

        if not self.model_trained: self.fit_model()

        # to account for red-side/blue-side bias that might be picked up by 
        # our training model, for each match involving team A and team B,
        # we should assign team A to team 1 and team B to team 2 and predict,
        # AND flip it around to assign team A -> team 2 and team B -> team 1.
        # However, due to time constraints, we are only rolling with performing
        # the first prediction outlined above. Should we have some time remaining,
        # we should re-visit this and resolve this issue.
        cum_stats_all_teams = getCumulativeStatsForAllTeams(self.db_accessor)

        # ISSUES WITH getCumulativeStatsForAllTeams?
        # - when passed n_teams ranging from [23, 50], only returns 23 teams
        # - doesn't seem to skip teams without a region (try running the method without specifying n_teams)

        cum_stats_formatted = []

        for k, v in cum_stats_all_teams.items():
            v["team_id"] = k
            cum_stats_formatted.append(v)
            
        expected_wins = defaultdict(int)

        total_matches_considered = 0
        for i in range(len(cum_stats_formatted)):
            team_1 = cum_stats_formatted[i]

            for j in range(i + 1, len(cum_stats_formatted)):
                team_2 = cum_stats_formatted[j]

                data_dict = {}
                self.parse_team_cumulative_data(data_dict, team_1, "team_1")
                self.parse_team_cumulative_data(data_dict, team_2, "team_2")
                data_df = pd.DataFrame(data_dict, index=[0])
                predictions = self.pipeline.predict_proba(data_df)[0]
                print(f"expected outcome between {team_1['team_id']} and {team_2['team_id']}: {predictions}")
                
                expected_wins[team_1['team_id']] += predictions[0]
                expected_wins[team_2['team_id']] += predictions[1]
                total_matches_considered += 1
        
        ret = [
            self.fetch_team_info(k, v) 
            for k, v in sorted(
                expected_wins.items(), 
                key=lambda i: i[1], 
                reverse=True,
            )
        ]
            
        for i in range(len(ret)): ret[i]["rank"] = i + 1
        return ret
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        if not self.model_trained: self.fit_model()

        cum_stats_all_teams = getCumulativeDataForTournament(
            self.db_accessor,
            tournament_id,
            stage,
        )

        cum_stats_formatted = []
        expected_wins = defaultdict(int)

        for k, v in cum_stats_all_teams.items():
            v["team_id"] = k
            cum_stats_formatted.append(v)
        
        total_matches_considered = 0
        for i in range(len(cum_stats_formatted)):
            team_1 = cum_stats_formatted[i]

            for j in range(i + 1, len(cum_stats_formatted)):
                team_2 = cum_stats_formatted[j]

                data_dict = {}
                self.parse_team_cumulative_data(data_dict, team_1, "team_1")
                self.parse_team_cumulative_data(data_dict, team_2, "team_2")
                data_df = pd.DataFrame(data_dict, index=[0])

                predictions = self.pipeline.predict_proba(data_df)[0]
                print(f"expected outcome between {team_1['team_id']} and {team_2['team_id']}: {predictions}")
                
                expected_wins[team_1['team_id']] += predictions[0]
                expected_wins[team_2['team_id']] += predictions[1]
                total_matches_considered += 1
        
        ret = [
            self.fetch_team_info(k, v) 
            for k, v in sorted(
                expected_wins.items(), 
                key=lambda i: i[1], 
                reverse=True,
            )
        ]
            
        for i in range(len(ret)): ret[i]["rank"] = i + 1

        print(ret)
        return ret
    
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        if not self.model_trained: self.fit_model()
        if len(teams) < 2:
            res = []
            for i, t in enumerate(teams):
                team_info = self.fetch_team_info(t, -1)
                del team_info["expected_wins"]
                team_info["rank"] = i + 1
                res.append(team_info)
            print(res)
            return res


        cum_stats_all_teams = getCumulativeStatsForTeams(
            self.db_accessor,
            teams,
        )

        print(cum_stats_all_teams)

        cum_stats_formatted = []
        expected_wins = defaultdict(int)

        for k, v in cum_stats_all_teams.items():
            v["team_id"] = k
            cum_stats_formatted.append(v)
        
        total_matches_considered = 0

        print(cum_stats_formatted)
        for i in range(len(cum_stats_formatted)):
            team_1 = cum_stats_formatted[i]

            for j in range(i + 1, len(cum_stats_formatted)):
                team_2 = cum_stats_formatted[j]

                data_dict = {}
                self.parse_team_cumulative_data(data_dict, team_1, "team_1")
                self.parse_team_cumulative_data(data_dict, team_2, "team_2")
                data_df = pd.DataFrame(data_dict, index=[0])

                predictions = self.pipeline.predict_proba(data_df)[0]
                print(f"expected outcome between {team_1['team_id']} and {team_2['team_id']}: {predictions}")
                
                expected_wins[team_1['team_id']] += predictions[0]
                expected_wins[team_2['team_id']] += predictions[1]
                total_matches_considered += 1
        
        ret = [
            self.fetch_team_info(k, v) 
            for k, v in sorted(
                expected_wins.items(), 
                key=lambda i: i[1], 
                reverse=True,
            )
        ]
            
        for i in range(len(ret)): ret[i]["rank"] = i + 1

        print(ret)
        return ret
    
    def parse_team_cumulative_data(
        self,
        container: dict, 
        raw_data: dict, 
        key_prefix: str,
    ) -> None:
        for k, v in raw_data.items():
            if k == "team_id": continue
            new_key = f"{key_prefix}_{k}"

            if isinstance(v, (int, float, str)):
                container[new_key] = v
            elif isinstance(v, list):
                container[new_key] = v[0]
            else:
                print(f"UNKNOWN VALUE TYPE! type: {type(v)}; value: {v}")

    def fetch_team_info(self, team_id: str, expected_wins: float) -> dict:
        db_data = self.db_accessor.getDataFromTable(
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
# bm.get_global_rankings(38)
# bm.get_tournament_rankings("103462439438682788", "Playoffs")
bm.get_custom_rankings([
    "103461966951059521", 
    "99566404585387054",
    "98767991853197861",
    "98767991926151025",
    "98767991866488695",
    "100725845018863243",
    "98926509884398584",
])
# bm.fit_model()

# test tournament ID: 103462439438682788
# test stage name: "groups" (for more, see: https://github.com/rseo0301/lol-esports-ranking-model/blob/regression-model/supplement-docs.md)