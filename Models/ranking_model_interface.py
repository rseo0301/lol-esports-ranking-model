from abc import ABC, abstractmethod
from typing import List

import pandas as pd
from DataCleaning.datasetPrep.cumulative_df import get_training_and_test_datasets

class Ranking_Model(ABC):
    """
    According to this doc:
    https://docs.google.com/document/d/1Klodp4YqE6bIOES026ecmNb_jS5IOntRqLv5EmDAXyc/edit
    Responses should be in this format:
    [
        {"team_id": "100205573495116443"
        "team_code": "GEN",
        "team_name": "Gen.G"
        "rank": 1
        },
        ...
    ]
    """

    @abstractmethod
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        pass

    @abstractmethod
    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        pass

    """
    Input should be a list of team ids
    """
    @abstractmethod
    def get_custom_rankings(self, team_ids: List[str]) -> List[dict]:
        """
        Output should be in this format
        [
            {"team_id": "100205573495116443"
            "team_code": "GEN",
            "team_name": "Gen.G"
            "rank": 1
            },
            ...
        ]
        """
        pass

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def get_training_test_datasets(self, split_x_and_y = True, log_results = False) -> list:
        self.datasets = get_training_and_test_datasets(split_x_and_y=split_x_and_y, log_results=log_results)
        return self.datasets
    
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
                matchups.loc[len(matchups)] = new_row
                t2_edited.update(t1_edited)
                matchup_data.append(t2_edited)
        
        return [matchups, matchup_data]