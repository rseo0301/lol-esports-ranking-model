import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, ".."))
from dao.database_accessor import Database_Accessor


team1_id = "99566405123587075"
team2_id = "99566405128626825"
team3_id = "team3_id"

# Team between teams {100: 99566405123587075, 200: 99566405128626825}
game1_data = {
    'info': {
        'game_end': {
            'gameTime': 1536158,
            'winningTeam': 200
        },
        'game_info': {
            'gameName': '103462454882440803|game1',
            'eventTime': '2020-01-31T23:39:59.595Z',
            'eventType': 'game_info',
            'participants': [],
            'platformGameId': 'ESPORTSTMNT01:1291177'
        },
        'champion_kill': [
            {
                'bounty': 400,
                'killer': 1,
                'gameTime': 464979,
                'assistants': [],
                'killerTeamID': 100,
                'killStreakLength': 0
            },
        ],
        'epic_monster_kill': [
            {
                'killer': 7,
                'gameTime': 105246,
                'assistants': [],
                'monsterType': 'redCamp',
                'killerTeamID': 200,
                'inEnemyJungle': False,
            }
        ],
        'building_destroyed': [
            {
                'lane': 'top',
                'teamID': 200,
                'gameTime': 893868,
                'assistants': [],
                'turretTier': 'outer',
                'buildingType': 'turret',
            }
        ],
        'turret_plate_destroyed': [],
        'ward_placed': [],
        'ward_killed': [],
    },
    "stats_update": [
        {
            "teams": [
                {
                    "deaths": 5,
                    "teamID": 100,
                    "assists": 1,
                    "totalGold": 21362,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 1
                },
                {
                    "deaths": 2,
                    "teamID": 200,
                    "assists": 9,
                    "totalGold": 23317,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 1
                }
            ],
            "gameOver": False,
            "gameTime": 840207,
            "participants": [
                {
                    "XP": 6966,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 7.4049601554870605,
                        "MINIONS_KILLED": 116,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 5290
                },
                {
                    "XP": 3735,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 17.15499496459961,
                        "MINIONS_KILLED": 3,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 3713
                },
                {
                    "XP": 6902,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 9.73034954071045,
                        "MINIONS_KILLED": 133,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 5147
                },
                {
                    "XP": 4587,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 14.195404052734377,
                        "MINIONS_KILLED": 110,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4383
                },
                {
                    "XP": 3376,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 10.70949649810791,
                        "MINIONS_KILLED": 21,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 2829
                },
                {
                    "XP": 7101,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 8.08283519744873,
                        "MINIONS_KILLED": 114,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 4686
                },
                {
                    "XP": 4377,
                    "stats": {
                        "ASSISTS": 3,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 7.818757057189941,
                        "MINIONS_KILLED": 4,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 4191
                },
                {
                    "XP": 7288,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 11.95911693572998,
                        "MINIONS_KILLED": 135,
                        "CHAMPIONS_KILLED": 2
                    },
                    "totalGold": 5691
                },
                {
                    "XP": 5073,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 9.060464859008787,
                        "MINIONS_KILLED": 124,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 5358
                },
                {
                    "XP": 4326,
                    "stats": {
                        "ASSISTS": 3,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 15.21505069732666,
                        "MINIONS_KILLED": 18,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 3391
                }
            ]
        },
        {
            "teams": [
                {
                    "deaths": 19,
                    "teamID": 100,
                    "assists": 8,
                    "totalGold": 39272,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 1,
                    "dragonKills": 1
                },
                {
                    "deaths": 5,
                    "teamID": 200,
                    "assists": 45,
                    "totalGold": 50721,
                    "baronKills": 1,
                    "inhibKills": 1,
                    "towerKills": 8,
                    "dragonKills": 3
                }
            ],
            "gameOver": true,
            "gameTime": 1536158,
            "participants": [
                {
                    "XP": 12355,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 11.849115371704102,
                        "MINIONS_KILLED": 219,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 9387
                },
                {
                    "XP": 7605,
                    "stats": {
                        "ASSISTS": 2,
                        "NUM_DEATHS": 6,
                        "VISION_SCORE": 26.31504249572754,
                        "MINIONS_KILLED": 19,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 6370
                },
                {
                    "XP": 11287,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 4,
                        "VISION_SCORE": 24.18935775756836,
                        "MINIONS_KILLED": 205,
                        "CHAMPIONS_KILLED": 2
                    },
                    "totalGold": 9503
                },
                {
                    "XP": 9067,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 39.07364273071289,
                        "MINIONS_KILLED": 205,
                        "CHAMPIONS_KILLED": 2
                    },
                    "totalGold": 8854
                },
                {
                    "XP": 7338,
                    "stats": {
                        "ASSISTS": 3,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 39.696983337402344,
                        "MINIONS_KILLED": 33,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 5158
                },
                {
                    "XP": 14474,
                    "stats": {
                        "ASSISTS": 5,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 27.787368774414062,
                        "MINIONS_KILLED": 200,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 9197
                },
                {
                    "XP": 10137,
                    "stats": {
                        "ASSISTS": 13,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 25.195159912109375,
                        "MINIONS_KILLED": 18,
                        "CHAMPIONS_KILLED": 2
                    },
                    "totalGold": 8558
                },
                {
                    "XP": 15090,
                    "stats": {
                        "ASSISTS": 9,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 27.16229248046875,
                        "MINIONS_KILLED": 232,
                        "CHAMPIONS_KILLED": 6
                    },
                    "totalGold": 12821
                },
                {
                    "XP": 11303,
                    "stats": {
                        "ASSISTS": 3,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 32.62440872192383,
                        "MINIONS_KILLED": 212,
                        "CHAMPIONS_KILLED": 10
                    },
                    "totalGold": 13008
                },
                {
                    "XP": 10475,
                    "stats": {
                        "ASSISTS": 15,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 49.997650146484375,
                        "MINIONS_KILLED": 27,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 7137
                }
            ]
        }
    ]
}


"""
Test these methods:
addGamePlayed
getCumulativeStatsForTeam

"""
