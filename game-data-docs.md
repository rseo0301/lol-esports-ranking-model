
## Game data documentation

Table of contents
- [[#Event types]]
- [[#examples]]





### Event types
in-game events are categorized into different event "types", as outlined below:
 - [`building_destroyed`](#building_destroyed)
 - [`champion_kill`](#champion_kill)
 - [`champion_kill_special`](#champion_kill_special)
 - [`champion_level_up`](#champion_level_up)
 - [`epic_monster_kill`](#epic_monster_kill)
 - [`epic_monster_spawn`](#epic_monster_spawn)
 - [`game_end`](#game_end)
 - [`game_info`](#game_info)
 - [`item_destroyed`](#item_destroyed)
 - [`item_purchased`](#item_purchased)
 - [`item_sold`](#item_sold)
 - [`item_undo`](#item_undo)
 - [`queued_dragon_info`](#queued_dragon_info)
 - [`skill_level_up`](#skill_level_up)
 - [`stats_update`](#stats_update)
 - [`turret_plate_destroyed`](#turret_plate_destroyed)
 - [`ward_killed`](#ward_killed)
 - [`ward_placed`](#ward_placed)



#### `building_destroyed`
| attribute name   | type     | description                                     | notes                                                                                         |
| ---------------- | -------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string   | Timestamp of event                              |                                                                                               |
| `eventType`      | string   | event name                                      |                                                                                               |
| `platformGameId` | string   | Game ID                                         |                                                                                               |
| `gameTime`       | number   | In-game time when event fired (in ms)           |                                                                                               |
| `assistants`     | number[] | players that helped destroy this building       |                                                                                               |
| `teamID`         | number   | Team ID (100 or 200)                            |                                                                                               |
| `lastHitter`     | number   | Player that got actually destroyed the building |                                                                                               |
| `gameName`       | string   | Another unique identifier for this game         | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number   | ?                                               |                                                                                               |
| `buildingType`   | string   | type of building destroyed                      | `"turret"` or `"inhibitor"`                                                                   |
| `position`       | object   | position of building on the map                 |                                                                                               |
| `position.z`     | number   | z-coordinate of building                        |                                                                                               |
| `position.x`     | number   | x-coordinate of building                        |                                                                                               |
| `lane`           | string   | the lane where this building was located        | `"mid"` or `"top"` or `"bot"`                                                                 |
| `turretTier`     | string   | location of turret relative to nexus; undefined if `buildingType = "inhibitor"`            | `"outer"`, `"inner"`, `"base"`, or `"nexus"`                                                  |
| `playbackID`     | number   | ?                                               | in the game I am looking at, it is always set to 1, not sure if that applies across all games |

```json
{
	"eventTime": "2019-05-01T09:27:36.554Z",
	"eventType": "building_destroyed",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 939441,
	"assistants": [],
	"teamID": 200,
	"lastHitter": 0,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"sequenceIndex": 1534,
	"buildingType": "turret",
	"position": {
		"z": 8510,
		"x": 8955
	},
	"lane": "mid",
	"turretTier": "outer",
	"playbackID": 1
}
```

---
#### `champion_kill_special`
| attribute name     | type   | description                             | notes                                                                                         |
| ------------------ | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`        | string | Timestamp of event                      |                                                                                               |
| `eventType`        | string | event name                              |                                                                                               |
| `platformGameId`   | string | Game ID                                 |                                                                                               |
| `gameTime`         | number | In-game time when event fired (in ms)   |                                                                                               |
| `killer`           | number | Player index that killed                |                                                                                               |
| `killStreakLength` | number | `killer`'s kill streak length           |   only defined if `killType = "multi"`                                                                                            |
| `gameName`         | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`    | number | ?                                       |                                                                                               |
| `position`         | object | position of event on the map         |                                                                                               |
| `position.z`       | number | z-coordinate of event                |                                                                                               |
| `position.x`       | number | x-coordinate of event                |                                                                                               |
| `playbackID`       | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `killType`         | string | type of kill event                      | `"firstBlood"`, `"multi"`, or `"ace"`                                                                                              |

```json
{
	"eventTime": "2019-05-01T09:16:02.733Z",
	"eventType": "champion_kill_special",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"killType": "firstBlood",
	"gameTime": 245612,
	"sequenceIndex": 368,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"position": {
		"z": 2298,
		"x": 12995
	},
	"killer": 2,
	"playbackID": 1
}
```

---
#### `champion_kill`
| attribute name     | type     | description                                 | notes                                                                                         |
| ------------------ | -------- | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`        | string   | Timestamp of event                          |                                                                                               |
| `eventType`        | string   | event name                                  |                                                                                               |
| `platformGameId`   | string   | Game ID                                     |                                                                                               |
| `gameTime`         | number   | In-game time when event fired (in ms)       |                                                                                               |
| `killer`           | number   | Player index that killed `victim`           |                                                                                               |
| `killStreakLength` | number   | `killer`'s kill streak length               |                                                                                               |
| `gameName`         | string   | Another unique identifier for this game     | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`    | number   | ?                                           |                                                                                               |
| `position`         | object   | position of event on the map             |                                                                                               |
| `position.z`       | number   | z-coordinate of event                    |                                                                                               |
| `position.x`       | number   | x-coordinate of event                    |                                                                                               |
| `playbackID`       | number   | ?                                           | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `victimTeamID`     | number   | Team ID of player that was killed           | `100`  or `200`                                                                               |
| `victim`           | number   | Index of player that got killed             |                                                                                               |
| `bounty`           | number   | Bounty gold received by killer                                |                                                                                               |
| `assistants`       | number[] | Indexes of players that earned kill assists |                                                                                               |
| `killerTeamID`     | number   | Team ID of player that killed `victim`      | `100` or `200`                                                                                              |

```json
{
	"eventTime": "2019-05-01T09:16:02.726Z",
	"eventType": "champion_kill",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"victimTeamID": 200,
	"gameTime": 245612,
	"victim": 10,
	"sequenceIndex": 367,
	"killer": 2,
	"killStreakLength": 0,
	"bounty": 400,
	"assistants": [
		5
	],
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"position": {
		"z": 2110,
		"x": 13209
	},
	"playbackID": 1,
	"killerTeamID": 100
	}
```

---

#### `champion_level_up`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `participant`    | number | Index of participant that levelled up   |                                                                                               |
| `level`          | number | Participant's new level                 |                                                                                               |

```json
{
	"eventTime": "2019-05-01T09:15:57.053Z",
	"eventType": "champion_level_up",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 239950,
	"level": 4,
	"sequenceIndex": 355,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"participant": 1,
	"playbackID": 1
}
```

---

#### `epic_monster_kill`

| attribute name   | type     | description                             | notes                                                                                         |
| ---------------- | -------- | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string   | Timestamp of event                      |                                                                                               |
| `eventType`      | string   | event name                              |                                                                                               |
| `platformGameId` | string   | Game ID                                 |                                                                                               |
| `gameTime`       | number   | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string   | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number   | ?                                       |                                                                                               |
| `playbackID`     | number   | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `assistants`     | number[] | Indexes of participants that helped     |                                                                                               |
| `monsterType`    | string   | upper camel case name of monster killed      | `redCamp`, `scuttleCrab`, `blueCamp`, `dragon`, `riftHerald`, `baron`                         |
| `position`       | object   | Position of mob on the map              |                                                                                               |
| `position.x`     | number   | x-coordinate of mob on the map          |                                                                                               |
| `position.z`     | number   | z-coordinate of mob on the map          |                                                                                               |
| `killer`         | number   | Index of player that killed the mob     |                                                                                               |
| `inEnemyJungle`  | boolean  | whether this mob was counter-jungled    |                                                                                               |
| `killerTeamID`   | number   | Team ID associated with mob killer      | `100` or `200`                                                                                |

```json
{
	"eventTime": "2019-05-01T09:37:21.411Z",
	"eventType": "epic_monster_kill",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 1524288,
	"assistants": [],
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"monsterType": "scuttleCrab",
	"position": {
		"z": 8329,
		"x": 5858
	},
	"killer": 2,
	"sequenceIndex": 2533,
	"playbackID": 1,
	"inEnemyJungle": false,
	"killerTeamID": 100
}
```

---

#### `epic_monster_spawn`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `monsterType`    | string | upper camel case name of mob killed     | seems to be `dragon` only?                                                                    |
| `dragonType`     | strign | type of dragon                          | `air`, `earth`, `fire`, `ocean`                                                               |

```json
{
	"eventTime": "2019-05-01T09:16:50.619Z",
	"eventType": "epic_monster_spawn",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 293514,
	"sequenceIndex": 464,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"monsterType": "dragon",
	"dragonType": "air",
	"playbackID": 1
}
```

---

#### `game_end`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `wallTime`       | number | ??                                      |                                                                                               |
| `winningTeam`    | number | Team ID of winning team                 | `100` or `200`                                                                                |

```json
{
	"eventTime": "2019-05-01T09:40:59.589Z",
	"eventType": "game_end",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 1742456,
	"wallTime": 1556703659585,
	"sequenceIndex": 2897,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"winningTeam": 100,
	"playbackID": 1
}
```

---

#### `game_info`

| attribute name        | type     | description                             | notes                                                                                         |
| --------------------- | -------- | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`           | string   | Timestamp of event                      |                                                                                               |
| `eventType`           | string   | event name                              |                                                                                               |
| `platformGameId`      | string   | Game ID                                 |                                                                                               |
| `gameName`            | string   | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`       | number   | ?                                       |                                                                                               |
| `playbackID`          | number   | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `participants`        | object[] | Info about each player in the game      | length 10                                                                                     |
| `statsUpdateInterval` | number   | frequency of event collection           | assumed to be in ms                                                                           |
| `gameVersion`         | string   | Game version                            |                                                                                               |

###### `game_info.participants[i]`

| attribute name  | type     | description              | notes                                                           |
| --------------- | -------- | ------------------------ | --------------------------------------------------------------- |
| `keystoneID`    | number   | Keystone ID?             |                                                                 |
| `hashedIP`      | string   | Hashed IP address?       |                                                                 |
| `teamID`        | number   | Team ID                  | `100` or `200`                                                  |
| `participantID` | number   | ID of player             | ranges from 1 to 10                                             |
| `championName`  | string   | champ name               | `Jayce`, `Ahri`, etc.                                           |
| `accountID`     | number   | account ID               |                                                                 |
| `abGroup`       | string   | ?                        | In the game file I downloaded, the only value is `"Everything"` |
| `perks`         | object[] | 1-item array of perks(?) |                                                                 |
| `summonerName`  | string   | IGN of player            |                                                                 |
| `summonerLevel` | number   | account level            |                                                                 |

###### `game_info.participants[i].perks[0]`
***note that there is only 1 object in the `perks` array***

| attribute name | type     | description     | notes                     |
| -------------- | -------- | --------------- | ------------------------- |
| `perkIds`      | number[] | list of perk ID | Not sure what "perks" are |
| `perkStyle`    | number   | perk style      |                           |
| `perkSubStyle` | number   | perk sub-style                |                           |

The example below had its `participants` array truncated for brevity - it originally held 10 objects, 1 for each player in the game
```json
{
	"eventTime": "2019-05-01T09:11:39.980Z",
	"eventType": "game_info",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"participants": [
		{
			"keystoneID": 8010,
			"hashedIP": "3VoTUXLOxMy1OmdTUitHpqfdYIc=",
			"teamID": 100,
			"participantID": 1,
			"championName": "Jayce",
			"accountID": 200014860,
			"abGroup": "Everything",
			"perks": [
				{
				"perkIds": [
					8010,
					9111,
					9105,
					8014,
					8304,
					8345,
					5008,
					5008,
					5002
				],
				"perkStyle": 8000,
				"perkSubStyle": 8300
				}
			],
			"summonerName": "PVB Zeros",
			"summonerLevel": 30
		},
	],
	"sequenceIndex": 0,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"gameVersion": "9.8.270.9450",
	"statsUpdateInterval": 1000,
	"playbackID": 1
}
```

---

#### `item_destroyed`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `itemID`         | number | ID of item destroyed                    |                                                                                               |
| `participantID`  | number | ID of player that destroyed item        |                                                                                               |

```json
{
	"eventTime": "2019-05-01T09:19:28.255Z",
	"eventType": "item_destroyed",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"itemID": 2055,
	"gameTime": 451149,
	"participantID": 7,
	"sequenceIndex": 713,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"playbackID": 1
}
```

---

#### `item_purchased`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `itemID`         | number | ID of item purchased                    |                                                                                               |
| `participantID`  | number | ID of player that purchased item        |                                                                                               |

```json
{
	"eventTime": "2019-05-01T09:12:00.493Z",
	"eventType": "item_purchased",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"itemID": 1041,
	"gameTime": 3394,
	"participantID": 2,
	"sequenceIndex": 8,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"playbackID": 1
}
```

---

#### `item_sold`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `itemID`         | number | ID of item sold                    |                                                                                               |
| `participantID`  | number | ID of player that sold item        |                                                                                               |

```json
{
	"eventTime": "2019-05-01T09:19:46.218Z",
	"eventType": "item_sold",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"itemID": 2004,
	"gameTime": 469113,
	"participantID": 4,
	"sequenceIndex": 748,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"playbackID": 1
}
```

---

#### `item_undo`

| attribute name   | type                | description                               | notes                                                                                         |
| ---------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string              | Timestamp of event                        |                                                                                               |
| `eventType`      | string              | event name                                |                                                                                               |
| `platformGameId` | string              | Game ID                                   |                                                                                               |
| `gameTime`       | number              | In-game time when event fired (in ms)     |                                                                                               |
| `gameName`       | string              | Another unique identifier for this game   | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number              | ?                                         |                                                                                               |
| `playbackID`     | number              | ?                                         | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `itemID`         | number              | ID of item involved in the undo           |                                                                                               |
| `participantID`  | number              | ID of player that did the undoing         |                                                                                               |
| `goldGain`       | number              | Amount of gold gained back from undoing   | not sure if this field can also be                                                                                               |
| `itemsAdded`     | number[] (OPTIONAL) | array of item IDs added back from undoing | only some objects have this field                                                                                               |
| `itemBeforeUndo` | number              | ID of item before undoing                 |                                                                                               |

```json
{
	"eventTime": "2019-05-01T09:34:00.477Z",
	"eventType": "item_undo",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"itemID": 3047,
	"gameTime": 1323360,
	"goldGain": 800,
	"itemsAdded": [
		2422
	],
	"participantID": 4,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"sequenceIndex": 2187,
	"playbackID": 1,
	"itemBeforeUndo": 3047
}
```

---

#### `queued_dragon_info`

| attribute name        | type   | description                             | notes                                                                                         |
| --------------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`           | string | Timestamp of event                      |                                                                                               |
| `eventType`           | string | event name                              |                                                                                               |
| `platformGameId`      | string | Game ID                                 |                                                                                               |
| `gameTime`            | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`            | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`       | number | ?                                       |                                                                                               |
| `playbackID`          | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `nextDragonSpawnTime` | number | Dragon respawn time in ms               |                                                                                               |
| `nextDragonName`      | string | name of next dragon spawning            | `fire`, `ocean`, `air`, `earth`                                                               |

```json
{
	"eventTime": "2019-05-01T09:36:14.672Z",
	"eventType": "queued_dragon_info",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 1457545,
	"sequenceIndex": 2409,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"nextDragonSpawnTime": 1758,
	"playbackID": 1,
	"nextDragonName": "fire"
}
```

---

#### `skill_level_up`

| attribute name   | type    | description                                | notes                                                                                         |
| ---------------- | ------- | ------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string  | Timestamp of event                         |                                                                                               |
| `eventType`      | string  | event name                                 |                                                                                               |
| `platformGameId` | string  | Game ID                                    |                                                                                               |
| `gameTime`       | number  | In-game time when event fired (in ms)      |                                                                                               |
| `gameName`       | string  | Another unique identifier for this game    | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number  | ?                                          |                                                                                               |
| `playbackID`     | number  | ?                                          | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `skillSlot`      | number  | 1-based index of skill leveled up          |                                                                                               |
| `participant`    | number  | ID of player that leveled up their ability |                                                                                               |
| `evolved`        | boolean | whether or not this skill was "evolved"    | "evolved" probably refers to things like viktor's ability augments, khazix evolution, etc.    |

```json
{
	"eventTime": "2019-05-01T09:12:06.716Z",
	"eventType": "skill_level_up",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 9617,
	"skillSlot": 1,
	"sequenceIndex": 42,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"participant": 8,
	"playbackID": 1,
	"evolved": false
}
```

---

#### `stats_update`

| attribute name   | type     | description                                                                    | notes                                                                                         |
| ---------------- | -------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string   | Timestamp of event                                                             |                                                                                               |
| `eventType`      | string   | event name                                                                     |                                                                                               |
| `platformGameId` | string   | Game ID                                                                        |                                                                                               |
| `gameTime`       | number   | In-game time when event fired (in ms)                                          |                                                                                               |
| `gameName`       | string   | Another unique identifier for this game                                        | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number   | ?                                                                              |                                                                                               |
| `playbackID`     | number   | ?                                                                              | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `participants`   | object[] | array of [current stat objects](#stats_update.participants[i]) for each player | length 10 array                                                                               |
| `gameOver`       | boolean  | whether game has ended or not                                                  |                                                                                               |
| `teams`          | object[] | 2-item array consisting of each team-wide stats                                |                                                                                               |

###### `stats_update.participants[i]`

| attribute name                 | type     | description                                  | notes                                                           |
| ------------------------------ | -------- | -------------------------------------------- | --------------------------------------------------------------- |
| `magicPenetrationPercent`      | number   | % magic pen                                  |                                                                 |
| `participantID`                | number   | Player (participant) ID                      |                                                                 |
| `primaryAbilitySource`         | number   | primary ability source?                      | could be denoting AP/AD scaling for abilities                   |
| `spellVamp`                    | number   | spell vamp                                   |                                                                 |
| `cooldownReduction`            | number   | cooldown reduction                           |                                                                 |
| `lifeSteal`                    | number   | life steal                                   |                                                                 |
| `primaryAbilityResourceRegen`  | number   | primary ability resource regen               | could be denoting whether champion uses mana, rage, or sth else |
| `magicPenetrationPercentBonus` | number   | bonus % magic pen                            |                                                                 |
| `magicPenetration`             | number   | total magic pen?                             |                                                                 |
| `healthMax`                    | number   | max HP                                       |                                                                 |
| `position`                     | object   | position of player                           |                                                                 |
| `position.x`                   | number   | x-coordinate of player                       |                                                                 |
| `position.z`                   | number   | z-coordinate of player                       |                                                                 |
| `magicResist`                  | number   | magic resistance                             |                                                                 |
| `primaryAbilityResourceMax`    | number   | maximum mana/rage/etc. cap                   |                                                                 |
| `armorPenetrationPercentBonus` | number   | bonus % armor pen                            |                                                                 |
| `armorPenetrationPercent`      | number   | % armor pen                                  |                                                                 |
| `attackDamage`                 | number   | AD                                           |                                                                 |
| `teamID`                       | number   | team ID of player                            |                                                                 |
| `ccReduction`                  | number   | CC (crowd control) reduction                 |                                                                 |
| `currentGold`                  | number   | player's gold amount                         |                                                                 |
| `healthRegen`                  | number   | HP regen                                     |                                                                 |
| `attackSpeed`                  | number   | attack speed                                 |                                                                 |
| `XP`                           | number   | XP points for player                         |                                                                 |
| `armor`                        | number   | armor                                        |                                                                 |
| `level`                        | number   | player level                                 |                                                                 |
| `armorPenetration`             | number   | total armor pen?                             |                                                                 |
| `accountID`                    | number   | account ID                                   |                                                                 |
| `totalGold`                    | number   | player's total gold?                         | not sure of difference b/w this field and `currentGold`         |
| `health`                       | number   | current HP                                   |                                                                 |
| `abilityPower`                 | number   | AP                                           |                                                                 |
| `stats`                        | object[] | array of key-value pairs for different stats | all stats listed in the [Appendix](#Appendix)                   |
| `goldPerSecond`                | number   | passive gold income per second               |                                                                 |

###### `stats_update.teams[i]`
`teams` array contains 2 objects, 1 per team

| attribute name  | type   | description                 | notes |
| --------------- | ------ | --------------------------- | ----- |
| `inhibKills`    | number | # inhibitors destroyed      |       |
| `towerKills`    | number | # towers destroyed          |       |
| `teamID`        | number | Team ID                     |       |
| `baronKills`    | number | # barons killed             |       |
| `dragonKills`   | number | # dragons killed            |       |
| `assists`       | number | total # assists across team |       |
| `totalGold`     | number | total gold across team      |       |
| `championKills` | number | total # kills across team   |       |
| `deaths`        | number | total # deaths across team  |       |

***This example was truncated for brevity; normally, `participants` should have 10 objects, and `participants[i].stats` should have all key-value pairs outlined in the [Appendix](#Appendix)***

```json
{
	"eventTime": "2019-05-01T09:11:57.308Z",
	"eventType": "stats_update",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 0,
	"participants": [
		{
			"magicPenetrationPercent": 0,
			"participantID": 1,
			"primaryAbilityResource": 357,
			"spellVamp": 0,
			"cooldownReduction": 0,
			"lifeSteal": 0,
			"primaryAbilityResourceRegen": 12,
			"magicPenetrationPercentBonus": 0,
			"magicPenetration": 0,
			"healthMax": 560,
			"position": {
				"z": 581,
				"x": 560
			},
			"magicResist": 30,
			"primaryAbilityResourceMax": 357,
			"armorPenetrationPercentBonus": 0,
			"armorPenetrationPercent": 0,
			"attackDamage": 58,
			"teamID": 100,
			"ccReduction": 0,
			"currentGold": 500,
			"healthRegen": 12,
			"attackSpeed": 100,
			"XP": 0,
			"armor": 27,
			"level": 1,
			"armorPenetration": 0,
			"accountID": 200014860,
			"totalGold": 500,
			"health": 560,
			"abilityPower": 0,
			"stats": [
				{
					"value": 0,
					"name": "MINIONS_KILLED"
				},
				{
					"value": 0,
					"name": "NEUTRAL_MINIONS_KILLED"
				},
				{
					"value": 0,
					"name": "NEUTRAL_MINIONS_KILLED_YOUR_JUNGLE"
				},
				{
					"value": 0,
					"name": "NEUTRAL_MINIONS_KILLED_ENEMY_JUNGLE"
				},
				{
					"value": 0,
					"name": "CHAMPIONS_KILLED"
				}
			],
			"goldPerSecond": 0
		}
	],
	"gameOver": false,
	"sequenceIndex": 3,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"teams": [
		{
			"inhibKills": 0,
			"towerKills": 0,
			"teamID": 100,
			"baronKills": 0,
			"dragonKills": 0,
			"assists": 0,
			"totalGold": 2500,
			"championsKills": 0,
			"deaths": 0
		},
		{
			"inhibKills": 0,
			"towerKills": 0,
			"teamID": 200,
			"baronKills": 0,
			"dragonKills": 0,
			"assists": 0,
			"totalGold": 2500,
			"championsKills": 0,
			"deaths": 0
		}
	],
	"playbackID": 1
}
```

---

#### `turret_plate_destroyed.json`

| attribute name   | type     | description                                       | notes                                                                                         |
| ---------------- | -------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string   | Timestamp of event                                |                                                                                               |
| `eventType`      | string   | event name                                        |                                                                                               |
| `platformGameId` | string   | Game ID                                           |                                                                                               |
| `gameTime`       | number   | In-game time when event fired (in ms)             |                                                                                               |
| `gameName`       | string   | Another unique identifier for this game           | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number   | ?                                                 |                                                                                               |
| `playbackID`     | number   | ?                                                 | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `assistants`     | number[] | list of participant IDs that helped destroy plate |                                                                                               |
| `teamID`         | number   | Team ID that destroyed the plate                  |                                                                                               |
| `lastHitter`     | number   | Player that got the last hit on the plate?        | Always set to 0 and idk why                                                                   |
| `position`       | object   | position of turret                                |                                                                                               |
| `position.x`     | number   | x-coordinate of turret                            |                                                                                               |
| `position.z`     | number   | z-coordinate of turret                            |                                                                                               |
| `lane`           | string   | the lane where turret is located                  | `top`, `mid`, or `bot`                                                                        |

```json
{
	"eventTime": "2019-05-01T09:22:39.584Z",
	"eventType": "turret_plate_destroyed",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 642475,
	"assistants": [],
	"teamID": 200,
	"lastHitter": 0,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"sequenceIndex": 1047,
	"position": {
		"z": 8510,
		"x": 8955
	},
	"lane": "mid",
	"playbackID": 1
}
```

---

#### `ward_killed`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `position`       | object | position of ward killed                      |                                                                                               |
| `position.x`     | number | x-coordinate of ward                  |                                                                                               |
| `position.z`     | number | z-coordinate of ward                  |                                                                                               |
| `wardType`       | string | type of ward                            | `yellowTrinket`, `control`, `sight`, or `blueTrinket`                                         |
| `killer`         | number | ID of player that killed ward           |                                                                                               |

```json
{
	"eventTime": "2019-05-01T09:12:46.485Z",
	"eventType": "ward_killed",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 49385,
	"sequenceIndex": 89,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"wardType": "yellowTrinket",
	"killer": 6,
	"position": {
		"z": 2868,
		"x": 10284
	},
	"playbackID": 1
}
```

---

#### `ward_placed`

| attribute name   | type   | description                             | notes                                                                                         |
| ---------------- | ------ | --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `eventTime`      | string | Timestamp of event                      |                                                                                               |
| `eventType`      | string | event name                              |                                                                                               |
| `platformGameId` | string | Game ID                                 |                                                                                               |
| `gameTime`       | number | In-game time when event fired (in ms)   |                                                                                               |
| `gameName`       | string | Another unique identifier for this game | There doesn't seem to be a unified formatting followed by this field                          |
| `sequenceIndex`  | number | ?                                       |                                                                                               |
| `playbackID`     | number | ?                                       | in the game I am looking at, it is always set to 1, not sure if that applies across all games |
| `position`       | object | position of ward placed                      |                                                                                               |
| `position.x`     | number | x-coordinate of ward                  |                                                                                               |
| `position.z`     | number | z-coordinate of ward                  |                                                                                               |
| `wardType`       | string | type of ward                            | `yellowTrinket`, `control`, `sight`, or `blueTrinket`                                         |
| `placer`         | number | ID of player that placed ward           |                                                                                               |

```json
{
	"eventTime": "2019-05-01T09:12:43.662Z",
	"eventType": "ward_placed",
	"platformGameId": "ESPORTSTMNT01:1110148",
	"gameTime": 46562,
	"sequenceIndex": 84,
	"gameName": "bmr|pvb|g1|29219dd268bb46b2981",
	"wardType": "yellowTrinket",
	"position": {
		"z": 2868,
		"x": 10284
	},
	"playbackID": 1,
	"placer": 4
}
```

---
---

#### Appendix

###### `stats_update.participants[i].stats[j]`
| attribute name | type   | description               | notes |
| -------------- | ------ | ------------------------- | ----- |
| `value`        | number | Value for associated stat |       |
| `name`         | string | Type of stat.             |       |

Possible `name` values include:
 - `MINIONS_KILLED`
 - `NEUTRAL_MINIONS_KILLED`
 - `NEUTRAL_MINIONS_KILLED_YOUR_JUNGLE`
 - `NEUTRAL_MINIONS_KILLED_ENEMY_JUNGLE`
 - `CHAMPIONS_KILLED`
 - `NUM_DEATHS`
 - `ASSISTS`
 - `PERK0`
 - `PERK0_VAR1`
 - `PERK0_VAR2`
 - `PERK0_VAR3`
 - `PERK1`
 - `PERK1_VAR1`
 - `PERK1_VAR2`
 - `PERK1_VAR3`
 - `PERK2`
 - `PERK2_VAR1`
 - `PERK2_VAR2`
 - `PERK2_VAR3`
 - `PERK3`
 - `PERK3_VAR1`
 - `PERK3_VAR2`
 - `PERK3_VAR3`
 - `PERK4`
 - `PERK4_VAR1`
 - `PERK4_VAR2`
 - `PERK4_VAR3`
 - `PERK5`
 - `PERK5_VAR1`
 - `PERK5_VAR2`
 - `PERK5_VAR3`
 - `WARD_PLACED`
 - `WARD_KILLED`
 - `VISION_SCORE`
 - `TOTAL_DAMAGE_DEALT`
 - `PHYSICAL_DAMAGE_DEALT_PLAYER`
 - `MAGIC_DAMAGE_DEALT_PLAYER`
 - `TRUE_DAMAGE_DEALT_PLAYER`
 - `TOTAL_DAMAGE_DEALT_TO_CHAMPIONS`
 - `PHYSICAL_DAMAGE_DEALT_TO_CHAMPIONS`
 - `MAGIC_DAMAGE_DEALT_TO_CHAMPIONS`
 - `TRUE_DAMAGE_DEALT_TO_CHAMPIONS`
 - `TOTAL_DAMAGE_TAKEN`
 - `PHYSICAL_DAMAGE_TAKEN`
 - `MAGIC_DAMAGE_TAKEN`
 - `TRUE_DAMAGE_TAKEN`
 - `TOTAL_DAMAGE_SELF_MITIGATED`
 - `TOTAL_DAMAGE_SHIELDED_ON_TEAMMATES`
 - `TOTAL_DAMAGE_DEALT_TO_BUILDINGS`
 - `TOTAL_DAMAGE_DEALT_TO_TURRETS`
 - `TOTAL_DAMAGE_DEALT_TO_OBJECTIVES`
 - `TOTAL_TIME_CROWD_CONTROL_DEALT`
 - `TOTAL_HEAL_ON_TEAMMATES`
 - `TIME_CCING_OTHERS`