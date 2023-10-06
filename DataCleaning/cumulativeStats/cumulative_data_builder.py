# Class to build up "cumulative stats" for each team
# "game_stats" is the cumulative stats we get from one game
from distutils.log import error
import sys
import os
from tokenize import Number
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from typing import Tuple
from database_accessor import Database_Accessor
from util import getTeamIdsFromGameInfo

CUMULATIVE_STATS_KEYS = [
    'first_blood_rate',
    'avg_kd_ratio',
    'avg_assists_per_kill',
    'barons_per_game',
    'dragons_per_game',
    'heralds_per_game',
    'turrets_per_game',
    'first_tower_rate',
    'vision_score_per_minute',
    'avg_time_per_win',
    'avg_time_per_loss',
    'overall_winrate',
    'gold_diff_per_min',
    'gold_diff_at_14',
    'region'
]
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
        team1_cumulative_stats, team2_cumulative_stats = self._parseCumulativeStatsFromData(game_info=game_info, stats_info=stats_info)
        
        self._updateTeamCumulativeStats(team_id=team1_id, cumulative_stats=team1_cumulative_stats)
        self._updateTeamCumulativeStats(team_id=team2_id, cumulative_stats=team2_cumulative_stats)
        return self.getCumulativeStatsForTeam(team1_id), self.getCumulativeStatsForTeam(team2_id)


    def getCumulativeStatsForTeam(self, team_id: str) -> dict:
        return self.team_stats[team_id]['cumulativeStats']


    # After team with "team_id" plays a game that results in "cumulative_stats",
    # Update the team's cumulative stats
    def _updateTeamCumulativeStats(self, team_id: str, cumulative_stats: dict) -> dict:
        if team_id not in self.team_stats:
            default_stats = {}
            for key in CUMULATIVE_STATS_KEYS:
                match key:
                    case 'region':
                        default_stats[key] = None
                    case other:
                        default_stats[key] = 0
            self.team_stats[team_id] = {}
            self.team_stats[team_id]['cumulativeStats'] = default_stats
            self.team_stats[team_id]['n_games'] = 0
            self.team_stats[team_id]['weighted_count'] = 0
        

        new_n_games: int = self.team_stats[team_id]['n_games'] + 1
        old_weighted_count: float = self.team_stats[team_id]['weighted_count']
        new_weighted_count: float = old_weighted_count*0.9 + 1
        new_cumulative_stats = {}
        for key, value in self.getCumulativeStatsForTeam(team_id=team_id).items():
            if key == 'region':
                new_cumulative_stats[key] = cumulative_stats[key]
                continue
            new_cumulative_stats[key] = (value*old_weighted_count*0.9 + cumulative_stats[key])/new_weighted_count
        
        self.team_stats[team_id]['n_games'] = new_n_games
        self.team_stats[team_id]['weighted_count'] = new_weighted_count
        self.team_stats[team_id]['cumulativeStats'] = new_cumulative_stats
        return new_cumulative_stats
        

    # Given game and stats info, convert it into cumulative stats format
    # Will return cumulative stats for (team1, team2)
    def _parseCumulativeStatsFromData(self, game_info: dict, stats_info: dict) -> Tuple[dict, dict]:
        team1_stats = {}
        team2_stats = {}
        team_info = stats_info['stats_update'][-1]['teams']
        team1_info = [info for info in team_info if info['teamID'] == 100][0]
        team2_info = [info for info in team_info if info['teamID'] == 200][0]
        kills = sorted(game_info['champion_kill'], key=lambda obj: obj['gameTime'])
        
        def addStatsToTeams(key: str, values: Tuple):
            team1_stats[key] = values[0]
            team2_stats[key] = values[1]

        def get_team_kills() -> Tuple[int, int]:
            if 'championKills' in team1_info and 'championKills' in team2_info:
                team1_kills, team2_kills = team1_info['championsKills'], team2_info['championsKills']
            else:
                team1_kills = len([kill for kill in kills if kill['killerTeamID'] == 100])
                team2_kills = len([kill for kill in kills if kill['killerTeamID'] == 200])
            return team1_kills,team2_kills
        
        def get_first_blood_team() -> int:
            killer_team = kills[0]['killerTeamID']
            return killer_team
        
        def get_avg_kd_ratio() -> Tuple[float, float]:
            team1_kills, team2_kills = get_team_kills()
            team1_deaths, team2_deaths = team1_info['deaths'], team2_info['deaths']
            return float(team1_kills/team1_deaths), float(team2_kills/team2_deaths)

        def get_avg_assists_per_kill() -> Tuple[float, float]:
            team1_kills, team2_kills = get_team_kills()
            team1_assists, team2_assists = team1_info['assists'], team2_info['assists']
            return float(team1_assists/team1_kills), float(team2_assists/team2_kills)
        
        def get_barons_per_game() -> Tuple[int, int]:
            team1_barons = stats_info['stats_update'][-1]['teams'][0]['baronKills']
            team2_barons = stats_info['stats_update'][-1]['teams'][1]['baronKills']
            if stats_info['stats_update'][-1]['teams'][0]['teamID'] != 100:
                error("Found a game where team 0 in stats info, does not correlate to a teamID of 100")
            return team1_barons, team2_barons
        
        def get_dragons_per_game() -> Tuple[int, int]:
            team1_dragons = stats_info['stats_update'][-1]['teams'][0]['dragonKills']
            team2_dragons = stats_info['stats_update'][-1]['teams'][1]['dragonKills']
            return team1_dragons, team2_dragons

        def get_heralds_per_game() -> Tuple[int, int]:
            team1_heralds = len([event for event in game_info['epic_monster_kill'] if event['monsterType'].lower() == 'riftHerald' and event['killerTeamID'] == 100])
            team2_heralds = len([event for event in game_info['epic_monster_kill'] if event['monsterType'].lower() == 'riftHerald' and event['killerTeamID'] == 200])
            return team1_heralds, team2_heralds
        
        def get_turrets_per_game() -> Tuple[int, int]:
            team1_turrets = stats_info['stats_update'][-1]['teams'][0]['towerKills']
            team2_turrets = stats_info['stats_update'][-1]['teams'][1]['towerKills']
            return team1_turrets, team2_turrets
        
        def get_first_turret_team() -> int:
            turrets_destroyed = [event for event in game_info['building_destroyed'] if event['buildingType'] == 'turret']
            return turrets_destroyed[0]['teamID']




        if get_first_blood_team() == 100:
            addStatsToTeams(key='first_blood_rate', values=(1, 0))
        elif get_first_blood_team() == 200:
            addStatsToTeams(key='first_blood_rate', values=(0, 1))
        addStatsToTeams(key='avg_kd_ratio', values=get_avg_kd_ratio())
        addStatsToTeams(key='avg_assists_per_kill', values=get_avg_assists_per_kill())
        addStatsToTeams(key='barons_per_game', values=get_barons_per_game())
        addStatsToTeams(key='dragons_per_game', values=get_dragons_per_game())
        addStatsToTeams(key='heralds_per_game', values=get_heralds_per_game())
        addStatsToTeams(key='turrets_per_game', values=get_turrets_per_game())
        if get_first_turret_team() == 100:
            addStatsToTeams(key='first_tower_rate', values=(1, 0))
        elif get_first_turret_team() == 200:
            addStatsToTeams(key='first_tower_rate', values=(0, 1))
            
        addStatsToTeams(key='vision_score_per_minute', values=get_avg_assists_per_kill())
        addStatsToTeams(key='avg_time_per_win', values=get_avg_assists_per_kill())
        addStatsToTeams(key='avg_time_per_loss', values=get_avg_assists_per_kill())
        addStatsToTeams(key='overall_winrate', values=get_avg_assists_per_kill())
        addStatsToTeams(key='gold_diff_per_min', values=get_avg_assists_per_kill())
        addStatsToTeams(key='gold_diff_at_14', values=get_avg_assists_per_kill())
        addStatsToTeams(key='region', values=get_avg_assists_per_kill())
        
        # Sanity check
        if team1_stats.keys() != CUMULATIVE_STATS_KEYS:
            error("Error in cumulative_data_builder: while parsing cumulative stats from gamedata, parsed keys don't match CUMULATIVE_STATS_KEYS")

        return team1_stats, team2_stats



    

# Testing
if __name__=="__main__":
    dao: Database_Accessor = Database_Accessor(
        db_name="games", 
        # db_host="riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com",
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
        team1_stats, team2_stats = cumulative_stats_builder.addGamePlayed(game_info=game_info, stats_info=stats_info)
        print("Hello World")

    print("Hello World")