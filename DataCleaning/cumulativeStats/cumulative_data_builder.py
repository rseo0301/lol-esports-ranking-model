# Class to build up "cumulative stats" for each team
# "game_stats" is the cumulative stats we get from one game
from distutils.log import error
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, ".."))
from tokenize import Number
import json
from typing import Tuple
from dao.database_accessor import Database_Accessor
from dao.util import getTeamIdsFromGameInfo, getWinningTeam

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
                },
                wins_weighted_count: int,
                losses_weighted_count: int
            },
            ...
        }
        """
    

    # Updates the cumulative stats for the teams involved in the game described by game_info and stats_info
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
            self._init_cumulative_stats_for_team(team_id)
        

        new_n_games: int = self.team_stats[team_id]['n_games'] + 1
        old_weighted_count: float = self.team_stats[team_id]['weighted_count']
        new_weighted_count: float = self._calculate_next_weighted_count(old_weighted_count)
        old_cumulative_stats = self.getCumulativeStatsForTeam(team_id=team_id)
        new_cumulative_stats = {}
        for key in CUMULATIVE_STATS_KEYS:
            if key not in cumulative_stats:
                new_cumulative_stats[key] = old_cumulative_stats[key]
                continue
            if key == 'region':
                new_cumulative_stats[key] = cumulative_stats[key]
                continue
            new_cumulative_stats[key] = (old_cumulative_stats[key]*old_weighted_count*0.9 + cumulative_stats[key])/new_weighted_count
        
        self.team_stats[team_id]['n_games'] = new_n_games
        self.team_stats[team_id]['weighted_count'] = new_weighted_count
        self.team_stats[team_id]['cumulativeStats'] = new_cumulative_stats

        # Update win/loss weighted counts
        if 'avg_time_per_win' in cumulative_stats:
            self.team_stats[team_id]['wins_weighted_count'] = self._calculate_next_weighted_count(self.team_stats[team_id]['wins_weighted_count'])
        elif 'avg_time_per_loss' in cumulative_stats:
            self.team_stats[team_id]['losses_weighted_count'] = self._calculate_next_weighted_count(self.team_stats[team_id]['losses_weighted_count'])

        return new_cumulative_stats


    # Given a weighted count, calculate the "new" weighted count, after adding 1 more game
    def _calculate_next_weighted_count(self, old_weighted_count):
        return old_weighted_count*0.9 + 1


    # Initialize team_id in self.team_stats
    def _init_cumulative_stats_for_team(self, team_id):
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
        self.team_stats[team_id]['wins_weighted_count'] = 0
        self.team_stats[team_id]['losses_weighted_count'] = 0
        

    # Given game and stats info, convert it into cumulative stats format
    # Will return cumulative stats for (team1, team2)
    # In other words, build "cumulative stats" as if this is the only game these teams have played
    def _parseCumulativeStatsFromData(self, game_info: dict, stats_info: dict) -> Tuple[dict, dict]:
        team1_id, team2_id = getTeamIdsFromGameInfo(db_accessor=self.db_accessor, game_info=game_info)
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
            team1_deaths, team2_deaths = max(team1_info['deaths'], 1), max(team2_info['deaths'], 1)
            return float(team1_kills/team1_deaths), float(team2_kills/team2_deaths)

        def get_avg_assists_per_kill() -> Tuple[float, float]:
            team1_kills, team2_kills = get_team_kills()
            team1_kills = max(team1_kills, 1)
            team2_kills = max(team2_kills, 1)
            team1_assists, team2_assists = team1_info['assists'], max(team2_info['assists'], 1)
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
        
        def get_vision_score_per_minute() -> Tuple[float, float]:
            game_length_minutes = game_info['game_end']['gameTime']/60
            participants = stats_info['stats_update'][-1]['participants']
            team1_total_vision_score = sum([participant['stats']['VISION_SCORE'] for participant in participants[:5]])
            team2_total_vision_score = sum([participant['stats']['VISION_SCORE'] for participant in participants[5:]])
            return team1_total_vision_score/game_length_minutes, team2_total_vision_score/game_length_minutes

        def get_game_time_minutes() -> int:
            return (game_info['game_end']['gameTime'] * 0.001) / 60
            
        def get_gold_diff_per_min() -> Tuple[float, float]:
            stats_at_game_end = next(event for event in stats_info['stats_update'] if event['gameOver'] == True)
            game_length_min = stats_at_game_end['gameTime'] * 0.001 / 60
            team1_gold, team2_gold = stats_at_game_end['teams'][0]['totalGold'], stats_at_game_end['teams'][1]['totalGold']
            team1_avg_gold_diff = (team1_gold - team2_gold) / game_length_min
            return team1_avg_gold_diff, -team1_avg_gold_diff

        def get_gold_diff_at_14() -> Tuple[int, int]:
            stats_at_14 = next(event for event in stats_info['stats_update'] if event['gameTime'] >= 14*60*1000)
            team1_gold, team2_gold = stats_at_14['teams'][0]['totalGold'], stats_at_14['teams'][1]['totalGold']
            team1_gold_diff = team1_gold - team2_gold
            return team1_gold_diff, -team1_gold_diff
            
        
        def getTeamRegions() -> Tuple[str, str]:
            team1_region, team2_region = "region not found", "region not found"
            team1_region_data = self.db_accessor.getDataFromTable(tableName="team_region_mapping", columns=["region"], where_clause=f"id={team1_id}")
            if team1_region_data:
                team1_region = team1_region_data[0][0]
            team2_region_data = self.db_accessor.getDataFromTable(tableName="team_region_mapping", columns=["region"], where_clause=f"id={team2_id}")
            if team2_region_data:
                team2_region = team2_region_data[0][0]
            return team1_region, team2_region
            

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
        addStatsToTeams(key='vision_score_per_minute', values=get_vision_score_per_minute())
        game_time_minutes = get_game_time_minutes()
        if getWinningTeam(game_info=game_info) == 100:
            team1_stats['avg_time_per_win'] = game_time_minutes
            team2_stats['avg_time_per_loss'] = game_time_minutes
            addStatsToTeams(key='overall_winrate', values=(1,0))
        if getWinningTeam(game_info=game_info) == 200:
            team1_stats['avg_time_per_loss'] = game_time_minutes
            team2_stats['avg_time_per_win'] = game_time_minutes
            addStatsToTeams(key='overall_winrate', values=(0, 1))
        addStatsToTeams(key='gold_diff_per_min', values=get_gold_diff_per_min())
        addStatsToTeams(key='gold_diff_at_14', values=get_gold_diff_at_14())
        addStatsToTeams(key='region', values=getTeamRegions())
        
        # Sanity check
        expected_keys = set(CUMULATIVE_STATS_KEYS)
        expected_keys.remove("avg_time_per_win")
        expected_keys.remove("avg_time_per_loss")
        if not expected_keys.issubset(set(team1_stats.keys())) or not expected_keys.issubset(set(team2_stats.keys())):
            error("Error in cumulative_data_builder: while parsing cumulative stats from gamedata, parsed keys don't match CUMULATIVE_STATS_KEYS")

        return team1_stats, team2_stats



    

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
    # ESPORTSTMNT06:2763130
    games = dao.getDataFromTable(tableName="games", 
    columns=["info", "stats_update"],
    where_clause="id='ESPORTSTMNT06:2763130' or id='ESPORTSTMNT03:3083538'")

    for game in games:
        game_info = json.loads(game[0])
        stats_info = json.loads(game[1])
        team1_stats, team2_stats = cumulative_stats_builder.addGamePlayed(game_info=game_info, stats_info=stats_info)
        print("Hello World")

    print("Hello World")