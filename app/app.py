import streamlit as st
import pandas as pd
from pathlib import Path

# ---------- Paths ----------
BASE_DIR = Path(__file__).resolve().parents[1]
PROC_DIR = BASE_DIR / "data" / "processed"

REVIEWS_PROCESSED = PROC_DIR / "reviews_with_topics.csv"
TOPIC_SUMMARY = PROC_DIR / "topic_summary.csv"

st.set_page_config(
    page_title="AI Competitive Intelligence Dashboard",
    layout="wide"
)

@st.cache_data
def load_data():
    reviews = pd.read_csv(REVIEWS_PROCESSED)
    topics = pd.read_csv(TOPIC_SUMMARY)
    return reviews, topics

st.title("🏁 AI Competitive Intelligence Dashboard")
st.caption("Compare competitors using NLP on customer reviews – from a Business Analyst perspective.")

reviews_df, topic_df = load_data()

competitors = sorted(reviews_df["competitor_name"].unique())
our_brand_name = "OurBrand"  # make sure this exists in the CSV

with st.sidebar:
    st.header("Filters")
    selected_competitors = st.multiselect(
        "Select competitors",
        options=competitors,
        default=competitors
    )
    min_rating, max_rating = st.slider(
        "Filter by review rating",
        1.0, 5.0, (1.0, 5.0), step=0.5
    )

filtered_reviews = reviews_df[
    (reviews_df["competitor_name"].isin(selected_competitors)) &
    (reviews_df["rating"].between(min_rating, max_rating))
]

tab1, tab2, tab3 = st.tabs([
    "📌 Overview",
    "🧠 Topics & Themes",
    "⚔️ Competitor vs Our Brand"
])

# ---------- TAB 1: Overview ----------
with tab1:
    st.subheader("Market Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Reviews (filtered)", len(filtered_reviews))
    with col2:
        avg_rating = filtered_reviews["rating"].mean() if len(filtered_reviews) else 0
        st.metric("Average Rating (filtered)", f"{avg_rating:.2f}")

    st.write("Average rating by competitor:")
    avg_by_comp = (
        filtered_reviews.groupby("competitor_name")["rating"]
        .mean()
        .reset_index()
        .sort_values("rating", ascending=False)
    )
    st.dataframe(avg_by_comp)

    if not avg_by_comp.empty:
        st.bar_chart(avg_by_comp.set_index("competitor_name"))

# ---------- TAB 2: Topics & Themes ----------
with tab2:
    st.subheader("Topics & Themes from Reviews")

    topics_filtered = topic_df[topic_df["competitor_name"].isin(selected_competitors)]

    st.write("Topic summary (by competitor):")
    st.dataframe(topics_filtered)

    global_topics = (
        topics_filtered.groupby(["topic_id", "topic_keywords"])
        .agg(
            total_reviews=("review_count", "sum"),
            avg_rating=("avg_rating", "mean")
        )
        .reset_index()
        .sort_values("total_reviews", ascending=False)
    )

    st.write("Global topic importance across all selected competitors:")
    st.dataframe(global_topics)

    if not global_topics.empty:
        st.bar_chart(
            global_topics.set_index("topic_keywords")[["total_reviews"]]
        )

# ---------- TAB 3: Gap Analysis ----------
with tab3:
    st.subheader("Competitor vs Our Brand (Gap Analysis)")

    if our_brand_name not in competitors:
        st.warning(f"Our brand '{our_brand_name}' not found in data. Add it in competitor_reviews_sample.csv.")
    else:
        comp_selected = st.selectbox(
            "Select competitor to compare with OurBrand",
            [c for c in competitors if c != our_brand_name]
        )

        topic_subset = topic_df[
            topic_df["competitor_name"].isin([our_brand_name, comp_selected])
        ]

        pivot = (
            topic_subset
            .pivot_table(
                index=["topic_id", "topic_keywords"],
                columns="competitor_name",
                values="avg_rating"
            )
            .reset_index()
        )

        st.write("Topic-level rating comparison:")
        st.dataframe(pivot)

        if our_brand_name in pivot.columns and comp_selected in pivot.columns:
            pivot["rating_gap"] = pivot[our_brand_name] - pivot[comp_selected]
            st.write("Positive gap = OurBrand better; Negative gap = Competitor better")
            st.dataframe(pivot[["topic_keywords", our_brand_name, comp_selected, "rating_gap"]])

            st.bar_chart(
                pivot.set_index("topic_keywords")[["rating_gap"]]
            )
        else:
            st.info("Need both OurBrand and competitor ratings to compute gaps.")
