import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "..", ".."))
import json
from dao.database_accessor import Database_Accessor
from dao.util import getTeamIdsFromGameInfo

dao: Database_Accessor = Database_Accessor(db_host="hackathon-db-2.c880zspfzfsi.us-west-2.rds.amazonaws.com")
team1_id = "99566405123587075"
team2_id = "99566405128626825"
team3_id = "103461966975897718"

# Game between teams {100: 99566405123587075, 200: 99566405128626825}
# team1 and team2
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
            "gameOver": True,
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

# Expected cumulative stats after game 1
game1_expected_cumulative_stats = {
    team1_id: {
        "region": [
            "NORTH AMERICA"
        ],
        "avg_kd_ratio": 0.15384615384615383,
        "barons_per_game": 0.0,
        "gold_diff_at_14": 319.0,
        "overall_winrate": 0.0,
        "avg_time_per_win": 0,
        "dragons_per_game": 0.0,
        "first_blood_rate": 0.0,
        "first_tower_rate": 1.0,
        "heralds_per_game": 0.0,
        "turrets_per_game": 4.0,
        "avg_time_per_loss": 28.155383333333337,
        "gold_diff_per_min": -234.910671316261,
        "avg_assists_per_kill": 2.0,
        "vision_score_per_minute": 0.005620877893580239
    },
    team2_id: {

    },
    team3_id: {

    }
}

