"""Customer Churn Machine Learning Pipeline.

Implements end-to-end data preprocessing, baseline & advanced classification models,
reproducible held-out evaluation (zero data leakage), and feature importance extraction.
"""

from typing import Dict, Any, Tuple
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

class ChurnPipeline:
    NUMERIC_FEATURES = ['Tenure', 'MonthlyCharges', 'TotalCharges']
    CATEGORICAL_FEATURES = ['Contract', 'TechSupport', 'OnlineSecurity', 'PaymentMethod']
    TARGET = 'Churn'

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.NUMERIC_FEATURES),
                ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), self.CATEGORICAL_FEATURES)
            ]
        )
        self.log_reg = LogisticRegression(random_state=self.random_state, max_iter=500)
        self.rf = RandomForestClassifier(n_estimators=30, max_depth=5, random_state=self.random_state, n_jobs=1)
        self.is_fitted = False
        self.feature_names = []

    def load_data(self, csv_path: str) -> pd.DataFrame:
        df = pd.read_csv(csv_path)
        required = set(self.NUMERIC_FEATURES + self.CATEGORICAL_FEATURES + [self.TARGET])
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns in dataset: {missing}")
        return df

    def split_data(self, df: pd.DataFrame, test_size: float = 0.25) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        X = df[self.NUMERIC_FEATURES + self.CATEGORICAL_FEATURES]
        y = df[self.TARGET]
        return train_test_split(X, y, test_size=test_size, random_state=self.random_state, stratify=y)

    def fit_and_train(self, X_train: pd.DataFrame, y_train: pd.Series):
        """Fit preprocessor strictly on training data (guaranteeing zero data leakage)."""
        X_train_trans = self.preprocessor.fit_transform(X_train)

        # Extract encoded feature names
        cat_encoder = self.preprocessor.named_transformers_['cat']
        encoded_cat = cat_encoder.get_feature_names_out(self.CATEGORICAL_FEATURES)
        self.feature_names = list(self.NUMERIC_FEATURES) + list(encoded_cat)

        self.log_reg.fit(X_train_trans, y_train)
        self.rf.fit(X_train_trans, y_train)
        self.is_fitted = True

    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> Dict[str, Dict[str, Any]]:
        """Evaluate both models on held-out test data."""
        if not self.is_fitted:
            raise RuntimeError("Pipeline must be fitted before evaluation.")

        X_test_trans = self.preprocessor.transform(X_test)
        results = {}

        for name, model in [('Logistic Regression (Baseline)', self.log_reg), ('Random Forest (Classification)', self.rf)]:
            y_pred = model.predict(X_test_trans)
            y_proba = model.predict_proba(X_test_trans)[:, 1]

            results[name] = {
                'accuracy': round(accuracy_score(y_test, y_pred), 4),
                'precision': round(precision_score(y_test, y_pred, zero_division=0), 4),
                'recall': round(recall_score(y_test, y_pred, zero_division=0), 4),
                'f1_score': round(f1_score(y_test, y_pred, zero_division=0), 4),
                'roc_auc': round(roc_auc_score(y_test, y_proba), 4),
                'confusion_matrix': confusion_matrix(y_test, y_pred).tolist(),
            }

        return results

    def get_feature_importances(self) -> pd.DataFrame:
        if not self.is_fitted:
            raise RuntimeError("Pipeline must be fitted before extracting feature importances.")
        importances = self.rf.feature_importances_
        df_imp = pd.DataFrame({
            'Feature': self.feature_names,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False).reset_index(drop=True)
        return df_imp
