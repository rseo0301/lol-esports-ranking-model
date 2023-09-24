## Documentation
### League.json
##### Each Object Contains:
| Key               | Type      | Possible Values  |  Relevant? | Notes |
|-------------------|-----------|------------------|------------|-------|
| id                |   String  | Any number as String   |  Yes | Unique identifier |
| name              |   String  | Any  | Yes  | Some names need specifying ie. "2023" |
| slug              |   String  | Any  | Yes  | Unique identifier |
| sport             |   String  | "lol"  | No  | League is the only game being analyzed |
| image             |   String  | any URL to picture  | TBD  | Could be useful for visual component |
| lightImage        |   String  | any URL to picture  | TBD  | Same value as 'Image' if it one doesn't exist |
| darkImage         |   String  | any URL to picture  | TBD  | Same value as 'Image' if it one doesn't exist |
| region            |   String  | See *(1)*  | Yes  | Could be categorized through one-hot method |
| priority          |   Integer | [1, 1000]  | Probably Not, TBD  | Notably, NA = 1, LEC = 3, LCK = 4, LPL = 201 |
| displayPriority   |   Object  | See *(2)*   | No  | Used in some sort of filtering process |
| tournaments       |   Array   | { id: string } | Yes | List of tournaments hosted by league, maps to tournament.json |

*(1) List of Regions*: 
  - NORTH AMERICA
  - BRAZIL
  - KOREA
  - COMMONWEALTH OF INDEPENDENT STATES
  - OCEANIA
  - EMEA
  - JAPAN
  - LATIN AMERICA
  - CHINA
  - HONG KONG, MACAU, TAIWAN
  - VIETNAM
  - LATIN AMERICA NORTH
  - LATIN AMERICA SOUTH

*(2) Display Priority:*
| Key | Type | Possible Values | Relevant? | Notes |
|-----|------|-----------------|-----------|-------|
| position| Integer | 1 to 33 | No | Some values have two leagues attached to them
| status | String | "selected" or "not_selected" | No | Currently, only NA leagues are selected- some sort of filtering already applied |  
### Players.json
##### Each object contains:
|       Key     | Type   |     Possible Values   | Relevant? | Notes                        |
|---------------|--------|-----------------------|-----------|------------------------------|
| player_id     | String | Any number as String  |  Yes      | Unique Identifier            |
| handle        | String | Any                   |  Yes      | Display name                 |
| first_name    | String | Any                   |  TBD      | In case of duplicate handle  |
| last_name     | String | Any                   |  TBD      | In case of duplicate handle  |
| home_team_id  | String | Any number as String  |  Yes      | maps to teams.json           |

Notes: Likely irrelevant for our model, only for visual component. There is a possibility we use the games data to track all of the player's past teams, as well as gather individual data, but it could get very complicated
 
### Teams.json
##### Each object contains:
|     Key     | Type   |     Possible Values      | Relevant? | Notes                        |
|-------------|--------|--------------------------|-----------|------------------------------|
| team_id     | String | Any number as String     |  Yes      | Unique Identifier            |
| name        | String | Any                      |  Yes      | name of team                 |
| acronym     | String | 2/3/4 character acronym  |  TBD      | Could be useful for visual   |
| slug        | String | Any                      |  Yes      | Unique Identifier            |

Notes: Will likely have many features appended to the team's stats. The features could be a team's average stats across our dataset. We may want to weigh games differently, perhaps based on importance, or restrict the stat's timeframe (e.g. last three months) to keep it more relevant to the team's current strength. 

### Tournaments.json
##### Each object contains:
|     Key     | Type   |     Possible Values      | Relevant? | Notes                         |
|-------------|--------|--------------------------|-----------|-------------------------------|
| id          | String | Any number as String     |  Yes      | Unique Identifier             |
| leagueId    | String | Any number as String     |  Yes      | maps to leagues.json          |
| name        | String | Any                      |  Yes      |                               |
| slug        | String | Any                      |  Yes      | Unique Identifier             |
| sport       | String | "lol"                    |  No       | Only working with league data |
| startDate   | String | yyyy-mm-dd               |  Yes      | Could be useful for visual    |
| endDate     | String | yyyy-mm-dd               |  Yes      | Could be useful for visual    |
| stages      | Array  | Object                   |  Yes      | See *(3)*                     |
| rankings    | Array  | Object                   |  TBD      | See *(9)*                     |

