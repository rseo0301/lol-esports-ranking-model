# Utility file
from database_accessor import Database_Accessor
import json
from typing import Tuple

# TODO Could probably build a cache for mapping table
def getTeamIdsFromGameInfo(db_accessor: Database_Accessor, game_info: dict) -> Tuple[str, str]:
    platformGameId = game_info['game_info']['platformGameId']
    mapping_data = db_accessor.getDataFromTable(
        tableName='mapping_data', 
        columns=['mapping'], 
        where_clause=f"id='{platformGameId}'")
    if not mapping_data:
        return None
    teamMapping = json.loads(mapping_data[0][0])["teamMapping"]
    return teamMapping["100"], teamMapping["200"]

# Return the winning team, given game_info
def getWinningTeam(game_info: dict) -> int:
    return game_info['game_end']['winningTeam']

# Debugging and testing:
if __name__ == "__main__":
    print("Hello World")