# Anomaly Detection in Football Referee Decisions
The objectivity of referee decisions in football is a recurrent point of controversy, recently amplified by the betting allegations in Turkey. This project aims to scientifically investigate potential biases by combining public match statistics with betting odds data. The goal is to detect statistically unexpected (anomalous) decisions (e.g., penalties, red cards) made by referees under specific conditions (e.g., high-stakes matches). The analysis seeks to provide data-driven insights into sports integrity and decision-making processes.


# Core Data 
The main dataset will consist of detailed match statistics for the Turkish Süper Lig:

### Match details, including  Home/Away Teams, and the Referee's name.

### In-game statistics like Goals, Shots, Corners, and Fouls.

### The primary outcome variables: The number of Red/Yellow Cards and Penalties awarded or should be awarded  to each team.


# Data Enrichment  

### The core data will be enriched with two critical types of data, analogous to creating indices or adding financial indicators in a stock market project:

### Betting Odds Data: The Closing Odds (1X2) collected from public archives will be used as a financial market indicator, representing the expected outcome of the match.

### Referee Performance Index (RPI): This is a custom index calculated from the core data. It measures each referee's historical tendency by calculating their average rate of awarding penalties and red cards per match, providing a baseline "bias" metric.

# Data Collection Strategy 

### Match statistics will be collected using Web Scraping tools like Python's requests and BeautifulSoup libraries from public sports statistics websites.

### Betting odds will be sourced from publicly accessible archives via CSV downloads or an API.

### All data will be cleaned, prepared, and merged into a master file, indexed by match.

### This master file, along with the collection scripts, will be stored in the GitHub repository.
