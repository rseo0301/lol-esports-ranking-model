# Utility file
from database_accessor import Database_Accessor
from typing import Tuple

# MATTHEW TODO
def getTeamIdsFromGameInfo(db_accessor: Database_Accessor, game_info: dict) -> Tuple[str, str]:
    return ("team-1-id", "team-2-id")
    platformGameId = game_info['game_info']['platformGameId']
    teamMapping = db_accessor.getDataFromTable(
        tableName='mapping_data', 
        columns=['mapping'], 
        where_clause=f"id={platformGameId}")
    return ("team-1-id", "team-2-id")


# Debugging and testing:
if __name__ == "__main__":
    print("Hello World")