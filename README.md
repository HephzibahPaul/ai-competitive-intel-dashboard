# 🏁 AI Competitive Intelligence Dashboard (NLP on Reviews)

## 1. Overview

This project is an **AI-powered Competitive Intelligence Dashboard** that uses
**NLP (topic clustering)** on customer reviews to compare **OurBrand** with
competitors.

It is designed from a **Business Analyst** perspective to help:
- Product teams find feature gaps
- Marketing teams understand messaging opportunities
- Strategy teams benchmark against competitors

Built with:
- Python (Pandas, Scikit-Learn)
- TF-IDF + KMeans clustering
- Streamlit for the dashboard UI

---

## 2. Business Problem

Companies get lots of reviews on platforms like Amazon and Google, across
multiple brands and products. Manually reading these:

- Takes too long
- Misses patterns
- Is not scalable

This project answers:
- “What are customers complaining about for each competitor?”
- “On which topics is OurBrand better or worse?”
- “What themes are most important for improvement?”

---

## 3. Data

Synthetic but realistic CSVs in `data/raw`:

- `competitor_products_sample.csv`
  - competitor_name, product_name, category, price, rating, description

- `competitor_reviews_sample.csv`
  - competitor_name, product_name, source, review_text, rating

You can extend these files with more rows to make the analysis richer.

---

## 4. NLP & Modeling Approach

1. **Preprocessing**
   - Lowercasing, removing punctuation
   - Basic normalization → `clean_text`

2. **Vectorization**
   - `TfidfVectorizer` (1–2 word n-grams)
   - max_features = 2000
   - English stopwords

3. **Topic Modeling (Clustering)**
   - `KMeans` with `N_TOPICS = 4`
   - Each review gets a `topic_id`
   - Top keywords per topic → `topic_keywords`

4. **Aggregation**
   - For each `(topic_id, competitor_name)`:
     - `review_count`
     - `avg_rating`

Results saved to:
- `data/processed/reviews_with_topics.csv`
- `data/processed/topic_summary.csv`

---

## 5. Dashboard Features (Streamlit)

Run:

```bash
streamlit run app/app.py
The app has 3 main tabs:

📌 Overview
Total reviews (after filters)

Average rating

Average rating by competitor (table + bar chart)

🧠 Topics & Themes
Topic-wise review counts per competitor

Global list of topics with:

keywords

total review volume

average rating

⚔️ Competitor vs OurBrand
Compare OurBrand vs one competitor on each topic

See topic-wise rating gap:

Positive → OurBrand better

Negative → Competitor better

6. How to Run the Project
1️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
2️⃣ Run NLP pipeline (build topics)
bash
Copy code
python -m src.nlp_analysis
3️⃣ Launch the dashboard
bash
Copy code
streamlit run app/app.py
7. Skills Demonstrated
Designed a competitive intelligence solution using NLP

Implemented text preprocessing, TF-IDF, and KMeans clustering

Aggregated results into topic-level business metrics

Built an interactive Streamlit dashboard for non-technical stakeholders

Interpreted model output into BA-style actionable insights

8. Possible Extensions
Add real (scraped or exported) review data

Use advanced topic modeling (LDA, BERTopic)

Add sentiment analysis per topic

Export automated PDF insight reports