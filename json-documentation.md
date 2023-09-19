## Documentation
### League.json
##### Each Object Contains:
- Id: numerical identifier for league
- Name: name of league
  - Some names aren’t very good and may need cleaning- ie. “2023”
- Slug: unique named identifier for league
  - Naturally a much clearer identifier compared to name
- Sport: name of esport/game
  - Only existing value in this dataset is ‘lol’ (League of Legends) as expected
- Image: URL Link image of logo
- lightImage: URL Link of light version of logo
  - Same URL as ‘Image’ if one does not exist
- darkImage: URL link of dark version of logo
  - Same URL as ‘Image’ if one does not exist
- Region: Region of the league. Listed below is all regions present in the dataset.
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
- Priority: Integer value, currently **unclear**.
  - Range of values from 1 ~ 1000, 1000 seems to be for smaller leagues
  - single digit leagues (NA = 1, LEC = 3, LCK = 4) seems to be bigger for bigger leagues, but LPL = 201
- Display Priority: Object where:
  - Position: Integer value, function **unclear**
  - Status: Either "selected" or "not_selected", function **unclear**
- Tournaments: An array of objects where each object contains:
  - Id: a numerical identifier for a tournament hosted by the league
  - **maps to id in tournament.json**

### Players.json
##### Each object contains:
- Player_id: A unique numerical identifier for the player
- Handle: The game handle that the player uses in game
- First_name: (Presumed) Legal/Actual first name of player
- Last_name: (Presumed) Legal/Actual last name of player
- Home_team_id: A numerical identifier for the player's current team
  - **maps to id in teams.json**
 
### Teams.json
##### Each object contains:
- Team_id: A unique numerical identifier for the team
- Name: Name of the team
- Acronym: 2, 3, or 4 character acronym of the team
- Slug: uniquely named identifier for the team

### Tournaments.json
##### Each object contains:
- Id: A unique numerical identifier for the tournament
- LeagueId: A unique numerical identifier for the league that the tournament is hosted in
  - **maps to id in leagues.json**
- Name: Name of the tournament
- Slug: Unique named identifier for the tournament
- Sport: Name of game title, exclusive to "lol" in this dataset.
- StartDate: Start date of the tournament
- EndDate: End date of the tournament
- Stages: an array of objects, where each object contains:
  - Name: Name of stage in tournament
  - Type: **unclear**, all values null
  - Slug: Identifier for the stage of tournament
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
  - Sections: An array of objects, where each object contains:
    - Name: Specific name of group within stage, ie. "Group A"
    - Matches: An array of matches played in the section. Each match contains:
      - ID: Unique numerical identifier for the match
      - Type: **unclear**, might be "normal" for all values?
      - Mode: **unclear**, might be "classic for all values, may be for cases in special events (ie. URF)
      - Strategy: object containing:
        - Type: **unclear**, seems to be "bestOf" for all values
        - Count: Corresponds to the max number of games to be played in the match, ie. "Best Of 5"
      - Teams: array of size 2, each object containing:
        - Id: Unique numerical id mapping to team id in **teams.json**, seems to start with blue side
        - Side: "blue" or "red" side, corresponding to the map on Summoner's Rift
        - Record: Object containing:
          - Wins, Losses, and Ties of team heading into the match
        - Result: Object containing:
          - Outcome: "win", "loss" or "tie", overall result of the match
          - GameWins: Number of individual games won by the team in the match
        - Players: Array of objects containing:
          - Id: unique numerical id mapping to player id in **players.json**
          - Role: role of player, one of "top", "jungle", "mid", "support", "bottom"
        - Games: Array of objects containing:
          - Id: Unique numerical id mapping to game id in **mapping_data.json**
          - State: "completed" or "unneeded" based on if a team has already won the match
          - Number: Number of game played within the match
          - Teams: An array of objects, one for each team, containing:
             - Id: Unique numerical id mapping to team id in **teams.json**, seems to start with blue side
             - Side: "blue" or "red"
             - Result: object containing:
               - Outcome: "win", "loss", or null if the game was not played ("unneeded")
        - Rankings: Array of objects, either empty or containing the number of objects corresponding to the number of teams. Each object contains:
          - Ordinal: Ranking of team(s) in standing
          - Teams: Array containing the team(s, in case of ties) corresponding to ranking. Object contains:
            - Id: Unique numerical id mapping to team id in **teams.json**
            - Side: not relevant to overall standings, and therefore appears exclusively null
            - Record: Object containing:
              - "wins", "losses" and "ties"
            - Result: Also not relevant to overall standings, appears exclusively null
            - Players: Array of objects containing:
              - Id: unique numerical id mapping to player id in **players.json**
              - Role: role of player, one of "top", "jungle", "mid", "support", "bottom"

### Mapping_data.json
##### Each object contains:
- ESportsGameId: Unique numerical identifier for the game, referenced in **tournaments.json**
- PlatformGameId: Another identifier used to reference the individual game files
  - **unclear** if the combination of letters and numbers hold any significance
- TeamMapping: object containing:
  - 200: Holds Id of first team, **not confirmed** but presumed to be the red team
  - 100: Holds Id of second team, **not confirmed** but presumed to be the blue team
- ParticipantMapping: object containing:
- Keys from 1 to 10, holding the player IDs of the 10 players
  - **not confirmed** if the indexing holds any significance