# Game between teams {100: 99566405123587075, 200: 103461966975897718}
# team1 and team3
game2_data = {
    'info': {
        "game_end": {
            "gameTime": 1928263,
            "winningTeam": 200
        },
        "game_info": {
            "gameName": "104174601834942039|game1",
            "eventTime": "2020-06-12T19:29:15.778Z",
            "eventType": "game_info",
            "platformGameId": "ESPORTSTMNT01:1403768"
        },
        "champion_kill": [
            {
                "bounty": 400,
                "killer": 8,
                "gameTime": 604273,
                "assistants": [
                    7,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 3,
                "gameTime": 903902,
                "assistants": [
                    2,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 907010,
                "assistants": [
                    6,
                    7,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 914901,
                "assistants": [
                    7,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 927662,
                "assistants": [
                    6,
                    7,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 3
            },
            {
                "bounty": 300,
                "killer": 4,
                "gameTime": 1051280,
                "assistants": [
                    2,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 274,
                "killer": 9,
                "gameTime": 1052105,
                "assistants": [
                    6,
                    7,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1060996,
                "assistants": [
                    7,
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 1075974,
                "assistants": [
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1616629,
                "assistants": [
                    7,
                    8,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1620466,
                "assistants": [
                    8,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1626252,
                "assistants": [
                    7,
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 3
            },
            {
                "bounty": 274,
                "killer": 8,
                "gameTime": 1758998,
                "assistants": [
                    6,
                    7,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 219,
                "killer": 8,
                "gameTime": 1878222,
                "assistants": [
                    7,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 274,
                "killer": 9,
                "gameTime": 1891104,
                "assistants": [
                    7,
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 1894918,
                "assistants": [
                    6,
                    7,
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 1902724,
                "assistants": [
                    6,
                    7,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 3
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1912765,
                "assistants": [
                    7,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 4
            }
        ],
        "epic_monster_kill": [
            {
                "killer": 2,
                "gameTime": 105271,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 106957,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 118230,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 136215,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 138299,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 151283,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 161197,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 175473,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 211206,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 235537,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 252198,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 254476,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 266112,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 296587,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 341999,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 356009,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 371512,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 397784,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 400824,
                "assistants": [
                    4,
                    5
                ],
                "monsterType": "dragon",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 431432,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": True
            },
            {
                "killer": 2,
                "gameTime": 453180,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 454536,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 464713,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 469078,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 498882,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 648147,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 651746,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 662633,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 665741,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 711775,
                "assistants": [
                    10
                ],
                "monsterType": "riftHerald",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 725061,
                "assistants": [
                    3
                ],
                "monsterType": "dragon",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 744563,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 758053,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 773657,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 6,
                "gameTime": 798687,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": True
            },
            {
                "killer": 2,
                "gameTime": 799546,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 803411,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 835204,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 843791,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 848715,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 6,
                "gameTime": 864407,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 883381,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 959035,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 994865,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 995428,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 6,
                "gameTime": 996553,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1104223,
                "assistants": [
                    9
                ],
                "monsterType": "dragon",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1128284,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 4,
                "gameTime": 1129342,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 1135061,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1139525,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1142091,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1148135,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 3,
                "gameTime": 1148267,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 9,
                "gameTime": 1151771,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1160264,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1171930,
                "assistants": [
                    8,
                    9,
                    10
                ],
                "monsterType": "riftHerald",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1181148,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 6,
                "gameTime": 1270303,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 4,
                "gameTime": 1276915,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1288475,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 4,
                "gameTime": 1290230,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1312112,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1355551,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1373369,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 1377007,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 9,
                "gameTime": 1406268,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 1,
                "gameTime": 1416771,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1424671,
                "assistants": [
                    8,
                    9,
                    10
                ],
                "monsterType": "dragon",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1425959,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1438752,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 1504319,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": True
            },
            {
                "killer": 8,
                "gameTime": 1516390,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 4,
                "gameTime": 1516819,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1525421,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 9,
                "gameTime": 1528793,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 6,
                "gameTime": 1531799,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 4,
                "gameTime": 1555198,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 1565872,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1661997,
                "assistants": [
                    8,
                    9,
                    10
                ],
                "monsterType": "baron",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 1,
                "gameTime": 1679841,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1683744,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 1689029,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 8,
                "gameTime": 1809620,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": True
            },
            {
                "killer": 8,
                "gameTime": 1811505,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 7,
                "gameTime": 1812496,
                "assistants": [
                    6,
                    9
                ],
                "monsterType": "dragon",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1821381,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 9,
                "gameTime": 1835988,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 2,
                "gameTime": 1837212,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 6,
                "gameTime": 1839067,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": False
            },
            {
                "killer": 3,
                "gameTime": 1841052,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": False
            },
            {
                "killer": 1,
                "gameTime": 1841448,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": False
            }
        ],
        "building_destroyed": [
            {
                "lane": "bot",
                "teamID": 200,
                "gameTime": 895706,
                "assistants": [
                    4
                ],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 100,
                "gameTime": 954372,
                "assistants": [
                    8,
                    10
                ],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 100,
                "gameTime": 1003834,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "top",
                "teamID": 100,
                "gameTime": 1102536,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 100,
                "gameTime": 1489351,
                "assistants": [
                    6,
                    10
                ],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "top",
                "teamID": 100,
                "gameTime": 1662691,
                "assistants": [],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 100,
                "gameTime": 1718020,
                "assistants": [],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 100,
                "gameTime": 1743833,
                "assistants": [
                    6,
                    7,
                    8
                ],
                "turretTier": "base",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 100,
                "gameTime": 1748029,
                "assistants": [
                    6,
                    7,
                    9,
                    10
                ],
                "turretTier": None,
                "buildingType": "inhibitor"
            },
            {
                "lane": "mid",
                "teamID": 100,
                "gameTime": 1757055,
                "assistants": [
                    9,
                    10
                ],
                "turretTier": "base",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 100,
                "gameTime": 1783056,
                "assistants": [
                    6,
                    7,
                    9,
                    10
                ],
                "turretTier": None,
                "buildingType": "inhibitor"
            },
            {
                "lane": "top",
                "teamID": 100,
                "gameTime": 1883506,
                "assistants": [
                    7,
                    8,
                    10
                ],
                "turretTier": "base",
                "buildingType": "turret"
            },
            {
                "lane": "top",
                "teamID": 100,
                "gameTime": 1915043,
                "assistants": [],
                "turretTier": None,
                "buildingType": "inhibitor"
            },
            {
                "lane": "mid",
                "teamID": 100,
                "gameTime": 1919400,
                "assistants": [
                    8,
                    10
                ],
                "turretTier": "nexus",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 100,
                "gameTime": 1919897,
                "assistants": [
                    6,
                    7,
                    10
                ],
                "turretTier": "nexus",
                "buildingType": "turret"
            }
        ],
    },
    "stats_update": [
        {
            "teams": [
                {
                    "deaths": 1,
                    "teamID": 100,
                    "assists": 0,
                    "totalGold": 19725,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 2
                },
                {
                    "deaths": 0,
                    "teamID": 200,
                    "assists": 2,
                    "totalGold": 21832,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 0
                }
            ],
            "gameOver": False,
            "gameTime": 841015,
            "participants": [
                {
                    "XP": 6082,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 7.770286560058594,
                        "MINIONS_KILLED": 104,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4140
                },
                {
                    "XP": 4009,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 11.47717571258545,
                        "MINIONS_KILLED": 4,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 3760
                },
                {
                    "XP": 6381,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 4.3867716789245605,
                        "MINIONS_KILLED": 109,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4148
                },
                {
                    "XP": 4391,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 6.141035556793213,
                        "MINIONS_KILLED": 115,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4895
                },
                {
                    "XP": 3499,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 13.940760612487791,
                        "MINIONS_KILLED": 19,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 2782
                },
                {
                    "XP": 7177,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 6.945842742919922,
                        "MINIONS_KILLED": 123,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4640
                },
                {
                    "XP": 4455,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 13.353017807006836,
                        "MINIONS_KILLED": 6,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4319
                },
                {
                    "XP": 6452,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 9.104408264160156,
                        "MINIONS_KILLED": 130,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 5498
                },
                {
                    "XP": 4739,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 10.566888809204102,
                        "MINIONS_KILLED": 119,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4603
                },
                {
                    "XP": 3461,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 10.697073936462402,
                        "MINIONS_KILLED": 3,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 2772
                }
            ]
        },
        {
            "teams": [
                {
                    "deaths": 16,
                    "teamID": 100,
                    "assists": 6,
                    "totalGold": 47763,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 1,
                    "dragonKills": 2
                },
                {
                    "deaths": 2,
                    "teamID": 200,
                    "assists": 49,
                    "totalGold": 61848,
                    "baronKills": 1,
                    "inhibKills": 3,
                    "towerKills": 11,
                    "dragonKills": 3
                }
            ],
            "gameOver": True,
            "gameTime": 1928263,
            "participants": [
                {
                    "XP": 15221,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 28.790931701660156,
                        "MINIONS_KILLED": 249,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 10293
                },
                {
                    "XP": 9262,
                    "stats": {
                        "ASSISTS": 2,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 33.675655364990234,
                        "MINIONS_KILLED": 20,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 7830
                },
                {
                    "XP": 14216,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 23.48464584350586,
                        "MINIONS_KILLED": 238,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 10177
                },
                {
                    "XP": 13393,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 4,
                        "VISION_SCORE": 19.297863006591797,
                        "MINIONS_KILLED": 299,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 13226
                },
                {
                    "XP": 8348,
                    "stats": {
                        "ASSISTS": 2,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 75.78276062011719,
                        "MINIONS_KILLED": 35,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 6237
                },
                {
                    "XP": 17795,
                    "stats": {
                        "ASSISTS": 6,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 21.634321212768555,
                        "MINIONS_KILLED": 249,
                        "CHAMPIONS_KILLED": 5
                    },
                    "totalGold": 13663
                },
                {
                    "XP": 12121,
                    "stats": {
                        "ASSISTS": 14,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 56.5147705078125,
                        "MINIONS_KILLED": 38,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 10471
                },
                {
                    "XP": 17539,
                    "stats": {
                        "ASSISTS": 6,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 42.196250915527344,
                        "MINIONS_KILLED": 279,
                        "CHAMPIONS_KILLED": 6
                    },
                    "totalGold": 15767
                },
                {
                    "XP": 15543,
                    "stats": {
                        "ASSISTS": 7,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 43.16498947143555,
                        "MINIONS_KILLED": 277,
                        "CHAMPIONS_KILLED": 4
                    },
                    "totalGold": 14326
                },
                {
                    "XP": 10207,
                    "stats": {
                        "ASSISTS": 16,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 72.38910675048828,
                        "MINIONS_KILLED": 8,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 7621
                }
            ]
        }
    ]
}

# Game between teams {100: 99566405123587075, 200: 99566405128626825}
# team1 and team2
game3_data = {
    'info': {
        "game_end": {
            "gameTime": 2105275,
            "winningTeam": 100
        },
        "game_info": {
            "gameName": "106273298443342402|game1",
            "eventTime": "2021-06-30T20:12:57.705Z",
            "eventType": "game_info",
            "participants": [
                {
                    "teamID": 100,
                    "championName": "Viego",
                    "summonerName": "100 Tenacity",
                    "participantID": 1
                },
                {
                    "teamID": 100,
                    "championName": "Diana",
                    "summonerName": "100 Kenvi",
                    "participantID": 2
                },
                {
                    "teamID": 100,
                    "championName": "Lucian",
                    "summonerName": "100 ry0ma",
                    "participantID": 3
                },
                {
                    "teamID": 100,
                    "championName": "Jinx",
                    "summonerName": "100 Luger",
                    "participantID": 4
                },
                {
                    "teamID": 100,
                    "championName": "Braum",
                    "summonerName": "100 Poome",
                    "participantID": 5
                },
                {
                    "teamID": 200,
                    "championName": "MonkeyKing",
                    "summonerName": "CLG Thien",
                    "participantID": 6
                },
                {
                    "teamID": 200,
                    "championName": "Volibear",
                    "summonerName": "CLG Keel",
                    "participantID": 7
                },
                {
                    "teamID": 200,
                    "championName": "Viktor",
                    "summonerName": "CLG rjs",
                    "participantID": 8
                },
                {
                    "teamID": 200,
                    "championName": "Ziggs",
                    "summonerName": "CLG Katsurii",
                    "participantID": 9
                },
                {
                    "teamID": 200,
                    "championName": "Nautilus",
                    "summonerName": "CLG Hooks",
                    "participantID": 10
                }
            ],
            "platformGameId": "ESPORTSTMNT01:2131752"
        },
        "champion_kill": [
            {
                "bounty": 400,
                "killer": 5,
                "gameTime": 749904,
                "assistants": [
                    2,
                    3,
                    4
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 888135,
                "assistants": [
                    7,
                    8,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 890480,
                "assistants": [
                    2,
                    3,
                    4
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 4,
                "gameTime": 892925,
                "assistants": [
                    2,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 3,
                "gameTime": 1010606,
                "assistants": [
                    1,
                    2
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 1129319,
                "assistants": [
                    8,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 3,
                "gameTime": 1130643,
                "assistants": [
                    1,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 1130775,
                "assistants": [
                    7,
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 1131570,
                "assistants": [
                    7,
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 4,
                "gameTime": 1444591,
                "assistants": [
                    1,
                    2,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 3,
                "gameTime": 1446511,
                "assistants": [
                    2,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1479875,
                "assistants": [],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1539770,
                "assistants": [
                    4
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 274,
                "killer": 3,
                "gameTime": 1567942,
                "assistants": [
                    1,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 1576519,
                "assistants": [
                    4
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1576619,
                "assistants": [
                    8
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 1579334,
                "assistants": [
                    7,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1580194,
                "assistants": [
                    3,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 274,
                "killer": 1,
                "gameTime": 1652741,
                "assistants": [
                    2,
                    3,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 219,
                "killer": 3,
                "gameTime": 1812434,
                "assistants": [
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 1817359,
                "assistants": [
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 4,
                "gameTime": 1826159,
                "assistants": [
                    1,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 1826389,
                "assistants": [
                    9
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 1878864,
                "assistants": [
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 2030082,
                "assistants": [
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 2051705,
                "assistants": [
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 2072769,
                "assistants": [
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 274,
                "killer": 2,
                "gameTime": 2080311,
                "assistants": [
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 2
            },
            {
                "bounty": 274,
                "killer": 4,
                "gameTime": 2080477,
                "assistants": [
                    1,
                    2,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 2082958,
                "assistants": [],
                "killerTeamID": 100,
                "killStreakLength": 3
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 2095095,
                "assistants": [],
                "killerTeamID": 100,
                "killStreakLength": 4
            }
        ],
        "epic_monster_kill": [
            {
                "killer": 7,
                "gameTime": 108647,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 114637,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 119332,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 123996,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 137500,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 150730,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 154963,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 172594,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 181687,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 195450,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 205797,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 212281,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 227453,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 231424,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 274143,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 286182,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 299573,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 303510,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 324653,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 343013,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 379609,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 383315,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 414510,
                "assistants": [
                    3,
                    4,
                    5
                ],
                "monsterType": "dragon",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 438567,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 1,
                "gameTime": 442072,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 454507,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 454738,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 488384,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 494240,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 518398,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 525873,
                "assistants": [
                    1
                ],
                "monsterType": "riftHerald",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 538811,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 542907,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 549991,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 550354,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 560662,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 605578,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 613452,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 637820,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 640825,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 688951,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 695299,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 705019,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 707437,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 761943,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 2,
                "gameTime": 783541,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 799220,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 818445,
                "assistants": [],
                "monsterType": "dragon",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 826973,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 836591,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 842509,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 852497,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 857326,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 866859,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": true
            },
            {
                "killer": 2,
                "gameTime": 871227,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 917053,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 925155,
                "assistants": [],
                "monsterType": "riftHerald",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 938229,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 948259,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 957517,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 983978,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1002072,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1034850,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1044243,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 8,
                "gameTime": 1070643,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1075012,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 1080440,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1088143,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1092184,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 8,
                "gameTime": 1140870,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 8,
                "gameTime": 1155295,
                "assistants": [
                    6,
                    9,
                    10
                ],
                "monsterType": "dragon",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 1157644,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 1165183,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 7,
                "gameTime": 1187773,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1188402,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1199484,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1201699,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 6,
                "gameTime": 1224828,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1250670,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1260489,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 6,
                "gameTime": 1270421,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 1282957,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1294273,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1318370,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1327709,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1333195,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1348513,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 6,
                "gameTime": 1380181,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 6,
                "gameTime": 1390871,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1396992,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1506321,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1513532,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 9,
                "gameTime": 1516280,
                "assistants": [
                    7,
                    8
                ],
                "monsterType": "dragon",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1519257,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 1524321,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 1533053,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 6,
                "gameTime": 1541986,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1558044,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 8,
                "gameTime": 1586579,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 8,
                "gameTime": 1601668,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1614139,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1650294,
                "assistants": [
                    1,
                    3,
                    4,
                    5,
                    9
                ],
                "monsterType": "baron",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 1666347,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1669324,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 1686007,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1686901,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1696228,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1696693,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 1,
                "gameTime": 1706552,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1736860,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1743049,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 1760481,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 1782067,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 1859709,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 1863581,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 3,
                "gameTime": 1866558,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 1872247,
                "assistants": [],
                "monsterType": "dragon",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 1879626,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 9,
                "gameTime": 1889582,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1900889,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1907075,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 1911877,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1913599,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1931227,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 2009246,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 2020253,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 2021908,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 4,
                "gameTime": 2028924,
                "assistants": [
                    2,
                    5,
                    7,
                    8,
                    9
                ],
                "monsterType": "baron",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 2032535,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 4,
                "gameTime": 2067054,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            }
        ],
        "building_destroyed": [
            {
                "lane": "bot",
                "teamID": 200,
                "gameTime": 833880,
                "assistants": [
                    5
                ],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "top",
                "teamID": 200,
                "gameTime": 1026617,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1188732,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 200,
                "gameTime": 1788950,
                "assistants": [],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1832472,
                "assistants": [
                    4,
                    5
                ],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1841794,
                "assistants": [
                    1,
                    3
                ],
                "turretTier": "base",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1848634,
                "assistants": [
                    3,
                    5
                ],
                "turretTier": null,
                "buildingType": "inhibitor"
            },
            {
                "lane": "top",
                "teamID": 200,
                "gameTime": 1940219,
                "assistants": [],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 2091289,
                "assistants": [],
                "turretTier": "nexus",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 2097244,
                "assistants": [
                    1,
                    2,
                    4
                ],
                "turretTier": "nexus",
                "buildingType": "turret"
            }
        ],
    },
    "stats_update": [
        {
            "teams": [
                {
                    "deaths": 0,
                    "teamID": 100,
                    "assists": 3,
                    "totalGold": 23961,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 1,
                    "dragonKills": 2
                },
                {
                    "deaths": 1,
                    "teamID": 200,
                    "assists": 0,
                    "totalGold": 20930,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 0
                }
            ],
            "gameOver": false,
            "gameTime": 840786,
            "participants": [
                {
                    "XP": 6931,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 11.09061050415039,
                        "MINIONS_KILLED": 121,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4780
                },
                {
                    "XP": 5856,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 13.046119689941406,
                        "MINIONS_KILLED": 3,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 5049
                },
                {
                    "XP": 7599,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 11.966157913208008,
                        "MINIONS_KILLED": 138,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 5203
                },
                {
                    "XP": 5609,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 12.950394630432127,
                        "MINIONS_KILLED": 135,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 5407
                },
                {
                    "XP": 3137,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 16.516870498657227,
                        "MINIONS_KILLED": 21,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 3522
                },
                {
                    "XP": 7169,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 9.251444816589355,
                        "MINIONS_KILLED": 135,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4976
                },
                {
                    "XP": 4438,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 11.75104808807373,
                        "MINIONS_KILLED": 5,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4022
                },
                {
                    "XP": 7223,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 11.25966739654541,
                        "MINIONS_KILLED": 128,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4578
                },
                {
                    "XP": 4574,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 9.610260009765623,
                        "MINIONS_KILLED": 115,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4407
                },
                {
                    "XP": 3004,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 17.958436965942383,
                        "MINIONS_KILLED": 21,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 2947
                }
            ]
        },
        {
            "teams": [
                {
                    "deaths": 10,
                    "teamID": 100,
                    "assists": 48,
                    "totalGold": 72179,
                    "baronKills": 2,
                    "inhibKills": 1,
                    "towerKills": 8,
                    "dragonKills": 3
                },
                {
                    "deaths": 21,
                    "teamID": 200,
                    "assists": 20,
                    "totalGold": 55774,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 2
                }
            ],
            "gameOver": true,
            "gameTime": 2105275,
            "participants": [
                {
                    "XP": 19336,
                    "stats": {
                        "ASSISTS": 6,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 41.96663284301758,
                        "MINIONS_KILLED": 258,
                        "CHAMPIONS_KILLED": 4
                    },
                    "totalGold": 14853
                },
                {
                    "XP": 18502,
                    "stats": {
                        "ASSISTS": 8,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 49.796722412109375,
                        "MINIONS_KILLED": 32,
                        "CHAMPIONS_KILLED": 7
                    },
                    "totalGold": 14823
                },
                {
                    "XP": 20194,
                    "stats": {
                        "ASSISTS": 8,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 67.88123321533203,
                        "MINIONS_KILLED": 304,
                        "CHAMPIONS_KILLED": 5
                    },
                    "totalGold": 16004
                },
                {
                    "XP": 19415,
                    "stats": {
                        "ASSISTS": 12,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 66.1397476196289,
                        "MINIONS_KILLED": 346,
                        "CHAMPIONS_KILLED": 4
                    },
                    "totalGold": 17345
                },
                {
                    "XP": 13578,
                    "stats": {
                        "ASSISTS": 14,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 89.03742980957031,
                        "MINIONS_KILLED": 32,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 9154
                },
                {
                    "XP": 16394,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 35.3630256652832,
                        "MINIONS_KILLED": 269,
                        "CHAMPIONS_KILLED": 3
                    },
                    "totalGold": 13128
                },
                {
                    "XP": 12552,
                    "stats": {
                        "ASSISTS": 4,
                        "NUM_DEATHS": 6,
                        "VISION_SCORE": 39.94133377075195,
                        "MINIONS_KILLED": 13,
                        "CHAMPIONS_KILLED": 2
                    },
                    "totalGold": 9511
                },
                {
                    "XP": 19043,
                    "stats": {
                        "ASSISTS": 5,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 51.022335052490234,
                        "MINIONS_KILLED": 302,
                        "CHAMPIONS_KILLED": 4
                    },
                    "totalGold": 13759
                },
                {
                    "XP": 15840,
                    "stats": {
                        "ASSISTS": 4,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 50.18354415893555,
                        "MINIONS_KILLED": 310,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 12478
                },
                {
                    "XP": 9896,
                    "stats": {
                        "ASSISTS": 7,
                        "NUM_DEATHS": 6,
                        "VISION_SCORE": 84.13357543945312,
                        "MINIONS_KILLED": 31,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 6898
                }
            ]
        }
    ]
}

# Game between teams {100: 99566405128626825, 200: 99566405123587075}
# team2 and tea1
game4_data = {
    'info': {
        "game_end": {
            "gameTime": 1677716,
            "winningTeam": 100
        },
        "game_info": {
            "gameName": "106273298443342402|game2",
            "eventTime": "2021-06-30T21:12:24.922Z",
            "eventType": "game_info",
            "participants": [
                {
                    "teamID": 100,
                    "championName": "DrMundo",
                    "summonerName": "100 Tenacity",
                    "participantID": 1
                },
                {
                    "teamID": 100,
                    "championName": "Kindred",
                    "summonerName": "100 Kenvi",
                    "participantID": 2
                },
                {
                    "teamID": 100,
                    "championName": "Lulu",
                    "summonerName": "100 ry0ma",
                    "participantID": 3
                },
                {
                    "teamID": 100,
                    "championName": "Varus",
                    "summonerName": "100 Luger",
                    "participantID": 4
                },
                {
                    "teamID": 100,
                    "championName": "Braum",
                    "summonerName": "100 Poome",
                    "participantID": 5
                },
                {
                    "teamID": 200,
                    "championName": "LeeSin",
                    "summonerName": "CLG Thien",
                    "participantID": 6
                },
                {
                    "teamID": 200,
                    "championName": "Gragas",
                    "summonerName": "CLG Keel",
                    "participantID": 7
                },
                {
                    "teamID": 200,
                    "championName": "Vladimir",
                    "summonerName": "CLG rjs",
                    "participantID": 8
                },
                {
                    "teamID": 200,
                    "championName": "Aphelios",
                    "summonerName": "CLG Katsurii",
                    "participantID": 9
                },
                {
                    "teamID": 200,
                    "championName": "Nautilus",
                    "summonerName": "CLG Hooks",
                    "participantID": 10
                }
            ],
            "platformGameId": "ESPORTSTMNT01:2131800"
        },
        "champion_kill": [
            {
                "bounty": 400,
                "killer": 1,
                "gameTime": 214203,
                "assistants": [],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 317464,
                "assistants": [
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 3,
                "gameTime": 340691,
                "assistants": [],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 10,
                "gameTime": 465746,
                "assistants": [
                    6,
                    7,
                    8
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 490560,
                "assistants": [
                    6,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 716578,
                "assistants": [
                    7
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 739798,
                "assistants": [
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 741321,
                "assistants": [
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 743074,
                "assistants": [
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 750520,
                "assistants": [
                    9
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 761402,
                "assistants": [
                    6
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 817469,
                "assistants": [],
                "killerTeamID": 200,
                "killStreakLength": 3
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 819390,
                "assistants": [
                    1
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 824852,
                "assistants": [
                    1
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 274,
                "killer": 6,
                "gameTime": 829152,
                "assistants": [],
                "killerTeamID": 200,
                "killStreakLength": 4
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 833384,
                "assistants": [
                    9,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 865741,
                "assistants": [],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1009458,
                "assistants": [
                    1,
                    3,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 1018063,
                "assistants": [
                    7,
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 274,
                "killer": 9,
                "gameTime": 1018659,
                "assistants": [
                    7,
                    8,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 4,
                "gameTime": 1021314,
                "assistants": [
                    1,
                    2,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 1022043,
                "assistants": [
                    7,
                    8
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 1024426,
                "assistants": [
                    8,
                    9
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 1028096,
                "assistants": [
                    2,
                    3,
                    4
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 1053620,
                "assistants": [],
                "killerTeamID": 100,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 7,
                "gameTime": 1057562,
                "assistants": [
                    6,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1097032,
                "assistants": [
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 3,
                "gameTime": 1099946,
                "assistants": [
                    2,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1158051,
                "assistants": [],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1161560,
                "assistants": [
                    7,
                    10
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1169630,
                "assistants": [],
                "killerTeamID": 200,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 1292083,
                "assistants": [
                    2,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1296582,
                "assistants": [
                    1,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1303072,
                "assistants": [
                    1,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 274,
                "killer": 2,
                "gameTime": 1443050,
                "assistants": [
                    1,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 4,
                "gameTime": 1450296,
                "assistants": [
                    1,
                    2,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 274,
                "killer": 2,
                "gameTime": 1475742,
                "assistants": [
                    3,
                    4
                ],
                "killerTeamID": 100,
                "killStreakLength": 3
            },
            {
                "bounty": 274,
                "killer": 4,
                "gameTime": 1479247,
                "assistants": [
                    1,
                    2,
                    3
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 6,
                "gameTime": 1479711,
                "assistants": [
                    7,
                    8
                ],
                "killerTeamID": 200,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 10,
                "gameTime": 1481043,
                "assistants": [
                    6,
                    7
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 4,
                "gameTime": 1487429,
                "assistants": [
                    1,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 1,
                "gameTime": 1490378,
                "assistants": [
                    2,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 1508125,
                "assistants": [],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 8,
                "gameTime": 1532270,
                "assistants": [],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1630709,
                "assistants": [
                    1,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1638453,
                "assistants": [
                    1,
                    3,
                    4,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 1
            },
            {
                "bounty": 300,
                "killer": 5,
                "gameTime": 1638784,
                "assistants": [
                    1,
                    2,
                    3,
                    4
                ],
                "killerTeamID": 100,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 2,
                "gameTime": 1640271,
                "assistants": [
                    1,
                    3,
                    5
                ],
                "killerTeamID": 100,
                "killStreakLength": 2
            },
            {
                "bounty": 300,
                "killer": 9,
                "gameTime": 1640370,
                "assistants": [
                    6,
                    7,
                    8
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 10,
                "gameTime": 1641230,
                "assistants": [
                    7,
                    9
                ],
                "killerTeamID": 200,
                "killStreakLength": 0
            },
            {
                "bounty": 300,
                "killer": 10,
                "gameTime": 1650685,
                "assistants": [],
                "killerTeamID": 200,
                "killStreakLength": 1
            }
        ],
        "epic_monster_kill": [
            {
                "killer": 2,
                "gameTime": 111523,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 7,
                "gameTime": 112713,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 118401,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 155711,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 181725,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 202964,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 220418,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 230245,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 236206,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 253249,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": true
            },
            {
                "killer": 2,
                "gameTime": 267914,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 279858,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 293512,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 336189,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 373623,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 382225,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 393175,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 431232,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 456815,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 495292,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 7,
                "gameTime": 506871,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 555368,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 555996,
                "assistants": [
                    1
                ],
                "monsterType": "riftHerald",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 562586,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 578075,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 578704,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 580790,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 592183,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 598707,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 627024,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 631023,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 678473,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 698080,
                "assistants": [
                    4,
                    5
                ],
                "monsterType": "dragon",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 715553,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 722335,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 785219,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 799668,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 803239,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 808468,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 847471,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 901349,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 923400,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 928957,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 9,
                "gameTime": 935776,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 936601,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 937529,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 955692,
                "assistants": [
                    5
                ],
                "monsterType": "riftHerald",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 971565,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 971664,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 983118,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1070600,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1085716,
                "assistants": [
                    2,
                    3,
                    4,
                    5,
                    8,
                    8
                ],
                "monsterType": "dragon",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1115961,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1121919,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1134792,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1138694,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": true
            },
            {
                "killer": 2,
                "gameTime": 1145149,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1221001,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1225836,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1236815,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1237080,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1243598,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1264278,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1289998,
                "assistants": [
                    1,
                    4,
                    5,
                    9
                ],
                "monsterType": "baron",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 9,
                "gameTime": 1307338,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 6,
                "gameTime": 1318879,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 9,
                "gameTime": 1319342,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 1331418,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 3,
                "gameTime": 1366829,
                "assistants": [],
                "monsterType": "blueCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1367193,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1391883,
                "assistants": [
                    3
                ],
                "monsterType": "dragon",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1394068,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1408037,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 1524730,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 1,
                "gameTime": 1537064,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 9,
                "gameTime": 1541464,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 7,
                "gameTime": 1542092,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1542949,
                "assistants": [],
                "monsterType": "redCamp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1546422,
                "assistants": [],
                "monsterType": "raptor",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1555848,
                "assistants": [],
                "monsterType": "wolf",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1560808,
                "assistants": [],
                "monsterType": "gromp",
                "killerTeamID": 100,
                "inEnemyJungle": false
            },
            {
                "killer": 8,
                "gameTime": 1563288,
                "assistants": [],
                "monsterType": "krug",
                "killerTeamID": 200,
                "inEnemyJungle": false
            },
            {
                "killer": 2,
                "gameTime": 1574985,
                "assistants": [],
                "monsterType": "scuttleCrab",
                "killerTeamID": 100,
                "inEnemyJungle": false
            }
        ],
        "building_destroyed": [
            {
                "lane": "top",
                "teamID": 200,
                "gameTime": 856602,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 910982,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 100,
                "gameTime": 956222,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 200,
                "gameTime": 1144852,
                "assistants": [],
                "turretTier": "outer",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1323414,
                "assistants": [
                    2,
                    3
                ],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1334598,
                "assistants": [
                    3,
                    4,
                    5
                ],
                "turretTier": "base",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 200,
                "gameTime": 1420567,
                "assistants": [
                    1,
                    3
                ],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 200,
                "gameTime": 1447581,
                "assistants": [
                    3,
                    5
                ],
                "turretTier": "base",
                "buildingType": "turret"
            },
            {
                "lane": "bot",
                "teamID": 200,
                "gameTime": 1463636,
                "assistants": [
                    1,
                    3,
                    5
                ],
                "turretTier": null,
                "buildingType": "inhibitor"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1468668,
                "assistants": [
                    2,
                    3,
                    4
                ],
                "turretTier": null,
                "buildingType": "inhibitor"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1496012,
                "assistants": [
                    4,
                    5
                ],
                "turretTier": "nexus",
                "buildingType": "turret"
            },
            {
                "lane": "top",
                "teamID": 200,
                "gameTime": 1605584,
                "assistants": [
                    3
                ],
                "turretTier": "inner",
                "buildingType": "turret"
            },
            {
                "lane": "top",
                "teamID": 200,
                "gameTime": 1623818,
                "assistants": [
                    1,
                    3,
                    5
                ],
                "turretTier": "base",
                "buildingType": "turret"
            },
            {
                "lane": "mid",
                "teamID": 200,
                "gameTime": 1640569,
                "assistants": [
                    2,
                    3,
                    5
                ],
                "turretTier": "nexus",
                "buildingType": "turret"
            },
            {
                "lane": "top",
                "teamID": 200,
                "gameTime": 1667412,
                "assistants": [],
                "turretTier": null,
                "buildingType": "inhibitor"
            }
        ],
    },
    "stats_update": [
        {
            "teams": [
                {
                    "deaths": 10,
                    "teamID": 100,
                    "assists": 6,
                    "totalGold": 24120,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 1
                },
                {
                    "deaths": 6,
                    "teamID": 200,
                    "assists": 13,
                    "totalGold": 23584,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 0,
                    "dragonKills": 0
                }
            ],
            "gameOver": false,
            "gameTime": 840726,
            "participants": [
                {
                    "XP": 6887,
                    "stats": {
                        "ASSISTS": 2,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 8.462809562683105,
                        "MINIONS_KILLED": 114,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 5792
                },
                {
                    "XP": 5642,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 25.77021598815918,
                        "MINIONS_KILLED": 11,
                        "CHAMPIONS_KILLED": 4
                    },
                    "totalGold": 5873
                },
                {
                    "XP": 7014,
                    "stats": {
                        "ASSISTS": 0,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 6.104644775390625,
                        "MINIONS_KILLED": 108,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 4948
                },
                {
                    "XP": 4914,
                    "stats": {
                        "ASSISTS": 2,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 6.063873291015625,
                        "MINIONS_KILLED": 113,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4509
                },
                {
                    "XP": 3164,
                    "stats": {
                        "ASSISTS": 2,
                        "NUM_DEATHS": 3,
                        "VISION_SCORE": 12.759075164794922,
                        "MINIONS_KILLED": 18,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 2998
                },
                {
                    "XP": 7362,
                    "stats": {
                        "ASSISTS": 3,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 7.399072170257568,
                        "MINIONS_KILLED": 101,
                        "CHAMPIONS_KILLED": 5
                    },
                    "totalGold": 6321
                },
                {
                    "XP": 5094,
                    "stats": {
                        "ASSISTS": 2,
                        "NUM_DEATHS": 0,
                        "VISION_SCORE": 7.861560344696045,
                        "MINIONS_KILLED": 5,
                        "CHAMPIONS_KILLED": 3
                    },
                    "totalGold": 4920
                },
                {
                    "XP": 6085,
                    "stats": {
                        "ASSISTS": 1,
                        "NUM_DEATHS": 1,
                        "VISION_SCORE": 11.606928825378418,
                        "MINIONS_KILLED": 104,
                        "CHAMPIONS_KILLED": 0
                    },
                    "totalGold": 4059
                },
                {
                    "XP": 5617,
                    "stats": {
                        "ASSISTS": 3,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 7.83736515045166,
                        "MINIONS_KILLED": 106,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 4921
                },
                {
                    "XP": 3228,
                    "stats": {
                        "ASSISTS": 4,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 10.835750579833984,
                        "MINIONS_KILLED": 19,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 3363
                }
            ]
        },
        {
            "teams": [
                {
                    "deaths": 24,
                    "teamID": 100,
                    "assists": 61,
                    "totalGold": 59991,
                    "baronKills": 1,
                    "inhibKills": 2,
                    "towerKills": 11,
                    "dragonKills": 2
                },
                {
                    "deaths": 27,
                    "teamID": 200,
                    "assists": 36,
                    "totalGold": 49892,
                    "baronKills": 0,
                    "inhibKills": 0,
                    "towerKills": 1,
                    "dragonKills": 1
                }
            ],
            "gameOver": true,
            "gameTime": 1677716,
            "participants": [
                {
                    "XP": 16609,
                    "stats": {
                        "ASSISTS": 14,
                        "NUM_DEATHS": 2,
                        "VISION_SCORE": 19.43981170654297,
                        "MINIONS_KILLED": 211,
                        "CHAMPIONS_KILLED": 6
                    },
                    "totalGold": 14842
                },
                {
                    "XP": 15115,
                    "stats": {
                        "ASSISTS": 8,
                        "NUM_DEATHS": 7,
                        "VISION_SCORE": 88.2555160522461,
                        "MINIONS_KILLED": 67,
                        "CHAMPIONS_KILLED": 14
                    },
                    "totalGold": 16216
                },
                {
                    "XP": 13793,
                    "stats": {
                        "ASSISTS": 12,
                        "NUM_DEATHS": 4,
                        "VISION_SCORE": 21.582338333129883,
                        "MINIONS_KILLED": 148,
                        "CHAMPIONS_KILLED": 2
                    },
                    "totalGold": 10098
                },
                {
                    "XP": 12279,
                    "stats": {
                        "ASSISTS": 11,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 30.795351028442383,
                        "MINIONS_KILLED": 209,
                        "CHAMPIONS_KILLED": 4
                    },
                    "totalGold": 11339
                },
                {
                    "XP": 10144,
                    "stats": {
                        "ASSISTS": 16,
                        "NUM_DEATHS": 6,
                        "VISION_SCORE": 64.43998718261719,
                        "MINIONS_KILLED": 27,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 7496
                },
                {
                    "XP": 14378,
                    "stats": {
                        "ASSISTS": 6,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 21.74927520751953,
                        "MINIONS_KILLED": 192,
                        "CHAMPIONS_KILLED": 8
                    },
                    "totalGold": 12493
                },
                {
                    "XP": 11219,
                    "stats": {
                        "ASSISTS": 10,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 35.75667953491211,
                        "MINIONS_KILLED": 24,
                        "CHAMPIONS_KILLED": 5
                    },
                    "totalGold": 9376
                },
                {
                    "XP": 12307,
                    "stats": {
                        "ASSISTS": 7,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 26.07009506225586,
                        "MINIONS_KILLED": 184,
                        "CHAMPIONS_KILLED": 1
                    },
                    "totalGold": 8903
                },
                {
                    "XP": 13860,
                    "stats": {
                        "ASSISTS": 5,
                        "NUM_DEATHS": 5,
                        "VISION_SCORE": 24.666725158691406,
                        "MINIONS_KILLED": 235,
                        "CHAMPIONS_KILLED": 6
                    },
                    "totalGold": 11792
                },
                {
                    "XP": 9749,
                    "stats": {
                        "ASSISTS": 8,
                        "NUM_DEATHS": 7,
                        "VISION_SCORE": 49.59792709350586,
                        "MINIONS_KILLED": 35,
                        "CHAMPIONS_KILLED": 4
                    },
                    "totalGold": 7328
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
if __name__=="__main__":
    # This chunk of code is used for finding example games to use in testing
    nGames = 0
    while True:
        games_data = dao.getDataFromTable(tableName="games", columns=["info", "stats_update"], limit = 10, offset=nGames)
        if len(games_data) == 0:
            break
        nGames += len(games_data)
        for game_data in games_data:
            info = json.loads(game_data[0])
            stats = json.loads(game_data[1])
            t1_id, t2_id = getTeamIdsFromGameInfo(db_accessor=dao, game_info=info)
            if (t1_id == team1_id and t2_id == team2_id) or (t1_id == team2_id and t2_id == team1_id):
                print(f"Same matchup {info['game_info']['platformGameId']}")
            if t1_id == team1_id:
                print(f"Team 1 id is the same {info['game_info']['platformGameId']}")

    # This is the actual testing
