from typing import List

import numpy as np
import requests
from Models.ranking_model_interface import Ranking_Model
from API.main import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from dao.util import getCumulativeDataForTournament

class RandomForest(Ranking_Model):

    model = RandomForestClassifier(n_estimators=150, min_samples_split=2, min_samples_leaf=1, max_features='sqrt', max_depth=7, bootstrap=True)

    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        return super().get_global_rankings(n_teams)
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        return super().get_tournament_rankings
    
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        return super().get_custom_rankings(teams)
    
    def fit(self, X, y):
        self.model
        self.model.fit(X, y)

    def predict(self, X):
        result = self.model.predict_proba(X)
        return result
    
    def optimal_parameters(self):
        # Number of trees in random forest
        n_estimators = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
        max_features = ['log2', 'sqrt']
        max_depth = [3,4,5,6,7]
        min_samples_split = [2, 5]
        min_samples_leaf = [1, 2]
        bootstrap = [True, False]
        # Create the param grid
        param_grid = {'n_estimators': n_estimators,
                    'max_features': max_features,
                    'max_depth': max_depth,
                    'min_samples_split': min_samples_split,
                    'min_samples_leaf': min_samples_leaf,
                    'bootstrap': bootstrap}

        model = RandomForestClassifier()
        search = RandomizedSearchCV(estimator=model, param_distributions= param_grid, cv=10, verbose=2, n_jobs=-1, n_iter=150)
        search.fit(self.datasets[0], self.datasets[2])
        print(search.best_params_)
        print(search.score(self.datasets[1], self.datasets[3]))
        #{'n_estimators': 110, 'min_samples_split': 5, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'max_depth': 7, 'bootstrap': True}

rfc = RandomForest()
rfc.get_training_test_datasets()
# rfc.optimal_parameters()
print(rfc.datasets[0].columns)