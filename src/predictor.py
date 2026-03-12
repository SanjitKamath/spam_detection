"""
Spam Prediction Engine
======================
"""

import joblib
import numpy as np

from src.nlp_features import transform_text
from src.url_features import url_feature_vector
from src.reputation import domain_reputation

MODEL_PATH = "models/spam_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_spam(text):

    tfidf = transform_text(text).toarray()

    url_features = np.array(url_feature_vector(text)).reshape(1,-1)

    reputation = np.array([[domain_reputation(text)]])

    combined = np.hstack((tfidf,url_features,reputation))

    prediction = model.predict(combined)[0]

    probability = model.predict_proba(combined)[0][1]

    return {
        "prediction": "spam" if prediction else "not_spam",
        "confidence": float(probability)
    }