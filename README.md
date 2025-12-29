#### FINAL PROJECT REPORT: ANOMALY DETECTION IN REFEREE DECISIONS (TURKISH SÜPER LIG)

### The objectivity of referee decisions in Turkish football is an arguable point of controversy. This project aimed to scientifically investigate potential biases by combining public match statistics with betting odds data. The final report validates the Referee Performance Index (RPI) and assesses its independence from financial market expectations using Advanced Machine Learning.

***

## 1. MOTIVATION

### The "Why" Behind The Analysis
The integrity of refereeing in **Turkish football** has been a subject of intense debate, especially following recent controversial matches and on-field incidents that have sparked public outrage and mistrust. As a data science enthusiast and a passionate follower of the league, I am driven to move beyond subjective arguments and explore this issue using rigorous, data-driven approaches.

### Goal
This project is motivated by the desire to bring scientific objectivity to this heated topic. By analyzing years of data, I aim to answer: **"Is the referee a bigger factor than the betting odds in predicting match deviations?"**

***

## 2. CORE DATA AND FEATURE ENGINEERING

### Core Data (Strict Data Inventory)
The analysis used match records from five seasons of the Turkish Süper Lig, including:
* Match identifiers: **Home/Away Teams**, **Date**, and the **Referee's name**.
* The primary outcome variables (decisions used for analysis): **Red Cards** and **Penalties** awarded per match.
* **Financial Data:** Historical Pre-match Betting Odds (Home Win, Draw, Away Win).

### Final RPI Formula (Statistically Justified)
The RPI was designed to quantify a referee's critical decision tendency, serving as the project's **main original feature**. The final formula was justified by a Logistic Regression model showing a Penalty decision has $\mathbf{0.87}$ times the impact of a Red Card decision on the match outcome.

$$\text{RPI} = (\text{Avg. Red Cards} \times 1.0) + (\text{Avg. Penalties} \times 0.87)$$

***

## 3. STATISTICAL PROOF AND HYPOTHESIS TEST

### Hypothesis Tested ($t$-Test)
The project tested whether the RPI successfully isolates groups of referees with statistically different penalty rates.
* **Null Hypothesis ($H_0$):** There is **no** statistically significant difference in the average penalty rate per match between high-RPI referees and low-RPI referees.

### $t$-Test Results (Scientific Validation)
The Independent Samples $t$-Test on the final adjusted data yielded the following results:

| Metric | High RPI Group Avg. Penalty | Normal RPI Group Avg. Penalty | P-Value | Conclusion |
| :--- | :---: | :---: | :---: | :--- |
| **Result** | $\mathbf{0.4286}$ | $\mathbf{0.2769}$ | $\mathbf{0.00018}$ | $H_0$ Rejected |

**Conclusion:** The P-Value is significantly less than 0.05. This **rejects the Null Hypothesis** and proves that the RPI successfully isolates a group of referees with a measurably higher propensity for awarding penalties.

***

## 4. ANALYTICAL FINDINGS & AI MODELING

### 4.1. Betting Odds Impact (Financial Link)
The analysis assessed the influence of the **Betting Odds (Financial Indicator)** on decision frequency:
* **Penalties vs. Odds Correlation:** **-0.0047** (Extremely Weak)
* **Conclusion:** The analysis found **no strong linear relationship** between betting market expectations and the frequency of critical referee decisions.

### 4.2. Advanced AI Analysis (Random Forest)
We deployed a **Random Forest Classifier** to predict match anomalies (unexpected losses).
* **Objective:** To determine Feature Importance.
* **Findings:** While Betting Odds are the primary predictor, **Referee RPI** emerged as a significant secondary factor. This proves that in high-volatility matches, referee strictness plays a measurable role that the market does not fully account for.

***

## 5. FUTURE WORK AND EXPANSION

### 5.1. Cross-League Analysis
The current RPI metric is calibrated solely for Turkish football. Future iterations will apply this model to the **English Premier League (EPL)** and **Bundesliga** to benchmark Turkish referees against European standards.

### 5.2. VAR Integration
Future work involves scraping **VAR (Video Assistant Referee)** intervention data to distinguish between "corrected" errors and subjective on-field calls.

***

## 6. CODE AND REPRODUCIBILITY

* **Language:** All code is written in **Python**.
* **Dependencies:** Listed in `requirements.txt`.
* **Code Location:** All final processing, cleaning, RPI calculation, and Machine Learning scripts are located in the `/Scripts` folder (File: `DSA210_Final_Analysis_with_AI.ipynb
