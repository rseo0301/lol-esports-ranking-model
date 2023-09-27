# Takes in a "game" JSON object, cleans it, and outputs a JSON object that we can store in our database
import json
import os
from typing import Dict, List

# Given a gamedata object, clean it, and return a tuple:
# First element will be dictionary, keyed by event type
# Second element will be list of stat updates
def cleanGameData(gameData: List[Dict]) -> tuple[Dict, List]:
    print(list(gameData[0].keys()))
    return ([], list())





filePath = os.path.abspath("game-data.json")
with open(filePath, "r") as json_file:
    game_data = json.load(json_file)
    print(type(game_data))
    print(type(game_data[0]))
    cleanGameData(game_data)

