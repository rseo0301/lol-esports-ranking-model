# Takes in a "game" JSON object, cleans it, and outputs a JSON object that we can store in our database
from distutils.log import warn
import json
import os
from datetime import datetime
from typing import Dict, List

class Game_Cleaner:
    def __init__(self):
        self.skipped_games = []

    # Given a gamedata object, clean it, and return a tuple:
    # First element will be dictionary, keyed by event type
    # Second element will be list of stat updates
    def cleanGameData(self, gameData: List[Dict]) -> tuple[Dict, Dict, datetime]:
        gameDataRet = {}
        statsUpdateRet = {}

        try:
            # Filter out all stats_update events, except for the 14 minute mark and game end
            # TODO should paramaterize this somewhere
            stats_at_14 = next(event for event in gameData if (event['eventType'].lower() == 'stats_update' and event['gameTime'] >= 14*60*1000))
            stats_at_game_end = next(event for event in gameData if (event['eventType'].lower() == 'stats_update' and event['gameOver'] == True))
            gameData = [event for event in gameData if event['eventType'].lower() != 'stats_update']
            gameData += [stats_at_14, stats_at_game_end]
            
            for event in gameData:
                if not isinstance(event, Dict):
                    continue
                eventType = event["eventType"].lower()
                match eventType:
                    case "stats_update":
                        self._appendToObjectArray(statsUpdateRet, eventType, self._cleanStatsUpdate(event))
                    case "epic_monster_kill":
                        self._appendToObjectArray(gameDataRet, eventType, self._cleanEpicMonsterKill(event))
                    case "champion_kill":
                        self._appendToObjectArray(gameDataRet, eventType, self._cleanChampionKill(event))
                    case "ward_placed":
                        self._appendToObjectArray(gameDataRet, eventType, self._cleanWardPlaced(event))
                    case "ward_killed":
                        self._appendToObjectArray(gameDataRet, eventType, self._cleanWardKilled(event))
                    case "turret_plate_destroyed":
                        self._appendToObjectArray(gameDataRet, eventType, self._cleanTurretPlateDestroyed(event))
                    case "building_destroyed":
                        self._appendToObjectArray(gameDataRet, eventType, self._cleanBuildingDestroyed(event))
                    case "game_info":
                        gameDataRet[eventType] = self._cleanGameInfo(event)
                    case "game_end":
                        gameDataRet[eventType] = self._cleanGameEnd(event)
                        
            # eventTime is formatted like this: "2023-07-22T17:14:16.356Z"
            eventTime = datetime.strptime(gameDataRet['game_info']['eventTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
            return (gameDataRet, statsUpdateRet, eventTime)
        except Exception as e:
            gameID = gameData[0].get('platformGameId', 'game_id_not_found')
            warn(f"An error occurred while processing game {gameID}: {e}")
            self.skipped_games.append(gameID)


    def _cleanStatsUpdate(self, info: Dict) -> Dict:
        def cleanStatsUpdateParticipant(info: List[Dict]) -> Dict:
            desiredKeys = ["totalGold", "XP"]
            ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)

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
            ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
            return ret

        desiredKeys = ["gameTime", "gameOver"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        ret["participants"] = []
        for participant in info["participants"]:
            ret["participants"].append(cleanStatsUpdateParticipant(participant))
        ret["teams"] = []
        for team in info["teams"]:
            ret["teams"].append(cleanStatsUpdateTeam(team))
        return ret

    def _cleanGameEnd(self, info: Dict) -> Dict:
        desiredKeys = ["gameTime", "winningTeam"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    def _cleanWardKilled(self, info: Dict) -> Dict:
        desiredKeys = ["gameTime", "position", "wardType", "killer"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    def _cleanWardPlaced(self, info: Dict) -> Dict:
        desiredKeys = ["gameTime", "position", "wardType", "placer"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    def _cleanTurretPlateDestroyed(self, info: Dict) -> Dict:
        desiredKeys = ["gameTime", "lastHitter", "lane", "teamID", "assistants"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    def _cleanEpicMonsterKill(self, info: Dict) -> Dict:
        desiredKeys = ["gameTime", "killer", "monsterType", "inEnemyJungle", "killerTeamID", "assistants"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    def _cleanChampionKill(self, info: Dict) -> Dict:
        desiredKeys = ["gameTime", "killer", "killStreakLength", "killerTeamID", "bounty", "assistants"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        return ret

    def _cleanBuildingDestroyed(self, info: Dict) -> Dict:
        desiredKeys = ["gameTime", "buildingType", "lane", "turretTier", "teamID", "assistants"]
        defaultValues = {"turretTier": None}
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys, defaultValues=defaultValues)
        return ret

    def _cleanGameInfo(self, info: Dict) -> Dict:
        def cleanGameInfoParticipant(info: Dict) -> Dict:
            desiredKeys = ["teamID", "participantID", "championName", "summonerName"]
            ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
            return ret

        desiredKeys = ["eventTime", "eventType", "platformGameId", "gameName"]
        ret = self._extractDesiredKeys(object=info, desiredKeys=desiredKeys)
        ret["participants"] = []
        for participant in info["participants"]:
            ret["participants"].append(cleanGameInfoParticipant(participant))
        return ret



    # Returns an object containing all the "desiredKeys" from "object"
    # "defaultValues" are used if a "desiredKey" doesn't exist in "object"
    def _extractDesiredKeys(self, object: Dict, desiredKeys: List, defaultValues: Dict = {}) -> Dict:
        ret = {}
        for key in desiredKeys:
            if key in object.keys():
                ret[key] = object[key]
            elif key in defaultValues.keys():
                ret[key] = defaultValues[key]
        return ret

    # Appends "value" to "object[key]"
    # Assumes that "object[key]" is an array
    def _appendToObjectArray(self, object: Dict, key, value):
        if key not in object.keys():
            object[key] = []
        object[key].append(value)

    def __del__(self):
        if len(self.skipped_games) == 0:
            return
        warn("The following games could not be properly parsed, and so were skipped: " + ', '.join(self.skipped_games))


# Uncomment the following code for testing/debugging
# if __name__ == "__main__":
#     filePath = os.path.abspath("game-data.json")
#     game_cleaner: Game_Cleaner = Game_Cleaner()
#     with open(filePath, "r") as json_file:
#         game_data = json.load(json_file)
#         game, stats = game_cleaner.cleanGameData(game_data)
#         print(game)

