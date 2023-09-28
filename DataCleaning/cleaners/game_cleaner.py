# Takes in a "game" JSON object, cleans it, and outputs a JSON object that we can store in our database
import json
import os
from typing import Dict, List

# Given a gamedata object, clean it, and return a tuple:
# First element will be dictionary, keyed by event type
# Second element will be list of stat updates
def cleanGameData(gameData: List[Dict]) -> tuple[Dict, List]:
    gameDataRet = {}
    statsUpdateRet = []
    for event in gameData:
        if not isinstance(event, Dict):
            continue
        eventType = event["eventType"].lower()
        match eventType:
            case "stats_update":
                statsUpdateRet.append(_cleanStatsUpdate(event))
            case "epic_monster_kill":
                _appendToObjectArray(gameDataRet, eventType, _cleanEpicMonsterKill(event))
            case "champion_kill":
                _appendToObjectArray(gameDataRet, eventType, _cleanChampionKill(event))
            case "ward_placed":
                _appendToObjectArray(gameDataRet, eventType, _cleanWardPlaced(event))
            case "ward_killed":
                _appendToObjectArray(gameDataRet, eventType, _cleanWardKilled(event))
            case "turret_plate_destroyed":
                _appendToObjectArray(gameDataRet, eventType, _cleanTurretPlateDestroyed(event))
            case "building_destroyed":
                _appendToObjectArray(gameDataRet, eventType, _cleanBuildingDestroyed(event))
            case "game_info":
                gameDataRet[eventType] = _cleanGameInfo(event)
            case "game_end":
                gameDataRet[eventType] = _cleanGameEnd(event)


    return (gameDataRet, statsUpdateRet)


def _cleanStatsUpdate(info: Dict) -> Dict:
    def cleanStatsUpdateParticipant(info: List[Dict]) -> Dict:
        desiredKeys = ["totalGold", "XP"]
        ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)

        rawStats = info["stats"]
        desiredStats = {}
        statsDesiredKeys = ["MINIONS_KILLED", "CHAMPIONS_KILLED", "NUM_DEATHS", "ASSISTS", "VISION_SCORE", "XP"]
        for rawStat in rawStats:
            statName = rawStat["name"]
            if statName in statsDesiredKeys:
                desiredStats[statName] = rawStat["value"]
                statsDesiredKeys.remove(statName)
            if not statsDesiredKeys:
                break
        
        ret["stats"] = desiredStats
        return ret
    
    def cleanStatsUpdateTeam(info: Dict) -> Dict:
        desiredKeys = ["inhibKills","towerKills","teamID","baronKills","dragonKills","assists","totalGold","championKills","deaths"]
        ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    desiredKeys = ["gameTime", "gameOver"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    ret["participants"] = []
    for participant in info["participants"]:
        ret["participants"].append(cleanStatsUpdateParticipant(participant))
    ret["teams"] = []
    for team in info["teams"]:
        ret["teams"].append(cleanStatsUpdateTeam(team))
    return ret

def _cleanGameEnd(info: Dict) -> Dict:
    desiredKeys = ["gameTime", "winningTeam"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    return ret

def _cleanWardKilled(info: Dict) -> Dict:
    desiredKeys = ["gameTime", "position", "wardType", "killer"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    return ret

def _cleanWardPlaced(info: Dict) -> Dict:
    desiredKeys = ["gameTime", "position", "wardType", "placer"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    return ret

def _cleanTurretPlateDestroyed(info: Dict) -> Dict:
    desiredKeys = ["gameTime", "lastHitter", "lane", "teamID", "assistants"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    return ret

def _cleanEpicMonsterKill(info: Dict) -> Dict:
    desiredKeys = ["gameTime", "killer", "monsterType", "inEnemyJungle", "killerTeamID", "assistants"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    return ret

def _cleanChampionKill(info: Dict) -> Dict:
    desiredKeys = ["gameTime", "killer", "killStreakLength", "killerTeamID", "bounty", "assistants"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    return ret

def _cleanBuildingDestroyed(info: Dict) -> Dict:
    desiredKeys = ["gameTime", "buildingType", "lane", "turretTier", "teamID", "assistants"]
    defaultValues = {"turretTier": None}
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys, defaultValues=defaultValues)
    return ret

def _cleanGameInfo(info: Dict) -> Dict:
    def cleanGameInfoParticipant(info: Dict) -> Dict:
        desiredKeys = ["teamID", "participantID", "championName", "summonerName"]
        ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    desiredKeys = ["eventTime", "eventType", "platformGameId", "gameName"]
    ret = extractDesiredKeys(object=info, desiredKeys=desiredKeys)
    ret["participants"] = []
    for participant in info["participants"]:
        ret["participants"].append(cleanGameInfoParticipant(participant))
    return ret



# Returns an object containing all the "desiredKeys" from "object"
# "defaultValues" are used if a "desiredKey" doesn't exist in "object"
def extractDesiredKeys(object: Dict, desiredKeys: List, defaultValues: Dict = {}) -> Dict:
    ret = {}
    for key in desiredKeys:
        if key in object.keys():
            ret[key] = object[key]
        elif key in defaultValues.keys():
            ret[key] = defaultValues[key]
    return ret

# Appends "value" to "object[key]"
# Assumes that "object[key]" is an array
def _appendToObjectArray(object: Dict, key, value):
    if key not in object.keys():
        object[key] = []
    object[key].append(value)

# Uncomment the following code for testing/debugging
# if __name__ == "__main__":
#     filePath = os.path.abspath("game-data.json")
#     with open(filePath, "r") as json_file:
#         game_data = json.load(json_file)
#         game, stats = cleanGameData(game_data)
#         print(game)

