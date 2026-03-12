"""
Spam Detection Model Trainer
============================
Combines NLP + URL features.
"""

import pandas as pd
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from scipy.sparse import csr_matrix, hstack

from src.nlp_features import train_vectorizer
from src.url_features import url_feature_vector
from src.reputation import domain_reputation

MODEL_PATH = "models/spam_model.pkl"


def build_features(df):

    text_features = train_vectorizer(df["text"])

    extra_features = []

    for text in df["text"]:

        url_features = url_feature_vector(text)
        reputation = domain_reputation(text)

        extra_features.append(url_features + [reputation])

    extra_features = csr_matrix(np.array(extra_features))
    
    combined = hstack([text_features, extra_features])

    return combined


def train(dataset_path):

    df = pd.read_csv(dataset_path)

    X = build_features(df)

    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )

    model.fit(X_train,y_train)

    joblib.dump(model, MODEL_PATH)

    print("Model trained and saved.")


if __name__ == "__main__":

    train("data/spam_dataset.csv")