*(3) Stages*
|     Key     | Type   |     Possible Values      | Relevant? | Notes                         |
|-------------|--------|--------------------------|-----------|-------------------------------|
| name        | String | Corresponds to slug      |  Yes      |                               |
| type        | String | null                     |  No       | Seems to exist for consistency purposes |
| slug        | String | See *(4)*                |  Yes      | identifier for stage of tournament |
| sections    | Array  | Object                   |  Yes      | See *(5)*                     |

*(4) Slug*
  - groups
  - knockouts
  - regular_season
  - playoffs
  - regional_finals
  - round_1
  - round_2
  - elim
  - promotion
  - play_in_groups
  - play_in_elim
  - promotion_series
  - regional_qualifier
  - bracket_stage
  - play_in_group
  - play_in_knockouts
  - west
    
*(5) Sections*
|     Key     | Type   |     Possible Values      | Relevant? | Notes                         |
|-------------|--------|--------------------------|-----------|-------------------------------|
| name        | String | Any                      |  TBD      | Not too important             |
| matches     | Array  | Object                   |  Yes      | See *(6)*                     |

*(6) Matches*
|     Key     | Type   |     Possible Values      | Relevant? | Notes                         |
|-------------|--------|--------------------------|-----------|-------------------------------|
| id          | String | Any number as String     |  No       | Only individual games matter  |
| type        | String | "normal"                 |  No       | Other possible values not confirmed |
| state       | String | "completed"              |  No       | No unless some games were not completed (TBD) |
| mode        | String | "classic"                |  No       | Other possible values not confirmed |
| Strategy    | Object | {type: "bestOf", count: int} |  TBD  | Not relevant unless putting weight in BO3 |
| teams       | Array  | one object for each team |  No       | See *(7)*                     |
| games       | Array  | object, size of strategy.count |  No | See *(8)*                     |

*(7) Teams*
|     Key     | Type   |     Possible Values      | Relevant? | Notes                         |
|-------------|--------|--------------------------|-----------|-------------------------------|
| id          | String | Any number as String     |  Yes      | Maps to *teams.json*          |
| side        | String | "blue" or "red"          |  TBD      | Could be used, but blue/red advantage inconsistent and often varies by patch |
| record      | Object | {wins: int, losses: int, ties: int} |  TBD/No | current record       |
| result      | Object | {outcome: win/tie/draw, gameWins: int} | TBD | Not as important as individual games |
| players     | Array  | {id: String, role: String} |  Yes      | list of players for team    |

*(8) Games*
|     Key     | Type   |     Possible Values      | Relevant? | Notes                         |
|-------------|--------|--------------------------|-----------|-------------------------------|
| id          | String | Any number as String     |  Yes      | Maps to game data             |
| state       | String | "completed"              |  No       | No unless some games were not completed (TBD) |
| number      | int    | Number in match          |  No       |                               |
| teams       | Array  | One object for each team |  Yes      | Team id, side, and outcome    |

*(9) Rankings*
|     Key     | Type   |     Possible Values      | Relevant? | Notes                         |
|-------------|--------|--------------------------|-----------|-------------------------------|
| ordinal     | int    | 1 to number of teams in tournament |  No |                           |
| teams       | Array  | Objects with team information |  No  | More than 1 in case of ties   |
| result      | null   | null / other values no confirmed     |   No  |                       |
| teams       | Array  | One object for each team |  Yes      | Team id, side, and outcome    |

Notes: Rankings is irrelevant at current state, maybe can be implemented into visual component. Seems to be empty array for bracket play

### Mapping_data.json
##### Each object contains:
- *ESportsGameId*: Unique numerical identifier for the game, referenced in **tournaments.json**
- *PlatformGameId*: Another identifier used to reference the individual game files
  - **unclear** if the combination of letters and numbers hold any significance
- *TeamMapping*: object containing:
  - *200*: Holds Id of first team, **not confirmed** but presumed to be the red team
  - *100*: Holds Id of second team, **not confirmed** but presumed to be the blue team
- ParticipantMapping: object containing:
- Keys from *1 to 10*, holding the player IDs of the 10 players
  - **not confirmed** if the indexing holds any significance










