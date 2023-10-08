# Cleaner for all data files, except for "games"
# Cleans mapping_data.json
# Takes in a JSON object, cleans it, and outputs a JSON object that we can store in our database

from typing import List
class Esports_Cleaner:
    def __init__(self):
        pass

    def cleanLeaguesData(self, data: List[dict]) -> List[dict]:
        return data

    def cleanMappingData(self, data: List[dict]) -> List[dict]:
        return data

    def cleanPlayersData(self, data: List[dict]) -> List[dict]:
        return data

    def cleanTeamsData(self, data: List[dict]) -> List[dict]:
        return data

    def cleanTournamentsData(self, data: List[dict]) -> List[dict]:
        return data
