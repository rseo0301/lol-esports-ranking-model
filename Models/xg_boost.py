import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ranking_model_interface import Ranking_Model
from typing import List
from sklearn.model_selection import train_test_split, cross_validate
import pandas as pd
import numpy as np
import json
from xgboost import XGBClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.ensemble import GradientBoostingClassifier, HistGradientBoostingClassifier
from catboost import CatBoostClassifier

class XGBoostModel(Ranking_Model):
    def __init__(self) -> None:
        super().__init__()

    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        return super().get_global_rankings(n_teams)
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        return super().get_tournament_rankings(tournament_id, stage)
    
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        return super().get_custom_rankings(teams)
    
    def separate_xy(self, df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
        return (df.drop(columns=["winner"]), df["winner"])
    
    def fit_model(self, X_train: pd.DataFrame = None, y_train: pd.DataFrame = None) -> None:
        with open("bruh-0.json", "r") as f:
            self.raw_data_dict = json.loads(f.read())
        df = pd.DataFrame(self.raw_data_dict)
        df["winner"] = np.where(df["winner"] == 100, 1, 0)

        train_df, test_df = train_test_split(df, test_size=0.2, random_state=123)
        X_train, y_train = self.separate_xy(train_df)
        X_test, y_test = self.separate_xy(test_df)

        ohe = OneHotEncoder(dtype=int, sparse_output=False)
        cols = list(X_train.columns)
        ohe_feats = ["team_1_region", "team_2_region"]
        numeric_feats = list(filter(lambda c: c not in ohe_feats, cols))

        preprocessor = make_column_transformer(
            (ohe, ohe_feats),
        )

        pipeline = make_pipeline(preprocessor, XGBClassifier(random_state=123))
        cv_score = cross_validate(pipeline, X_train, y_train, return_train_score=True, cv=10)

        print("CROSS VALIDATION RESULTS (VALIDATION)\t ===> ", cv_score["test_score"].mean())
        print("CROSS VALIDATION RESULTS (TRAIN)\t ===> ", cv_score["train_score"].mean())

        pipeline.fit(X_train, y_train)

        print("---")
        print("FINAL TEST SCORE\t\t\t ===> ", pipeline.score(X_test, y_test))