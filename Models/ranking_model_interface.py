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
    _global_rankings: List[dict] = []

    def __init__(self):
        self.non_existent_teams = set([
            '99566404845279652', '99566404847770461', '98767991887166787', 
            '101388912911039804', '99566404856367466', '101388912914513220', 
            '103461966986776720', '101422616509070746', '102235771678061291', 
            '103535282124208038', '105709099258505657', '99322214684939974', 
            '99566406064558732', '99566406334639907', '99566406338282437',
        ])
        self._global_rankings = self.get_global_rankings(9999)

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

    def get_training_test_datasets(self, split_x_and_y = True, log_results = False) -> list:
        self.datasets = get_training_and_test_datasets(split_x_and_y=split_x_and_y, log_results=log_results)
        return self.datasets
    
    def calculate_wins(self, predictions, matchups):
        wins = {}
        for i, pred in enumerate(predictions):
            team_1 = matchups.iloc[i].iloc[0]
            team_2 = matchups.iloc[i].iloc[1]

            if self.match_includes_nonexistent_teams(team_1, team_2): continue
            
            if team_1 in wins:
                wins[team_1] = wins[team_1] + pred[1] / 2
            else:
                wins[team_1] = pred[1] / 2
            
            if team_2 in wins:
                wins[team_2] = wins[team_2] + pred[0] / 2
            else:
                wins[team_2] = pred[0] / 2
            
        sorted_wins = sorted(wins.items(), key=lambda x:x[1], reverse=True)
        sorted_dict = dict(sorted_wins)
        return sorted_dict

    def create_matchups(self, data) -> List:
 
        teams = list(data.keys())

        matchups = pd.DataFrame(columns=['team_1_name', 'team_2_name'])
        matchups_swapped = pd.DataFrame(columns=['team_1_name', 'team_2_name'])
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

                matchup = {'team_1_name': teams[i], 'team_2_name': teams[j]}
                matchups.loc[len(matchups)] = matchup
                matchup_swapped = {'team_1_name': teams[j], 'team_2_name': teams[i]}
                matchups_swapped.loc[len(matchups_swapped)] = matchup_swapped
                t2_edited.update(t1_edited)
                matchup_data.append(t2_edited)

        return [pd.concat([matchups, matchups_swapped]), matchup_data]
    
    def match_includes_nonexistent_teams(self, team1_id: str, team2_id: str) -> bool:
        return (team1_id in self.non_existent_teams) or (team2_id in self.non_existent_teams)