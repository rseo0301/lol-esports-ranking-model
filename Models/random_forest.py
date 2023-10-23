from typing import List
from Models.ranking_model_interface import Ranking_Model

class RandomForest(Ranking_Model):
    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        return super().get_global_rankings(n_teams)
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        return super().get_tournament_rankings(tournament_id, stage)
    
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        return super().get_custom_rankings(teams)


if __name__=="__main__":
    model = RandomForest()
    model.get_training_test_datasets()


    # def printData():
    #     url = "http://127.0.0.1:5000"
    #     response = requests.get(url + "/api/generate_tournament_data/103462439438682788")
    #     print(response.json())