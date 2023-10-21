import numpy as np
import tensorflow as tf
import keras
from keras import layers
from ranking_model_interface import Ranking_Model
from sklearn.preprocessing import StandardScaler
from typing import List
from sklearn.model_selection import StratifiedKFold, cross_val_score

class DeepNNModel(Ranking_Model):
    def __init__(self):
        self.scaler = StandardScaler()
        X_train, X_val, y_train, y_val = super().get_training_test_datasets()
        input_dim = X_train.shape[1]

        self.X_train = self.scaler.fit_transform(X_train)
        self.X_val = self.scaler.transform(X_val)
        self.y_train = y_train
        self.y_val = y_val
        self.model = keras.Sequential([
            layers.Input(shape=(input_dim,)),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.2),
            layers.Dense(64, activation='relu'),
            layers.Dropout(0.2),
            layers.Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, epochs=10, batch_size=32):
        self.model.fit(self.X_train, self.y_train, validation_data=(self.X_val, self.y_val), epochs=epochs, batch_size=batch_size)

    def predict(self, X=None):
        if X is None:
            X = self.X_val
        else:
            X = self.scaler.transform(X)
        y_pred = self.model.predict(X)
        return np.round(y_pred)

    def evaluate(self):
        loss, accuracy = self.model.evaluate(self.X_val, self.y_val)
        print(f"Validation Loss: {loss}")
        print(f"Validation Accuracy: {accuracy}")

  

    def cross_validate(self, cv=10):
        skf = StratifiedKFold(n_splits=cv)
        scores = cross_val_score(self.model, self.X_train, self.y_train, cv=skf, scoring='accuracy')
        print(f"Cross-validation scores: {scores}")
        print(f"Average accuracy: {scores.mean()} ± {scores.std()}")

    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        return super().get_global_rankings(n_teams)
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        return super().get_tournament_rankings(tournament_id, stage)
    
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        return super().get_custom_rankings(teams)

  

model = DeepNNModel()
model.train()
#model.cross_validate() # 10 fold CV
model.predict()
model.evaluate()