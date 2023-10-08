import pandas as pd
import json
from database_accessor import Database_Accessor
import sklearn

""" 
+-----------------+
| Tables_in_games |
+-----------------+
| cumulative_data |
| games           |
| leagues         |
| mapping_data    |
| players         |
| teams           |
| tournaments     |
+-----------------+ 
"""

db_accessor: Database_Accessor = Database_Accessor(db_name = 'games', 
    db_host = 'riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com', 
    db_user = 'data_cleaner')

gameCount: int = 0
cumulative_stats = db_accessor.getDataFromTable(tableName="cumulative_data", columns=["id", "scale_by_90"], limit=10, offset=gameCount)
for id, stats in cumulative_stats:
    stats = json.loads(stats)
    print(stats)


df = pd.DataFrame(cumulative_stats, columns=['id', 'stats'])                            # convert cumulative_stats into a pandas dataframe
df['stats'] = df['stats'].apply(json.loads)                                             # convert the 'stats' column from JSON string to dictionary
""" df = pd.concat([df.drop('stats', axis=1), df['stats'].apply(pd.Series)], axis=1)        # expand the 'stats' dictionary column into separate columns
print("debug")
print(df.columns)
df = df.dropna(how='any')                                                               # drop NaN values
#filtered_df = df[df['team_1'].notna() & df['team_2'].notna()]                           # drop rows with no match history between two teams """

# Expand 'team_1' and 'team_2' columns
df_team_1 = df['stats'].apply(lambda x: x['team_1']).apply(pd.Series).add_prefix('team_1_')
df_team_2 = df['stats'].apply(lambda x: x['team_2']).apply(pd.Series).add_prefix('team_2_')

# Drop the original 'stats' column and concatenate the new columns to the dataframe
df = pd.concat([df.drop('stats', axis=1), df_team_1, df_team_2], axis=1)

fields = [
    "avg_kd_ratio", 
    "barons_per_game", 
    "gold_diff_at_14", 
    "overall_winrate", 
    "avg_time_per_win", 
    "dragons_per_game", 
    "first_blood_rate", 
    "first_tower_rate", 
    "heralds_per_game", 
    "turrets_per_game", 
    "gold_diff_per_min", 
    "avg_assists_per_kill", 
    "vision_score_per_minute"
]

for field in fields:
    col_name = f"{field}_diff"
    team_1_col = f'team_1_{field}'
    team_2_col = f'team_2_{field}'
    
    # Check if both columns exist in the DataFrame
    if team_1_col in df.columns and team_2_col in df.columns:
        df[col_name] = df[team_1_col] - df[team_2_col]

# Assign columns in cumulative_data as features X
diff_fields = [f"{field}_diff" for field in fields]
X = df[diff_fields]

# Assign winning team as label y
df['winner'] = df['meta'].apply(lambda x: 'team_1' if x['winning_team'] == 100 else 'team_2')
y = df['winner']

# Splitting the data into a training set and validation set
# test_size = 0.2 means 20% of the dataset will be reserved for testing/validation
# and the remaining 80% will be used for training.
# random_state is just a random initializer
X_train, X_val, y_train, y_val = sklearn.train_test_split(X, y, test_size = 0.2, random_state = 42)

# Normalize fields to be on same scale so as to not skew model. StandardScaler is just standard Z-score normalisation
scaler = sklearn.StandardScaler().fit(X_train)            # Note: we only fit the scaler on training data
X_train = pd.DataFrame(scaler.transform(X_train), columns = X_train.columns)
X_val = pd.DataFrame(scaler.transform(X_val), columns = X_val.columns)

# Train the model (clf = classifier)
clf = sklearn.LogisticRegression().fit(X_train, y_train)

# Evaluate the model
accuracy = clf.score(X_val, y_val)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

