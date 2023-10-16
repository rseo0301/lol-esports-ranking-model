from typing import List
from Models.ranking_model_interface import Ranking_Model
import random
import string

FAKE_TEAM_NAMES = [
    "Super Monkey",
    "Random Team",
    "Cloud 8",
    "Team Solo Top",
    "Team Solo Bot",
    "Team Everyone Mid",
    "LA Lakers",
    "Lebron James",
    "Super Logical Gaming",
    "Support is so easy",
    "White Rabbit"
    ]

class Mock_Ranking_Model(Ranking_Model):
    def __init__(self):
        self.default_response = [
            {
                "team_id": "100205573495116443",
                "team_code": "GEN",
                "team_name": "Gen.G",
                "rank": 1
            },
            {
                "team_id": "98767991877340524",
                "team_code": "C9",
                "team_name": "Cloud9",
                "rank": 1
            },
            {
                "team_id": "99566404853058754",
                "team_code": "WBG",
                "team_name": "WeiboGaming FAW AUDI",
                "rank": 3
            }
        ]

    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        return self.default_response

    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        return self._generate_random_response(n_teams=n_teams)
    
    def get_custom_rankings(self, team_ids: List[str]) -> List[dict]:
        ret = self._generate_random_response(len(team_ids))
        for i in range(len(team_ids)):
            ret[i]['team_id'] = team_ids[i]
        return ret

    def _generate_random_response(self, n_teams: int = 20) -> List[dict]:
        # teamID is 17 numbers
        response = []
        for i in range(n_teams):
            team = {}
            team['team_id'] = random.randrange(10**16, 10**17)
            team['team_code'] = self._generate_random_team_code()
            team['team_name'] = self._generate_random_team_name()
            team['rank'] = i
            response += [team]
        return response

    def _generate_random_team_code(self) -> str:
        # Define the characters to choose from (capital letters and digits)
        characters = string.ascii_uppercase + string.digits
        # Generate a random string of length 2 or 3
        random_length = random.choice([2, 3])
        random_string = ''.join(random.choice(characters) for _ in range(random_length))
        return random_string
    
    def _generate_random_team_name(self) -> str:
        return random.choice(FAKE_TEAM_NAMES)