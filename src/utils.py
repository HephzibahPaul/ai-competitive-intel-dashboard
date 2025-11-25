import re
import pandas as pd

def basic_clean(text: str) -> str:
    """Basic text cleaning: lowercase, remove non-alphanumeric, normalize spaces."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def load_csv(path):
    return pd.read_csv(path)
