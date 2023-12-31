# Utility file
from logging import error
import os
import sys
current_script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_script_directory)
from database_accessor import Database_Accessor
import json
from typing import Tuple, List

# Could probably build a cache for mapping table
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

# Returns the latest cumulative stats for all teams
# If n_teams is specified, will return 'n_teams' number of random teams
def getCumulativeStatsForAllTeams(db_accessor: Database_Accessor, n_teams: int = None) -> dict:
    processed_teams = 0
    ret = {}
    while True:
        if n_teams and processed_teams >= n_teams:
            break
        teams_data = db_accessor.getDataFromTable(tableName="teams", columns=["id", "latest_cumulative_stats"], limit=50, offset=processed_teams)
        if not teams_data:
            break
        processed_teams += len(teams_data)
        for team_data in teams_data:
            if not team_data[1]:
                continue
            team_id = team_data[0]
            team_stats = json.loads(team_data[1])
            ret[team_id] = team_stats
            if n_teams and len(ret) >= n_teams:
                break
    return ret

# Get the cumulative stats for every team, just before they play the first game of the tournmanet/stage
def getCumulativeDataForTournament(db_accessor: Database_Accessor, tournament_id: str, stage_name: str) -> dict:
    # Gets the game ids for all games played in this stage of this tournament
    def getStageEsportsGameIds() -> List[str]:
        tournament_data = db_accessor.getDataFromTable(tableName="tournaments", columns=["tournament"], where_clause=f"id='{tournament_id}'")
        if not tournament_data:
            error(f"Could not find tournament with id '{tournament_id}'")
            return None
        tournament = json.loads(tournament_data[0][0])
        stage = [stage for stage in tournament['stages'] if stage['name'].strip().lower().replace('-', '').replace('_','') == stage_name.strip().lower().replace('-','').replace('_','')]
        if not stage:
            stage_names = [f"{stage['name']}" for stage in tournament['stages']]
            spacer = "\n   "
            error(f"Could not find stage '{stage_name}' in tournament '{tournament['name']}' ({tournament_id}). Valid stages for this tournament are: {spacer}{spacer.join(stage_names)}")
            return None
        stage = stage[0]
        esports_game_ids: List[str] = []
        for section in stage['sections']:
            for match in section['matches']:
                for game in match['games']:
                    esports_game_ids.append(game['id'])
        return esports_game_ids
    
    # Given a list of esports game ids,
    # return an object that maps each team_id to the first game they played (from given list of game ids)
    def getTeamsFirstGames(esports_game_ids: List[str]) -> dict:
        where_clause: str = " OR ".join([f"esportsGameId='{esports_game_id}'" for esports_game_id in esports_game_ids])
        order_clause = "eventTime DESC"
        games_data = db_accessor.getDataFromTable(tableName="games", columns=["id", "info"], where_clause=where_clause, order_clause=order_clause)
        team_first_game = {}
        for game_data in games_data:
            game_id = game_data[0]
            game_info: dict = json.loads(game_data[1])
            team1_id, team2_id = getTeamIdsFromGameInfo(db_accessor=db_accessor, game_info=game_info)
            team_first_game[team1_id] = game_id
            team_first_game[team2_id] = game_id
        return team_first_game
    
    # Expects an input of {team1_id: game1_id, team2_id: game2_id, ...}
    # Will return the associated cumulative stats for each game as {team1_id: cumulative_stats1, team2_id: cumulative_stats2, ...}
    def getCumulativeStatsForTeamsGames(teams_games: dict) -> dict:
        from DataCleaning.cumulativeStats.cumulative_data_builder import Cumulative_Stats_Builder
        where_clause = " OR ".join([f"games.id='{game_id}'" for game_id in teams_games.values()])
        cumulative_stats_data = db_accessor.getDataFromTable(
            tableName="cumulative_data", 
            join_clause="games AS games ON cumulative_data.id = games.id", 
            columns=["games.id", "games.info", "games.stats_update", "scale_by_90"], 
            where_clause=where_clause, 
            order_clause="eventTime DESC",
        )
        teams_cumulative_stats = {}
        csb = Cumulative_Stats_Builder(db_accessor)

        for data in cumulative_stats_data:
            game_info = json.loads(data[1])
            stats_info = json.loads(data[2])
            stats = json.loads(data[3])
            team1_id, team2_id = stats['meta']['team1_id'], stats['meta']['team2_id']
            
            team_1_stats, team_2_stats = stats.get('team_1'), stats.get('team_2')
            if (not team_1_stats) or (not team_2_stats):
                new_t1_stats, new_t2_stats = csb.addGamePlayed(game_info, stats_info)
                team_1_stats = team_1_stats if team_1_stats else new_t1_stats
                team_2_stats = team_2_stats if team_2_stats else new_t2_stats
                
            teams_cumulative_stats[team1_id] = team_1_stats
            teams_cumulative_stats[team2_id] = team_2_stats
            
        return teams_cumulative_stats
            
    esports_game_ids = getStageEsportsGameIds()
    if not esports_game_ids:
        return {}
    first_games = getTeamsFirstGames(esports_game_ids=esports_game_ids)
    if not first_games:
        return {}
    teams_cumulative_stats = getCumulativeStatsForTeamsGames(teams_games=first_games)
    return teams_cumulative_stats

# Returns the list of stages avaialable for a tournament
def getStagesForTournament(db_accessor: Database_Accessor, tournament_id: str) -> List[str]:
    tournament_data = db_accessor.getDataFromTable(tableName="tournaments", columns=["tournament"], where_clause=f"id='{tournament_id}'")
    if not tournament_data:
        error(f"Could not find tournament with id '{tournament_id}'")
        return None
    tournament = json.loads(tournament_data[0][0])
    return [stage['name'] for stage in tournament['stages']]

# Returns a list of all teams ids that have played a game on, or later than the given year
def getTeamsInYear(db_accessor: Database_Accessor, year: int = 2023) -> List:
    teams_data = db_accessor.getDataFromTable(
        tableName="teams",
        columns=["teams.id"],
        join_clause="games AS games ON teams.latest_game = games.id", 
        where_clause=f"YEAR(games.eventTime) >= {year}")
    return [team_data[0] for team_data in teams_data]

# Debugging and testing:
if __name__ == "__main__":
    # dao: Database_Accessor = Database_Accessor(db_host='riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com')
    dao: Database_Accessor = Database_Accessor()
    # cumulative_data_for_teams = getCumulativeStatsForTeams(db_accessor=dao, team_ids=["107580483738977500", "109981647134921596"])
    '''
    print(getStagesForTournament(db_accessor=dao, tournament_id='103462439438682788'))

    tournaments_data = dao.getDataFromTable(tableName="tournaments", columns=["tournament"])
    for tournament_data in tournaments_data:
        tournament = json.loads(tournament_data[0])
        cumulative_data_for_tournament = getCumulativeDataForTournament(db_accessor=dao, tournament_id=tournament['id'], stage_name="Playoffs")
        if cumulative_data_for_tournament:
            print(f"Cumulative data found for games in f{tournament['id']}")
            sys.exit(1)
    '''

    print(getTeamsInYear(db_accessor=dao, year=2009))

    print("Hello World")
