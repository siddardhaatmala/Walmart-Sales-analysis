
---

# Walmart Sales — SQL Exploratory Data Analysis

## Project Overview

This project performs an end-to-end exploratory data analysis (EDA) on Walmart's historical store sales data spanning 2010 to 2012. Utilizing a robust data pipeline, raw CSV data is transferred into a PostgreSQL database via SQLAlchemy and subsequently analyzed using pandas, matplotlib, and seaborn in a Python environment. The analysis uncovers critical trends across stores, departments, and store categories to drive optimal operational and inventory decisions.

**Author:** siddardha atmala

**Dataset Size:** ~421K records across 45 stores

---

## Repository Structure & Core Files

This project relies on four core data files, which must be referenced and positioned exactly as follows:

* `train.csv`: The historical training dataset containing sales records from 2010 to 2012.
* `test.csv`: The testing dataset used to validate predictive sales models.
* `stores.csv`: Metadata containing information regarding the 45 anonymized stores, including store `Type` and `Size`.
* `features.csv`: Supplemental engine details containing regional environmental data (e.g., Temperature, Fuel Price, Markdown clearances, CPI, Unemployment rates) matching the specific timeframes.

---

## Data Pipeline & Architecture

The workflow moves data dynamically from flat files to a relational database framework to optimize query performance and scalable analysis.

```python
from sqlalchemy import create_engine
import pandas as pd

# Database initialization
SQLALCHEMY_DATABASE_URL = f"postgresql://{input('Enter Username:')}:{input('Enter Password:')}@localhost:5432/Project1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Extraction
features_df = pd.read_csv("data/features.csv")
test_df = pd.read_csv("data/test.csv")
stores_df = pd.read_csv("data/stores.csv")
train_df = pd.read_csv('data/train.csv')

# Load phase into PostgreSQL
features_df.to_sql('raw_features', engine, if_exists='replace', index=False)
test_df.to_sql('test_data', engine, if_exists='replace', index=False)
stores_df.to_sql('stores', engine, if_exists='replace', index=False)
train_df.to_sql('train_data', engine, if_exists='replace', index=False)

```

---

## Key Business Insights & Analytical Findings

Following data aggregation and merging, deep SQL queries revealed fundamental drivers behind Walmart's performance:

### 1. Store Revenue Performance

Analysis of overall revenue mapped the core engines of Walmart's financial success. Store 20 sits at the peak, generating **$301.39M** in total revenue, followed tightly by Store 4 (**$299.54M**) and Store 14 (**$288.99M**).

| Rank | Store ID | Total Revenue ($) | Performance Bracket |
| --- | --- | --- | --- |
| 1 | 20 | 301,397,792.46 | Top 5
| 2 | 4 | 299,543,953.38 | Top 5
| 3 | 14 | 288,999,911.34 | Top 5
| 4 | 13 | 286,517,703.80 | Top 5
| 5 | 2 | 275,382,440.98 | Top 5
| ... | ... | ... | ... |
| 41 | 38 | 55,159,626.42 | Bottom 5
| 42 | 36 | 53,412,214.97 | Bottom 5
| 43 | 5 | 45,475,688.90 | Bottom 5
| 44 | 44 | 43,293,087.84 | Bottom 5
| 45 | 33 | 37,160,221.96 | Bottom 5

### 2. Strategic Department Priorities

Specific internal departments drive a disproportionate volume of capital. Department **92** leads individual performance rankings with a total of **$483.94M**. Department **95** lands closely behind with **$449.32M**, and Department **38** claims **$393.12M**. Inventory replenishment algorithms and floor space allocations should heavily favor these high-converting sectors.

### 3. Store Type Discrepancies

Macro divisions based on store types outline structural advantages:

* **Type A** stores stand out significantly, yielding an average weekly sales revenue of **20,099.57**.


* This performance vastly outpaces **Type B** by **64.2%** and **Type C** locations by **111.1%**.



---

## Technical Stack & Tools

* **Database Engine:** PostgreSQL
* **Database Connectivity:** SQLAlchemy, psycopg2


* **Data Aggregation:** Pandas


* **Visualization Suite:** Seaborn, Matplotlib



## How to Get Started

1. Ensure a local instance of PostgreSQL is active and a target database named `Project1` is created.


2. Organize files within a directory hierarchy matching `data/features.csv`, `data/test.csv`, `data/stores.csv`, and `data/train.csv`.


3. Run your data ingestion script to migrate records securely into your schema environment.


4. Access the analytical execution suite inside your Jupyter IDE environment to inspect analytical charts and query sets.
