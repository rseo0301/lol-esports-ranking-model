## Documentation
### League.json: Array of Leagues
##### Each League object contains:
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



