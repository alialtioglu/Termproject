FINAL PROJECT REPORT: ANOMALY DETECTION IN REFEREE DECISIONS
The objectivity of referee decisions in football is an arguable point of controversy. This project aimed to scientifically investigate potential biases by combining public match statistics with betting odds data. The final report validates the Referee Performance Index (RPI) and assesses its independence from financial market expectations.
1. Core Data and Feature Engineering
Core Data (Strict Data Inventory)
The analysis used match records from five seasons of the Turkish Süper Lig, including:

Match identifiers: Home/Away Teams and the Referee's name.

The primary outcome variables (decisions used for analysis): Red Cards and Penalties awarded per match.

Final RPI Formula (Statistically Justified)
The RPI was designed to quantify a referee's critical decision tendency. The final formula was justified by a Logistic Regression model showing a Penalty decision has 0.87 times the impact of a Red Card decision on the match outcome.

RPI=(Avg. Red Cards×1.0)+(Avg. Penalties×0.87)
2. Statistical Proof and Hypothesis Test
Hypothesis Tested (t-Test)
The project tested whether the RPI successfully identifies groups of referees with statistically different penalty rates.

Null Hypothesis (H 
0
​
 ): There is no statistically significant difference in the average penalty rate per match between high-RPI referees and low-RPI referees.

t-Test Results (Scientific Validation)
The Independent Samples t-Test on the final adjusted data yielded the following results:

Metric	High RPI Group Avg. Penalty	Normal RPI Group Avg. Penalty	P-Value	Conclusion
Result	0.4286	0.2769	0.00018468	H 
0
​
  Rejected

Export to Sheets

Conclusion: The P-Value is significantly less than 0.05. This proves that the RPI successfully isolates a group of referees with a measurably higher propensity for awarding penalties.

3. Analytical Findings
3.1. Decision Frequency Analysis (Highest Prone Teams)
This section reports contextual findings based on raw frequency averages:

Highest Penalty Conceded Average: [Insert Name of Team with Highest Penalty Conceded Avg.]

Highest Red Card Average: [Insert Name of Team with Highest Red Card Avg.]

Referee Tendency: The analysis confirmed that high-RPI referees have a statistically significant higher average penalty rate than the normal group.

3.2. Betting Odds Impact (Financial Link)
The correlation analysis provided the link between referee decisions and the financial market expectation:

Penaltı Kararları vs. Home Win Odds Korelasyonu: -0.0047

Kırmızı Kart Kararları vs. Home Win Odds Korelasyonu: +0.0635

Conclusion: The analysis found no strong linear relationship between betting market expectations and the frequency of critical referee decisions.

4. Future Work: Machine Learning and Anomaly Detection (02 January Deliverable)
The next phase of the project will shift from statistical validation to predictive modeling, using the engineered features to identify specific suspicious matches.

4.1. Anomaly Detection Goal
The objective is to flag matches where the final outcome (or a critical decision) significantly deviates from the prediction made by the model.

4.2. Machine Learning Method
Prediction Model: A classification algorithm (e.g., Logistic Regression or Random Forest) will be used to predict the probability of the Home Win based on Betting Odds (market expectation) and RPI (referee tendency).

Anomaly Flagging: Matches where the predicted outcome probability is high, but the actual outcome is a loss due to a late critical decision, will be flagged as anomalies.

5. Code and Reproducibility
Language: All code is written in Python.

Dependencies: Listed in requirements.txt.

Code Location: All final processing, cleaning, RPI calculation, and hypothesis testing scripts are located in the /scripts folder.

Final Data: The clean, processed data is stored in the /data/processed folder.
