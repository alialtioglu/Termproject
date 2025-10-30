# Anomaly Detection in Football Referee Decisions
The objectivity of referee decisions in football is a recurrent point of controversy, recently amplified by the betting allegations in Turkey. This project aims to scientifically investigate potential biases by combining public match statistics with betting odds data. The goal is to detect statistically unexpected (anomalous) decisions (e.g., penalties, red cards) made by referees under specific conditions (e.g., high-stakes matches). The analysis seeks to provide data-driven insights into sports integrity and decision-making processes.
Variable,Description,Purpose
Date,Date the match was played.,Time index for data integration.
Referee,Name of the match official.,Referee-specific performance and anomaly analysis.
"Goals, Shots, Corners, Fouls",Detailed in-game statistics.,Measures overall match flow and pressure level.
Home/Away Cards,Number of Red/Yellow Cards issued.,Part of the target variables (for anomaly detection).
Home/Away Penalties,Number of penalties awarded/not awarded.,Primary Target Variable (for anomaly detection).
