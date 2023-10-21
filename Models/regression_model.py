from typing import List
from ranking_model_interface import Ranking_Model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import matplotlib.pyplot as plt
import seaborn as sns

class RegressionModel(Ranking_Model):
    def __init__(self):
        self.model = LogisticRegression(max_iter=10000, C=0.01, penalty='l2') # l2 regularization
        self.scaler = StandardScaler() # init scaler

        X_train, X_val, y_train, y_val = super().get_training_test_datasets()

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
        grid_search = GridSearchCV(self.model, param_grid, cv=10, scoring='accuracy', n_jobs=-1) # n_jobs=-1 uses all cores
        grid_search.fit(self.X_train, self.y_train)
        # update the model with best found parameters
        self.model = grid_search.best_estimator_
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best cross-validation score: {grid_search.best_score_}")

  

    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self, X=None):
        if X is None:
            X = self.X_val
        else:
            X = self.scaler.transform(X)
        return self.model.predict(X)

    def evaluate(self):
        y_pred = self.predict()
        accuracy = accuracy_score(self.y_val, y_pred)
        report = classification_report(self.y_val, y_pred)

        # confusion matrix -- uncomment for visualization
        # y_prob = self.model.predict_proba(self.X_val)[:, 1] # probabilities for the positive class in ROC curve visualization
        # cm = confusion_matrix(self.y_val, y_pred)
        # sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        # plt.xlabel('Predicted labels')
        # plt.ylabel('True labels')
        # plt.title('Confusion Matrix')
        # plt.show()

        # ROC curve -- uncomment for visualization
        # fpr, tpr, _ = roc_curve(self.y_val, y_prob)
        # roc_auc = auc(fpr, tpr)
        # plt.figure()
        # plt.plot(fpr, tpr, color='darkorange', label=f'ROC curve (area = {roc_auc:.2f})')
        # plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
        # plt.xlabel('False Positive Rate')
        # plt.ylabel('True Positive Rate')
        # plt.title('Receiver Operating Characteristic (ROC) Curve')
        # plt.legend(loc="lower right")   
        # plt.show()

        print(f"Accuracy: {accuracy}")
        print(report)

  
    def get_global_rankings(self, n_teams: int = 20) -> List[dict]:
        return super().get_global_rankings(n_teams)
    
    def get_tournament_rankings(self, tournament_id: str, stage: str) -> List[dict]:
        return super().get_tournament_rankings(tournament_id, stage)
    
    def get_custom_rankings(self, teams: dict) -> List[dict]:
        return super().get_custom_rankings(teams)
  
  

model = RegressionModel()
model.tune_hyperparameters()
model.train()
model.cross_validate() # 10 fold CV
model.predict()
model.evaluate()