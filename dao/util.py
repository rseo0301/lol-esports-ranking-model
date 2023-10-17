# Utility file
from logging import error
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
def getCumulativeDataForTournament(db_accessor: Database_Accessor, tournament_id: str, stage_name: str) -> dict:
    tournament_data = db_accessor.getDataFromTable(tableName="tournaments", columns=["tournament"], where_clause=f"id='{tournament_id}'")
    if not tournament_data:
        error(f"Could not find tournament with id '{tournament_id}'")
        return None
    tournament = json.loads(tournament_data[0][0])
    stage = [stage for stage in tournament['stages'] if stage['name'].lower() == stage_name.lower()]
    if not stage:
        stage_names = [f"{stage['name']}" for stage in tournament['stages']]
        spacer = "\n   "
        error(f"Could not find stage '{stage_name}' in tournament '{tournament_id}'. Valid stages for this tournament are: {spacer}{spacer.join(stage_names)}")
        return None
    stage = stage[0]
    game_ids: List[str] = []
    for section in stage['sections']:
        for match in section['matches']:
            for game in match['games']:
                game_ids.append(game['id'])
    return game_ids

    # tournament['sections']['matches']
    
    """
    tournamnet['stages'] is an arry of objects, that look like
    {
        name: slug
        type: idk
        slug: slug
        sections: [sections]
    }

    sections look like:
    {
        name: idk
        matches: [matches]
    }

    matches look like:
    {
        ...,
        games: [games]
    }

    games look like:
    {
        ...,
        id: maps to gameID,
        teams: [...]
    }

    We want to return:
    {
        team1_id: {cumulative_stats},
        …
    }
    """


# Debugging and testing:
if __name__ == "__main__":
    dao: Database_Accessor = Database_Accessor()
    cumulative_data_for_teams = getCumulativeStatsForTeams(db_accessor=dao, team_ids=["107580483738977500", "109981647134921596"])

    cumulative_data_for_tournament = getCumulativeDataForTournament(db_accessor=dao, tournament_id="103462454280724883", stage_name="asdf")

    print("Hello World")