Anladım. **3.2. Decision Frequency Analysis** bölümünü atlayarak ve kalan kısımların akışını koruyarak son, akademik `README.md` dosyanızı hemen hazırlıyorum.

Bu dosya, bireysel takım istatistiklerinden ziyade, **metodolojik ve istatistiksel kanıt** üzerine odaklanır.

---

# 📝 FINAL PROJECT REPORT: ANOMALY DETECTION IN REFEREE DECISIONS

### The objectivity of referee decisions in football is an arguable point of controversy. This project aimed to scientifically investigate potential biases by combining public match statistics with betting odds data. The final report validates the Referee Performance Index (RPI) and assesses its independence from financial market expectations.

***

## 1. Core Data and Feature Engineering (Originality & Quality)

### Core Data (Strict Data Inventory)
The analysis used match records from five seasons of the Turkish Süper Lig, including:
* Match identifiers: **Home/Away Teams** and the **Referee's name**.
* The primary outcome variables (decisions used for analysis): **Red Cards** and **Penalties** awarded per match.

### Final RPI Formula (Statistically Justified)
The RPI was designed to quantify a referee's critical decision tendency, serving as the project's **main original feature**. The final formula was justified by a Logistic Regression model showing a Penalty decision has $\mathbf{0.87}$ times the impact of a Red Card decision on the match outcome.

$$\text{RPI} = (\text{Avg. Red Cards} \times 1.0) + (\text{Avg. Penalties} \times 0.87)$$

***

## 2. Statistical Proof and Hypothesis Test (Scientific Method)

### Hypothesis Tested ($t$-Test)
The project tested whether the RPI successfully isolates groups of referees with statistically different penalty rates.
* **Null Hypothesis ($H_0$):** There is **no** statistically significant difference in the average penalty rate per match between high-RPI referees and low-RPI referees.

### $t$-Test Results (Scientific Validation)
The Independent Samples $t$-Test on the final adjusted data yielded the following results:

| Metric | High RPI Group Avg. Penalty | Normal RPI Group Avg. Penalty | P-Value | Conclusion |
| :--- | :---: | :---: | :---: | :--- |
| **Result** | $\mathbf{0.4286}$ | $\mathbf{0.2769}$ | $\mathbf{0.00018468}$ | $H_0$ Rejected |

**Conclusion:** The P-Value is significantly less than 0.05. This **rejects the Null Hypothesis** and proves that the RPI successfully isolates a group of referees with a measurably higher propensity for awarding penalties.

***

## 3. Analytical Findings (Final Report)

### 3.1. Betting Odds Impact (Financial Link)
The analysis assessed the influence of the **Betting Odds (Financial Indicator)** on decision frequency:

* **Penaltı Kararları vs. Home Win Odds Korelasyonu:** **-0.0047**
* **Kırmızı Kart Kararları vs. Home Win Odds Korelasyonu:** **+0.0635**
* **Conclusion:** The analysis found **no strong linear relationship** between betting market expectations and the frequency of critical referee decisions.

***

## 4. Future Work: Machine Learning and Anomaly Detection (02 January Deliverable)

### 4.1. Anomaly Detection Goal
The next phase will shift from statistical validation to predictive modeling, using the engineered features to identify specific suspicious matches.

### 4.2. Machine Learning Method
* **Prediction Model:** A classification algorithm (e.g., **Logistic Regression** or **Random Forest**) will be used to predict the probability of the *Home Win* based on **Betting Odds** and **RPI**.
* **Anomaly Flagging:** Matches where the predicted outcome probability is high, but the actual outcome is a loss due to a late critical decision, will be flagged as anomalies.

***

## 5. Code and Reproducibility

* **Language:** All code is written in **Python**.
* **Dependencies:** Listed in `requirements.txt`.
* **Code Location:** All final processing, cleaning, RPI calculation, and hypothesis testing scripts are located in the `/scripts` folder.
* **Final Data:** The clean, processed data is stored in the `/data/processed` folder.
* 
