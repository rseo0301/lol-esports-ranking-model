from abc import ABC, abstractmethod
from typing import List
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