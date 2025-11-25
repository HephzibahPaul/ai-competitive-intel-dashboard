from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROC_DIR = DATA_DIR / "processed"

PRODUCTS_RAW = RAW_DIR / "competitor_products_sample.csv"
REVIEWS_RAW = RAW_DIR / "competitor_reviews_sample.csv"

REVIEWS_PROCESSED = PROC_DIR / "reviews_with_topics.csv"
TOPIC_SUMMARY = PROC_DIR / "topic_summary.csv"

MODEL_DIR = BASE_DIR / "models"
TOPIC_MODEL_PATH = MODEL_DIR / "kmeans_topics.pkl"

RANDOM_STATE = 42
N_TOPICS = 4
TEXT_COL = "review_text"
COMP_COL = "competitor_name"
RATING_COL = "rating"
