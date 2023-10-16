# Utility file
import os
import sys
current_script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_script_directory)
from database_accessor import Database_Accessor
import json
from typing import Tuple, List

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

# Returns the latest cumulative stats for the list of teams
def getCumulativeStatsForTeams(db_accessor: Database_Accessor, team_ids: List[str]) -> dict:
    id_filter = [f"id='{id}'" for id in team_ids]
    teams_data = db_accessor.getDataFromTable(tableName="teams", columns=["id", "latest_cumulative_stats"], where_clause=" OR ".join(id_filter))
    ret = {}
    for team_data in teams_data:
        team_id = team_data[0]
        cumulative_stats = json.loads(team_data[1])
        ret[team_id] = cumulative_stats
    return ret

# Get the cumulative stats for every team, just before they play the first game of the tournmanet/stage
def getCumulativeDataForTournament(tournament_id: str, stage: str) -> dict:
    pass
    """
    {
        team1_id: {cumulative_stats},
        …
    }
    """


# Debugging and testing:
if __name__ == "__main__":
    dao: Database_Accessor = Database_Accessor()
    temp = getCumulativeStatsForTeams(db_accessor=dao, team_ids=["107580483738977500", "109981647134921596"])
    print(temp["109981647134921596"])
    print("Hello World")