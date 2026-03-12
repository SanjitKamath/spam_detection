"""
NLP Feature Extraction
======================

Uses TF-IDF vectorization to convert email text
into numerical features suitable for ML models.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


def train_vectorizer(texts):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000,
        ngram_range=(1,2)
    )

    X = vectorizer.fit_transform(texts)

    joblib.dump(vectorizer, VECTORIZER_PATH)

    return X


def load_vectorizer():

    return joblib.load(VECTORIZER_PATH)


def transform_text(text):

    vectorizer = load_vectorizer()

    return vectorizer.transform([text])