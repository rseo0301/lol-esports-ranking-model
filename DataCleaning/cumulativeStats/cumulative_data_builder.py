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
                    ...
                }
            },
            ...
        }
        """
        
    def addGamePlayed(game_info: dict, stats_info: dict) -> tuple(dict, dict):
        pass

    def getCumulativeStatsForTeam(team_id: str) -> dict:
        pass