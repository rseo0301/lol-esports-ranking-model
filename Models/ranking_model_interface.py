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

    @abstractmethod
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        pass

    @abstractmethod
    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        pass

    def get_training_test_datasets(self, split_x_and_y = True, log_results = False) -> list:
        return get_training_and_test_datasets(split_x_and_y=split_x_and_y, log_results=log_results)