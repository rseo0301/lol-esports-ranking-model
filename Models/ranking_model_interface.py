from abc import ABC, abstractmethod
from typing import List

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

    @abstractmethod
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        pass