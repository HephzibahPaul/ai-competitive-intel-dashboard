🏁 AI Competitive Intelligence Dashboard
NLP-Driven Review Analytics for Product, Marketing & Strategy Teams

This project delivers an AI-powered Competitive Intelligence system that analyzes customer reviews using TF-IDF vectorization + KMeans clustering and presents insights through an interactive Streamlit dashboard.

Designed from a Business Analyst viewpoint, the project identifies customer pain points, feature gaps, and competitor strengths to support data-driven decision-making.

🚀 1. Project Overview

Modern organizations collect thousands of customer reviews across digital platforms. Manually reading these reviews is:

Time-consuming

Prone to bias

Unscalable

Ineffective for extracting hidden themes

This project automates review analysis to provide:

Topic-based insights

Competitor comparison

Customer sentiment patterns

Feature improvement opportunities

🎯 2. Business Value

The dashboard enables teams to:

Product Teams

Identify recurring issues

Detect feature gaps across competitors

Marketing & CX Teams

Understand customer expectations

Compare sentiment trends across brands

Strategy Teams

Benchmark performance against competitors

Uncover competitive advantages/disadvantages

🧠 3. Techniques & Tools Used
Technical Stack

Python

Pandas

NumPy

Scikit-Learn

TF-IDF Vectorizer

KMeans Clustering

Streamlit (Dashboard UI)

NLP Methods

Text preprocessing

Stopword removal

TF-IDF feature extraction

Topic modeling (KMeans)

📊 4. Data Sources

Located in data/raw/:

competitor_products_sample.csv
competitor_name, product_name, category, price, rating, description

competitor_reviews_sample.csv
competitor_name, product_name, source, review_text, rating

Pipeline Outputs

(Generated after running NLP pipeline)

data/processed/reviews_with_topics.csv

data/processed/topic_summary.csv

🧩 5. NLP Pipeline Workflow
Step 1 — Preprocessing

Lowercase transformation

Punctuation removal

Stopword removal

Clean text stored as clean_text

Step 2 — Vectorization

TF-IDF with bi-grams

2000 max features

Step 3 — Topic Modeling

KMeans with 4 clusters

Extracts top keywords per topic

Each review assigned a topic_id

Step 4 — Aggregation

Topic-wise review clustering

Topic average ratings

Competitor-topic distribution

All results are saved as processed CSV files.

🖥️ 6. Dashboard Features (Streamlit)
📌 Overview

Total number of reviews

Average rating

Competitor rating comparison

🧠 Topics & Themes

Topic keywords

Topic volumes

Topic-level average ratings

Competitor distribution across topics

⚔️ Competitor vs OurBrand

Topic-wise rating gap

Areas where competitors perform better

Areas where OurBrand leads

🛠️ 7. How to Run the Project
Install all dependencies
pip install -r requirements.txt

Run NLP pipeline
python -m src.nlp_analysis

Launch dashboard
streamlit run app/app.py

## 📁 8. Project Structure

```bash
ai-competitive-intel-dashboard/
│
├── app/
│   └── app.py                    # Streamlit dashboard application
│
├── data/
│   ├── raw/                      # Original input CSVs
│   │   ├── competitor_products_sample.csv
│   │   └── competitor_reviews_sample.csv
│   └── processed/                # Generated NLP outputs
│       ├── reviews_with_topics.csv
│       └── topic_summary.csv
│
├── src/
│   ├── config.py                 # Global configurations
│   ├── nlp_utils.py              # NLP preprocessing helpers
│   └── nlp_analysis.py           # NLP + topic modeling pipeline
│
├── screenshots/                  # Optional documentation images
├── requirements.txt
├── LICENSE
└── README.md

💡 9. Skills Demonstrated
Technical Skills

NLP (TF-IDF, KMeans)

Text preprocessing

Feature extraction

Data cleaning and transformation

Dashboard development with Streamlit

Business Analysis Skills

Competitive intelligence

Customer pain point identification

Topic-based review interpretation

Insight summarization

Dashboard storytelling for stakeholders

10. Author

Hephzibah Paul
Business Analyst | AI & Data Analytics
GitHub: https://github.com/HephzibahPaul