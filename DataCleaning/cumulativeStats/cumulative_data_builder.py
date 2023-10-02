# Class to build up "cumulative stats" for each team

class Cumulative_Stats_Builder:
    def __init__(self) -> Cumulative_Stats_Builder:
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
        
    def addGamePlayed(self, game_info: dict, stats_info: dict) -> tuple(dict, dict):
        team1_id, team2_id = self._getTeamIdFromGameInfo(game_info)
        self._updateTeamCumulativeStats(team_id=team1_id, game_info=game_info, stats_info=stats_info)
        self._updateTeamCumulativeStats(team_id=team2_id, game_info=game_info, stats_info=stats_info)
        return (self.getCumulativeStatsForTeam(team1_id), self.getCumulativeStatsForTeam(team2_id))

    def getCumulativeStatsForTeam(self, team_id: str) -> dict:
        return self.team_stats[team_id]['cumulativeStats']
    
    def _getTeamIdsFromGameInfo(self, game_info: dict) -> tuple(str, str):
        return ("team-1-id", "team-2-id")

    # Update the cumulative stats for the given team_id
    # after they have played a game that resulted in 'game_info' and 'stats_info'
    def _updateTeamCumulativeStats(self, team_id: str, game_info: dict, stats_info: dict) -> dict:
        # Add handling for if this is the first game this team has played
        new_n_games: int = self.team_stats[team_id]['n_games'] + 1
        old_weighted_count: float = self.team_stats[team_id]['weighted_count']
        new_weighted_count: float = old_weighted_count + (0.9**new_n_games)
        new_cumulative_stats = {}
        for key, value in self.getCumulativeStatsForTeam(team_id=team_id).items():
            # Check if this works for all keys. They might not all be numerical
            new_cumulative_stats[key] = (value*old_weighted_count*0.9+value)/new_weighted_count
        
        self.team_stats[team_id]['n_games'] = new_n_games
        self.team_stats[team_id]['weighted_count'] = new_weighted_count
        self.team_stats[team_id]['cumulativeStats'] = new_cumulative_stats
        return new_cumulative_stats
        