####  ANOMALY DETECTION IN REFEREE DECISIONS (TURKISH SÜPER LIG)

### The objectivity of referee decisions in Turkish football is an arguable point of controversy. This project aimed to scientifically investigate potential biases by combining public match statistics with betting odds data. The final report validates the Referee Performance Index (RPI) and assesses its independence from financial market expectations using Advanced Machine Learning.

***

## Project Description

This project explores the relationship between referee strictness and match anomalies in the Turkish Süper Lig from both a statistical and machine learning perspective. Using multi-season match data, the project investigates how specific referee behaviors (Penalties, Red Cards) influence match outcomes compared to pre-game betting expectations.

We aim to answer the question: **"Is the referee a bigger factor than the betting odds in predicting match deviations?"** To do so, we perform end-to-end data analysis—starting from raw data cleaning and RPI calculation to hypothesis testing and predictive modeling using Random Forest algorithms.

## Motivation

The integrity of refereeing in **Turkish football** has been a subject of intense debate, especially following recent controversial matches and on-field incidents that have sparked public outrage and mistrust. As a data science enthusiast and a passionate follower of the league, I am driven to move beyond subjective arguments and explore this issue using rigorous, data-driven approaches.

This project is motivated by the desire to bring scientific objectivity to this heated topic. By analyzing years of data, I aim to understand if these perceived biases are statistically significant anomalies or simply random variances inherent to the sport.

## Datasets

* **Dataset 1: Match Statistics (Master Data)**
    * **Name:** `master_stats_manual_entry.csv`
    * **Source:** Public Sports Broadcasters / TFF
    * **Data Acquisition Method:** Aggregated from public match logs and manually verified for consistency.

* **Dataset 2: Betting Odds Data**
    * **Name:** `betting_odds_raw.csv`
    * **Source:** Historical Odds Portals
    * **Data Acquisition Method:** Collected historical pre-match odds (Home Win, Draw, Away Win) to establish a baseline for "Expected Points".

## Data Collection and Preparation

### 1. Data Cleaning
* **Score Parsing:** Solved complex string formatting issues (e.g., removing non-numeric characters) to split scores into `Home_Score` and `Away_Score`.
* **Date Standardization:** Converted various date formats into a unified `datetime` object for merging.
* **Filtering:** Removed matches with missing critical data points (e.g., missing odds or unrecorded referee names).

### 2. Aggregation & Integration
* **Merged Datasets:** Combined Master Stats and Betting Odds using `Date` and `Team Names` as composite keys.
* **National Averages:** Calculated league-wide averages for red cards and penalties to establish a baseline.

### 3. Feature Engineering
* **RPI (Referee Performance Index):** Engineered a unique metric to quantify referee strictness.
    * *Formula:* $RPI = (Avg. Red Cards \times 1.0) + (Avg. Penalties \times 0.87)$
* **Anomaly Gap:** Created a feature measuring the difference between **Expected Points** (derived from Betting Odds) and **Actual Points** (Match Result).

## Analysis Plan

### 1. Exploratory Data Analysis (EDA)
* **Distributions:** Visualized the distribution of RPI to identify "Strict" vs. "Lenient" referees.
* **Correlation Heatmaps:** Analyzed relationships between Betting Odds and Referee Decisions.
* **Key Insights:**
    * High-RPI referees tend to be involved in matches with higher volatility.
    * No strong linear correlation exists between betting odds and decision frequency (Correlation $\approx -0.004$).

### 2. Hypothesis Testing
* **Hypothesis:**
    * $H_0$ (Null): There is no statistically significant difference in penalty rates between high-RPI referees and the norm.
    * $H_1$ (Alternative): High-RPI referees award significantly more penalties.
* **Method:** Independent Samples **t-Test**.
* **Results:**
    * **P-value:** $0.00018$ ($< 0.05$)
    * **Conclusion:** Rejected the Null Hypothesis. A specific group of referees statistically deviates from the league average.

## Machine Learning Models

### 1. Classification (Random Forest)
* **Target:** `is_anomaly` (Binary: 1 if Anomaly Gap > 1.2, else 0)
* **Features Used:** Betting Odds (Home/Draw), Referee RPI.
* **Model:** `RandomForestClassifier(n_estimators=100)`
* **Feature Importance Findings:**
    * While Betting Odds are the primary predictor, **Referee RPI** emerged as a significant secondary factor.
    * This suggests that in "surprise" matches, the referee's strictness level plays a measurable role.

### 2. Impact Analysis (Logistic Regression)
* **Target:** `Home_Win`
* **Purpose:** To calculate the weights for the RPI formula.
* **Result:** A Penalty decision has approximately **0.87x** the impact of a Red Card on the immediate match outcome.

## Limitations and Future Work

### Limitations
* **Subjectivity:** The model accounts for the *count* of decisions but cannot evaluate the *correctness* of a call.
* **Scope:** Analysis is limited to the Turkish Süper Lig; patterns may differ in European leagues.

### Future Work
* **Cross-League Analysis:** Apply the RPI model to the Premier League and Bundesliga.
* **VAR Integration:** Incorporate VAR intervention data to distinguish between on-field errors and corrected decisions.
* **Real-time Dashboard:** Develop a web app to flag "High Anomaly Risk" matches live.

## Technology Stack

* **Languages:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SciPy
* **Tools:** Google Colab, Jupyter Notebook, GitHub

## Timeline

| Task | Deadline |
| :--- | :--- |
| **Data Collection & Cleaning** | Oct 3, 2025 |
| **EDA & Hypothesis Testing** | Nov 28, 2025 |
| **Machine Learning Modeling** | Jan 3, 2026 |
| **Final Report Submission** | Jan 09, 2026 |

## Team

* **[Name-Surname]** Ali Baran Altıoğlu
* **Student ID:** 32039
