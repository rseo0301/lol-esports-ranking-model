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
team3_id = "team3_id"

# Game between teams {100: 99566405123587075, 200: 99566405128626825}
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

# Game between teams {100: 99566405123587075, 200: 103461966975897718}
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



"""
Test these methods:
addGamePlayed
getCumulativeStatsForTeam

"""
if __name__=="__main__":
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