# Class to build up "cumulative stats" for each team
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from typing import Tuple
from database_accessor import Database_Accessor
from util import getTeamIdsFromGameInfo
class Cumulative_Stats_Builder:
    def __init__(self, db_accessor: Database_Accessor):
        self.db_accessor = db_accessor
        self.team_stats = {}
        """
        Teams stats will look like this:
        {
            id: {
                n_games: int,
                weighted_count: number,
                cumulativeStats: {
                    gold_differential_at_14: number,
                    gold_differential_per_minute: number,
                    ...
                }
            },
            ...
        }
        """
        
    def addGamePlayed(self, game_info: dict, stats_info: dict) -> Tuple[dict, dict]:
        team1_id, team2_id = getTeamIdsFromGameInfo(db_accessor=self.db_accessor, game_info=game_info)
        self._updateTeamCumulativeStats(team_id=team1_id, game_info=game_info, stats_info=stats_info)
        self._updateTeamCumulativeStats(team_id=team2_id, game_info=game_info, stats_info=stats_info)
        return (self.getCumulativeStatsForTeam(team1_id), self.getCumulativeStatsForTeam(team2_id))

    def getCumulativeStatsForTeam(self, team_id: str) -> dict:
        return self.team_stats[team_id]['cumulativeStats']


    # Update the cumulative stats for the given team_id
    # after they have played a game that resulted in 'game_info' and 'stats_info'
    def _updateTeamCumulativeStats(self, team_id: str, game_info: dict, stats_info: dict) -> dict:
        # Add handling for if this is the first game this team has played
        new_n_games: int = self.team_stats[team_id]['n_games'] + 1
        old_weighted_count: float = self.team_stats[team_id]['weighted_count']
        new_weighted_count: float = old_weighted_count*0.9 + 1
        new_cumulative_stats = {}
        for key, value in self.getCumulativeStatsForTeam(team_id=team_id).items():
            # Check if this works for all keys. They might not all be numerical
            new_cumulative_stats[key] = (value*old_weighted_count*0.9+value)/new_weighted_count
        
        self.team_stats[team_id]['n_games'] = new_n_games
        self.team_stats[team_id]['weighted_count'] = new_weighted_count
        self.team_stats[team_id]['cumulativeStats'] = new_cumulative_stats
        return new_cumulative_stats
        
# Testing
if __name__=="__main__":
    dao: Database_Accessor = Database_Accessor(
        db_name="games", 
        db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
        db_port=3306, 
        db_user="data_cleaner",
        db_password="")
    cumulative_stats_builder = Cumulative_Stats_Builder(db_accessor=dao)

    games = dao.getDataFromTable(tableName="games", 
    columns=["info", "stats_update"], 
    order_clause="eventTime ASC", 
    limit=10)

    for game in games:
        game_info = json.loads(game[0])
        stats_info = json.loads(game[1])
        temp = cumulative_stats_builder.addGamePlayed(game_info=game_info, stats_info=stats_info)
        pass

    print("Hello")