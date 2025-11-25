import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

from src.config import (

    REVIEWS_RAW, REVIEWS_PROCESSED, TOPIC_SUMMARY,
    TOPIC_MODEL_PATH, RANDOM_STATE, N_TOPICS,
    TEXT_COL, COMP_COL, RATING_COL
)
from src.utils import basic_clean

def load_reviews():
    """Load raw reviews and add a clean_text column."""
    df = pd.read_csv(REVIEWS_RAW)
    df[TEXT_COL] = df[TEXT_COL].fillna("").astype(str)
    df["clean_text"] = df[TEXT_COL].apply(basic_clean)
    return df

def build_topic_model(df):
    """Fit TF-IDF + KMeans topic model and assign topic_id to each review."""
    vectorizer = TfidfVectorizer(
        max_features=2000,
        stop_words="english",
        ngram_range=(1, 2)
    )
    X = vectorizer.fit_transform(df["clean_text"])

    kmeans = KMeans(
        n_clusters=N_TOPICS,
        random_state=RANDOM_STATE,
        n_init=10
    )
    df["topic_id"] = kmeans.fit_predict(X)

    TOPIC_MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {"vectorizer": vectorizer, "kmeans": kmeans},
        TOPIC_MODEL_PATH
    )

    return df

def summarize_topics(df):
    """Create topic keywords and summary metrics by topic + competitor."""
    bundle = joblib.load(TOPIC_MODEL_PATH)
    vectorizer = bundle["vectorizer"]
    kmeans = bundle["kmeans"]

    terms = vectorizer.get_feature_names_out()
    topic_keywords = []
    for topic_idx, center in enumerate(kmeans.cluster_centers_):
        top_idx = center.argsort()[::-1][:8]
        top_terms = [terms[i] for i in top_idx]
        topic_keywords.append(", ".join(top_terms))

    topic_map = {i: kw for i, kw in enumerate(topic_keywords)}
    df["topic_keywords"] = df["topic_id"].map(topic_map)

    topic_summary = (
        df.groupby(["topic_id", "topic_keywords", COMP_COL])
          .agg(
              review_count=("clean_text", "count"),
              avg_rating=(RATING_COL, "mean")
          )
          .reset_index()
    )

    REVIEWS_PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(REVIEWS_PROCESSED, index=False)
    topic_summary.to_csv(TOPIC_SUMMARY, index=False)

    return df, topic_summary

def main():
    print("Loading reviews...")
    df = load_reviews()
    print(f"Loaded {len(df)} reviews")

    print("Building topic model...")
    df = build_topic_model(df)

    print("Summarising topics...")
    df, topic_summary = summarize_topics(df)

    print(f"Saved processed reviews to {REVIEWS_PROCESSED}")
    print(f"Saved topic summary to {TOPIC_SUMMARY}")
    print("Done ✅")

if __name__ == "__main__":
    main()
