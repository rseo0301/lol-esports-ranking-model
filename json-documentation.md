## Documentation
### League.json
##### Each Object Contains:
| Key               | Type             | Possible Values  |  Relevant? | Notes |
|-------------------|------------------|------------------|------------|-------|
| id                |    String        | Any number as String   |  Yes | Unique identifier |
| name              |    String        | Any  | Yes  | Some names need specifying ie. "2023" |
| slug              |    String        | Any  | Yes  | Unique identifier |
| sport             |    String        | "lol"  | No  | League is the only game being analyzed |
| image             |    String        | any URL to picture  | TBD  | Could be useful for visual component |
| lightImage        |    String        | any URL to picture  | TBD  | Same value as 'Image' if it one doesn't exist |
| darkImage         |    String        | any URL to picture  | TBD  | Same value as 'Image' if it one doesn't exist |
| region            |    String        | See *(1)*  | Yes  | Could be categorized through one-hot method |
| priority          |    Integer       | [1, 1000]  | Probably Not, TBD  | Notably, NA = 1, LEC = 3, LCK = 4, LPL = 201 |
| displayPriority  |    Object        | See *(2)*   | No  | Used in some sort of filtering process |
| tournaments       |    Array         | { id: string } | Yes | List of tournaments hosted by league, maps to tournament.json |

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
- *Id*: A unique numerical identifier for the tournament
- *LeagueId*: A unique numerical identifier for the league that the tournament is hosted in
  - **maps to id in leagues.json**
- *Name*: Name of the tournament
- *Slug*: Unique named identifier for the tournament
- *Sport*: Name of game title, exclusive to "lol" in this dataset.
- *StartDate*: Start date of the tournament
- *EndDate*: End date of the tournament
- *Stages*: an array of objects, where each object contains:
  - *Name*: Name of stage in tournament
  - *Type*: **unclear**, all values null
  - *Slug*: Identifier for the stage of tournament
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
  - *Sections*: An array of objects, where each object contains:
    - *Name*: Specific name of group within stage, ie. "Group A"
    - *Matches*: An array of matches played in the section. Each match contains:
      - *ID*: Unique numerical identifier for the match
      - *Type*: **unclear**, might be "normal" for all values?
      - *Mode*: **unclear**, might be "classic for all values, may be for cases in special events (ie. URF)
      - *Strategy*: object containing:
        - *Type*: **unclear**, seems to be "bestOf" for all values
        - *Count*: Corresponds to the max number of games to be played in the match, ie. "Best Of 5"
      - *Teams*: array of size 2, each object containing:
        - *Id*: Unique numerical id mapping to team id in **teams.json**, seems to start with blue side
        - *Side*: "blue" or "red" side, corresponding to the map on Summoner's Rift
        - *Record*: Object containing:
          - *Wins, Losses, and Ties* of team heading into the match
        - *Result*: Object containing:
          - *Outcome* : "win", "loss" or "tie", overall result of the match
          - *GameWins*: Number of individual games won by the team in the match
        - Players: Array of objects containing:
          - *Id*: unique numerical id mapping to player id in **players.json**
          - *Role*: role of player, one of "top", "jungle", "mid", "support", "bottom"
        - *Games*: Array of objects containing:
          - *Id*: Unique numerical id mapping to game id in **mapping_data.json**
          - *State*: "completed" or "unneeded" based on if a team has already won the match
          - *Number*: Number of game played within the match
          - *Teams*: An array of objects, one for each team, containing:
             - *Id*: Unique numerical id mapping to team id in **teams.json**, seems to start with blue side
             - *Side*: "blue" or "red"
             - *Result*: object containing:
               - *Outcome*: "win", "loss", or null if the game was not played ("unneeded")
        - *Rankings*: Array of objects, either empty or containing the number of objects corresponding to the number of teams. Each object contains:
          - *Ordinal*: Ranking of team(s) in standing
          - *Teams*: Array containing the team(s, in case of ties) corresponding to ranking. Object contains:
            - *Id*: Unique numerical id mapping to team id in **teams.json**
            - *Side*: not relevant to overall standings, and therefore appears exclusively null
            - *Record*: Object containing:
              - *"wins", "losses" and "ties"*
            - *Result*: Also not relevant to overall standings, appears exclusively null
            - *Players*: Array of objects containing:
              - *Id*: unique numerical id mapping to player id in **players.json**
              - *Role*: role of player, one of "top", "jungle", "mid", "support", "bottom"

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










