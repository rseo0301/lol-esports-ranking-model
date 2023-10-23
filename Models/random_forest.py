from collections import defaultdict
from typing import List
import numpy as np
import pandas as pd
import requests
from sklearn.preprocessing import OneHotEncoder
from Models.ranking_model_interface import Ranking_Model
from API.main import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from dao.util import getCumulativeDataForTournament, getCumulativeStatsForAllTeams, getCumulativeStatsForTeams

class RandomForest(Ranking_Model):

    model = RandomForestClassifier(n_estimators=120, min_samples_split=2, min_samples_leaf=2, max_features='sqrt', max_depth=5, bootstrap=False)

    def __init__(self) -> None:
        self._dao = Database_Accessor(db_host='riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com')
        self.get_training_test_datasets()
        self.fit(self.datasets[0], self.datasets[2])
        super().__init__()

    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:

        # checks if global rankings have already been calculated
        if not self._global_rankings:
            cumulative_data = getCumulativeStatsForAllTeams(db_accessor= self._dao)
            if cumulative_data:
                print(f"Cumulative data found for all teams")
                data = self.create_dataframe(cumulative_data)
                predictions = self.predict(data[0])
                wins = self.calculate_wins(predictions=predictions, matchups=data[1])
                self._global_rankings = self._sort_rankings(wins)

                print(self._global_rankings[:n_teams])

        return self._global_rankings[:n_teams]
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        cumulative_data_for_tournament = getCumulativeDataForTournament(db_accessor=self._dao, tournament_id=tournament_id, stage_name=stage)
        if cumulative_data_for_tournament:
            print(f"Cumulative data found for games in {tournament_id}")
            data = self.create_dataframe(cumulative_data_for_tournament)
            predictions = self.predict(data[0])
            wins = self.calculate_wins(predictions=predictions, matchups=data[1])
            output = self._sort_rankings(wins)

            print(output)
            return output

        return []
    
    def get_custom_rankings(self, teams: List) -> List[dict]:
        cumulative_data_for_teams = getCumulativeStatsForTeams(db_accessor= self._dao, team_ids=teams)
        if cumulative_data_for_teams:
            print(f"Cumulative data found for teams in list")
            data = self.create_dataframe(cumulative_data_for_teams)
            predictions = self.predict(data[0])
            wins = self.calculate_wins(predictions=predictions, matchups=data[1])
            output = self._sort_rankings(wins)

            print(output)
            return output

        print("No data found")
        return []
    
    # returns array of [cumulative data, corresponding matchups]
    # cumulative data must be predicted using model first
    def create_dataframe(self, data) -> List:
        
        # below function returns array in form of [matchups, matchup_data]
        matchup_info = self.create_matchups(data)
        matchups = matchup_info[0]
        matchup_data = matchup_info[1]
        
        # reorganize order of array as in model
        df = pd.DataFrame(matchup_data)
        cols = ["team_1_avg_kd_ratio","team_2_avg_kd_ratio","team_1_barons_per_game","team_2_barons_per_game","team_1_gold_diff_at_14",
                "team_2_gold_diff_at_14","team_1_overall_winrate","team_2_overall_winrate","team_1_avg_time_per_win",
                "team_2_avg_time_per_win","team_1_dragons_per_game","team_2_dragons_per_game","team_1_first_blood_rate","team_2_first_blood_rate",
                "team_1_first_tower_rate","team_2_first_tower_rate","team_1_heralds_per_game","team_2_heralds_per_game","team_1_turrets_per_game",
                "team_2_turrets_per_game","team_1_avg_time_per_loss","team_2_avg_time_per_loss","team_1_gold_diff_per_min","team_2_gold_diff_per_min",
                "team_1_avg_assists_per_kill","team_2_avg_assists_per_kill","team_1_vision_score_per_minute","team_2_vision_score_per_minute","team_1_region", "team_2_region"]
        df = df[cols]

        region_one = self.parse_region(df[['team_1_region']].values.reshape(-1, 1))
        region_two = self.parse_region(df[['team_2_region']].values.reshape(-1, 1))

        # initialize and fit encoder
        enc = OneHotEncoder(categories=[["BRAZIL", "CHINA", "COMMONWEALTH OF INDEPENDENT STATES", "EMEA", "HONG KONG, MACAU, TAIWAN", "JAPAN",
                                        'KOREA', "LATIN AMERICA", "LATIN AMERICA NORTH", "LATIN AMERICA SOUTH", "NORTH AMERICA", "OCEANIA", "VIETNAM", "None"]])
        enc.fit(region_one)
        # transform data and turn into dataframe
        one_hot = enc.transform(region_one).todense()
        one_hot_df = pd.DataFrame(one_hot, columns=enc.get_feature_names_out(["team_1_region"]))

        two_hot = enc.transform(region_two).todense()
        two_hot_df = pd.DataFrame(two_hot, columns=enc.get_feature_names_out(["team_2_region"]))

        # add one_hot features and remove initial region features
        X = pd.concat([df, one_hot_df, two_hot_df], axis=1)
        X = X.drop(columns=["team_1_region", "team_2_region"])

        return [X, matchups]
    
    def parse_region(self, region):
        for i, value in enumerate(region):
            if value[0] == 'region not found':
                region[i][0] = 'None'
        return region

    def fit(self, X, y):
        weights = X[['weights']].values
        weights = weights.flatten()
        X = X.drop(columns=['weights'])
        self.model.fit(X, y, sample_weight=weights)

    def predict(self, X):
        result = self.model.predict_proba(X)
        return result

    def worlds_predictions(self):
        df = pd.read_csv("../worlds_2023.csv")
        matchups = df[["team_1_name", "team_2_name"]]
        df = df.drop(columns=["team_1_name", "team_2_name"])

        predictions = self.predict(df)
        results = self.calculate_wins(predictions, matchups)
        print(results)   
        
    def _optimal_parameters(self):
        # Number of trees in random forest
        n_estimators = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
        max_features = ['log2', 'sqrt']
        max_depth = [3,4,5,6,7]
        min_samples_split = [2, 5]
        min_samples_leaf = [1, 2]
        bootstrap = [True, False]
        # Create the param grid
        param_grid = {'n_estimators': n_estimators,
                    'max_features': max_features,
                    'max_depth': max_depth,
                    'min_samples_split': min_samples_split,
                    'min_samples_leaf': min_samples_leaf,
                    'bootstrap': bootstrap}

        model = RandomForestClassifier()

        weights = self.datasets[0][['weights']].values
        weights = weights.flatten()
        search = RandomizedSearchCV(estimator=model, param_distributions= param_grid, cv=10, verbose=2, n_jobs=-1, n_iter=150)

        self.datasets[0] = self.datasets[0].drop(columns=["weights"])
        search.fit(self.datasets[0], self.datasets[2], sample_weight=weights)
        print(search.best_params_)
        print(search.score(self.datasets[1], self.datasets[3]))

    def _sort_rankings(self, expected_wins: defaultdict[any, int]) -> List[dict]:
        ret = [
            self._fetch_team_info(k, v) 
            for k, v in sorted(
                expected_wins.items(), 
                key=lambda i: i[1], 
                reverse=True,
            )
        ]

        for i in range(len(ret)): ret[i]["rank"] = i + 1

        return ret

    def _fetch_team_info(self, team_id: str, expected_wins: float) -> dict:
        db_data = self._dao.getDataFromTable(
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

if __name__ == "__main__":
    rfc = RandomForest()
    # rfc.optimal_parameters()
    rfc.get_global_rankings()
    rfc.worlds_predictions()
    tournament_rankings = rfc.get_tournament_rankings("108206581962155974", "Regular Season")
    custom_rankings = rfc.get_custom_rankings([
        "103461966951059521",
        "99566404585387054",
        "98767991853197861",
        "98767991926151025",
        "98767991866488695",
        "100725845018863243",
        "98926509884398584",
    ])
