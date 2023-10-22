from typing import List

import numpy as np
import pandas as pd
import requests
from sklearn.preprocessing import OneHotEncoder
from Models.ranking_model_interface import Ranking_Model
from API.main import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from dao.util import getCumulativeDataForTournament, getCumulativeStatsForTeams

class RandomForest(Ranking_Model):

    model = RandomForestClassifier(n_estimators=150, min_samples_split=2, min_samples_leaf=1, max_features='sqrt', max_depth=7, bootstrap=True)
    dao: Database_Accessor = Database_Accessor(db_host='riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com')

    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        return super().get_global_rankings(n_teams)
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        cumulative_data_for_tournament = getCumulativeDataForTournament(db_accessor=self.dao, tournament_id=tournament_id, stage_name=stage)
        if cumulative_data_for_tournament:
            print(f"Cumulative data found for games in {tournament_id}")
            data = self.create_dataframe(cumulative_data_for_tournament)
            predictions = self.predict(data[0])
            wins = self.calculate_wins(predictions=predictions, matchups=data[1])

            return [wins]

        print("No data found")
        return []
    
    def get_custom_rankings(self, teams: List) -> List[dict]:
        cumulative_data_for_teams: getCumulativeStatsForTeams(db_accessor= self.dao, team_ids=teams)
        if cumulative_data_for_teams:
            print(f"Cumulative data found for games in list")
            data = self.create_dataframe(cumulative_data_for_teams)
            predictions = self.predict(data[0])
            wins = self.calculate_wins(predictions=predictions, matchups=data[1])

            return [wins]

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

        region_one = df[['team_1_region']].values.reshape(-1, 1)
        enc = OneHotEncoder(categories=[["BRAZIL", "CHINA", "COMMONWEALTH OF INDEPENDENT STATES", "EMEA", "HONG KONG, MACAU, TAIWAN", "JAPAN",
                                        'KOREA', "LATIN AMERICA", "LATIN AMERICA NORTH", "LATIN AMERICA SOUTH", "NORTH AMERICA", "OCEANIA", "VIETNAM", "None"]])
        enc.fit(region_one)
        # transform data
        one_hot = enc.transform(region_one).todense()
        # turn one hot into dataframe
        one_hot_df = pd.DataFrame(one_hot, columns=enc.get_feature_names_out(["team_1_region"]))

        region_two = df[['team_2_region']].values.reshape(-1, 1)
        enc_two = OneHotEncoder(categories=[["BRAZIL", "CHINA", "COMMONWEALTH OF INDEPENDENT STATES", "EMEA", "HONG KONG, MACAU, TAIWAN", "JAPAN",
                                        'KOREA', "LATIN AMERICA", "LATIN AMERICA NORTH", "LATIN AMERICA SOUTH", "NORTH AMERICA", "OCEANIA", "VIETNAM", "None"]])
        enc_two.fit(region_two)
        # transform data
        two_hot = enc.transform(region_two).todense()
        # turn one hot into dataframe
        two_hot_df = pd.DataFrame(two_hot, columns=enc.get_feature_names_out(["team_2_region"]))

        # add one_hot features and remove initial region features
        X = pd.concat([df, one_hot_df, two_hot_df], axis=1)
        X = X.drop(columns=["team_1_region", "team_2_region"])

        return [X, matchups]
    
    def fit(self, X, y):
        self.model
        self.model.fit(X, y)

    def predict(self, X):
        result = self.model.predict_proba(X)
        return result

    def worlds_predictions(self):
        df = pd.read_csv("../worlds_2023.csv")
        matchups = df[["team_1_name", "team_2_name"]]
        df = df.drop(columns=["team_1_name", "team_2_name"])

        result = self.predict(df)
        self.calculate_wins(result, matchups)   
        
    def calculate_wins(self, predictions, matchups):
        wins = {}
        for i, pred in enumerate(predictions):
            team_1 = matchups.iloc[i].iloc[0]
            team_2 = matchups.iloc[i].iloc[1]
            if team_1 in wins:
                wins[team_1] = wins[team_1] + pred[1]
            else:
                wins[team_1] = pred[1]
            
            if team_2 in wins:
                wins[team_2] = wins[team_2] + pred[0]
            else:
                wins[team_2] = pred[0]
            
        sorted_wins = sorted(wins.items(), key=lambda x:x[1], reverse=True)
        sorted_dict = dict(sorted_wins)
        for key in sorted_dict:
            print(key, " : ", "{:.2f}".format(sorted_dict[key]))
        return sorted_dict

    def create_matchups(self, data) -> List:
        teams = list(data.keys())

        matchups = pd.DataFrame(columns=['team_1_name', 'team_2_name'])
        matchup_data = []

        for i in range(len(teams) - 1):
            team_1: dict = data[teams[i]] # dict containing data of first team
            t1_edited = {}

            for key, value in team_1.items():
                t1_edited["team_1_" + key] = team_1[key]

            for j in range(i+1,len(teams)):
                team_2: dict = data[teams[j]] # dict containing data of second team

                t2_edited = {}
                
                for key, value in team_2.items():
                    t2_edited["team_2_" + key] = team_2[key]

                new_row = {'team_1_name': teams[i], 'team_2_name': teams[j]}
                print(new_row)
                matchups.loc[len(matchups)] = new_row
                t2_edited.update(t1_edited)
                matchup_data.append(t2_edited)
        
        return [matchups, matchup_data]

    def optimal_parameters(self):
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
        search = RandomizedSearchCV(estimator=model, param_distributions= param_grid, cv=10, verbose=2, n_jobs=-1, n_iter=150)
        search.fit(self.datasets[0], self.datasets[2])
        print(search.best_params_)
        print(search.score(self.datasets[1], self.datasets[3]))
        #{'n_estimators': 110, 'min_samples_split': 5, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'max_depth': 7, 'bootstrap': True}

rfc = RandomForest()
rfc.get_training_test_datasets()
rfc.fit(rfc.datasets[0], rfc.datasets[2])
results = rfc.get_tournament_rankings("108998961191900167", "Knockouts")
