from typing import List
from ranking_model_interface import Ranking_Model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from dao.util import getCumulativeStatsForTeams, getCumulativeDataForTournament, getCumulativeStatsForAllTeams
from dao.database_accessor import Database_Accessor
import pandas as pd
import json

class RegressionModel(Ranking_Model):
    def __init__(self):
        self.model = LogisticRegression(max_iter=10000, C=0.01, penalty='l2') # l2 regularization
        self.scaler = StandardScaler() # init scaler

        X_train, X_val, y_train, y_val = super().get_training_test_datasets()

        # extract one-hot encoded region columns
        self.team_1_regions = [col for col in X_train.columns if col.startswith('team_1_region_')]
        self.team_2_regions = [col for col in X_train.columns if col.startswith('team_2_region_')]
        self.original_columns = X_train.columns.tolist()

        # scale data
        self.X_train = self.scaler.fit_transform(X_train)
        self.X_val = self.scaler.transform(X_val)
        self.y_train = y_train
        self.y_val = y_val


    def cross_validate(self, cv=10):
        skf = StratifiedKFold(n_splits=cv)
        scores = cross_val_score(self.model, self.X_train, self.y_train, cv=skf, scoring='accuracy')
        print(f"Cross-validation scores: {scores}")
        print(f"Average accuracy: {scores.mean()} ± {scores.std()}")

    def tune_hyperparameters(self):
        # hyperparam grid
        param_grid = {
            'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
            'penalty': ['l1', 'l2'],    
            'solver': ['liblinear']
        }

        # grid search with cross-validation
        grid_search = GridSearchCV(self.model, param_grid, cv=10, scoring='accuracy', n_jobs=-1)
        grid_search.fit(self.X_train, self.y_train)
        # update the model with best found parameters
        self.model = grid_search.best_estimator_
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best cross-validation score: {grid_search.best_score_}")

    def train(self):
        weights = self.X_train['weights'].values
        weights = weights.flatten()
        X_train = X_train.drop(columns=['weights'])
        self.model.fit(self.X_train, self.y_train, sample_weight=weights)

    def predict(self, X=None):
        if X is None:
            X = self.X_val
            X = X.drop(columns=['weights'])
        else:
            X = self.scaler.transform(X)
        return self.model.predict(X)

    def evaluate(self):
        y_pred = self.predict()
        accuracy = accuracy_score(self.y_val, y_pred)
        report = classification_report(self.y_val, y_pred)
        print(f"Accuracy: {accuracy}")
        print(report)  
    
    def encode_regions(self, input_df, team1_region, team2_region):
        # assign 0 to all other regions
        team1_region_dict = {col: 0 for col in self.team_1_regions}
        team2_region_dict = {col: 0 for col in self.team_2_regions}

        # assign 1 to specified team1 and team2 regions
        team1_region_dict[f'team_1_region_{team1_region}'] = 1
        team2_region_dict[f'team_2_region_{team2_region}'] = 1

        # add columns and values to dataframe
        for col, value in team1_region_dict.items():
            input_df[col] = value
        for col, value in team2_region_dict.items():
            input_df[col] = value

        # drop unneeded columns
        input_df.drop(columns=['team_1_region', 'team_2_region'], inplace=True)

        # reorder columns according to X_train's columns before scaling
        input_df = input_df[self.original_columns]
   
        return input_df

    def fetch_team_info(self, team_id: str, expected_wins: float) -> dict:
        dao: Database_Accessor = Database_Accessor(db_host='riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com')
        db_data = dao.getDataFromTable(
            "teams",
            ["team"],
            where_clause=f"id = '{team_id}'",
        )

        if not db_data[0][0]:
            print(f"team with team id {team_id} doesn't exist in Teams table")
            return { "expected_wins": expected_wins }

        team_data = json.loads(db_data[0][0])

        return {
            "team_id": team_id,
            "team_code": team_data["acronym"],
            "team_name": team_data["name"],
            "rank": None,                           # placeholder, will be updated in rank_teams function
            "expected_wins": expected_wins
        }    

    def create_teams_stat_df(self, teamA_stats, teamB_stats):
        # returns a DataFrame with the combined stats of both teams
        teamA_prefixed_stats = {f"team_1_{k}": v for k, v in teamA_stats.items()}
        teamB_prefixed_stats = {f"team_2_{k}": v for k, v in teamB_stats.items()}
        combined_stats = {**teamA_prefixed_stats, **teamB_prefixed_stats}
        return pd.DataFrame([combined_stats])
    
    def simulate_match(self, teamA_stats, teamB_stats):
        # prepare team stats for prediction
        input_df = self.create_teams_stat_df(teamA_stats, teamB_stats)

        # one hot encode regions for both teams
        team1_region = teamA_stats['region'][0]
        team2_region = teamB_stats['region'][0]
        input_df = self.encode_regions(input_df, team1_region, team2_region)

        # scale input data
        input_df = self.scaler.transform(input_df)
    
        # predict match outcome
        print("predicting a game...")
        prediction = self.model.predict(input_df)[0]
    
        # return the winning team (either 'A' or 'B')
        return 'A' if prediction == 1 else 'B'
    
    
    def rank_teams(self, teams):
        # win count per team
        wins = {team: 0 for team in teams.keys()}
    
        # round-robin, play every team against every other team
        for teamA_id, teamA_stats in teams.items():
            for teamB_id, teamB_stats in teams.items():
                if teamA_id != teamB_id:
                    winner = self.simulate_match(teamA_stats, teamB_stats)
                    if winner == 'A':
                        wins[teamA_id] += 1
                    else:
                        wins[teamB_id] += 1

        # create rankings by sorting by team win counts
        ranked_teams = sorted(wins.items(), key=lambda x: x[1], reverse=True)

        # handling ranks and ties
        rank = 0
        prev_wins = None

        # initialize list to rebuild ranking info
        ranked_teams_info = []
        for idx, (team_id, win_count) in enumerate(ranked_teams):
            # update rank only if win count is different from previous
            if win_count != prev_wins:
                rank = idx + 1
            prev_wins = win_count

            # fetch team info and update rank
            team_info = self.fetch_team_info(team_id, win_count)
            team_info['rank'] = rank
            ranked_teams_info.append(team_info)

        return ranked_teams_info
  
    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        dao: Database_Accessor = Database_Accessor(db_host='riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com')
        # check cache for rankings. if not cached then rank teams.
        if not self._global_rankings:
            team_stats = getCumulativeStatsForAllTeams(dao)
            self._global_rankings = self.rank_teams(team_stats)

        return self._global_rankings[:n_teams]
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        dao: Database_Accessor = Database_Accessor(db_host='riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com')
        team_stats = getCumulativeDataForTournament(dao, tournament_id, stage)
        rankings = self.rank_teams(team_stats)
        return rankings
    
    def get_custom_rankings(self, team_ids: List[str]) -> List[dict]:
        dao: Database_Accessor = Database_Accessor(db_host='riot-hackathon-db.c880zspfzfsi.us-west-2.rds.amazonaws.com')
        team_stats = getCumulativeStatsForTeams(dao, team_ids)
        rankings = self.rank_teams(team_stats)
        return rankings
  
  

# Testing
model = RegressionModel()
model.tune_hyperparameters()
model.train()
model.cross_validate() # 10 fold CV
model.predict()
model.evaluate()

test_tournament_ranks = model.get_tournament_rankings('103462439438682788', 'Playoffs')
test_custom_ranks = model.get_custom_rankings(['98767991877340524', '103461966951059521', '99294153828264740', '99294153824386385', '98767991860392497', '98926509892121852'])
#ranks = model.get_global_rankings()
print(f"tourney ranks: {test_tournament_ranks}")
print(f"custom ranks: {test_custom_ranks}")