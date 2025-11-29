import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# Load the final ready-for-analysis file
df = pd.read_csv('processed_data_final_eda_ready.csv')


# --- COLUMN NAME FIX (Necessary due to previous encoding issues) ---
# The code uses the character-mangled column names confirmed previously:
ODDS_COLS_MANGLED = ['Ev Galibiyeti OranÄ±', 'Beraberlik OranÄ±', 'Deplasman Galibiyeti OranÄ±']
RPI_COLS = ['RPI', 'Penalties', 'Red Cards']


# Plot settings
sns.set_style("whitegrid")


# --- EDA TASK 1: RPI Distribution ---
# This visualizes the distribution of the engineered RPI feature.
plt.figure(figsize=(10, 6))
sns.histplot(df['RPI'], bins=20, kde=True, color='skyblue')
plt.title('Referee Performance Index (RPI) Distribution', fontsize=16)
plt.xlabel('RPI Value (Weighted Decision per Match)', fontsize=12)
plt.ylabel('Number of Referees', fontsize=12)
plt.show()




# --- EDA TASK 2: Correlation Heatmap (Critical Analysis) ---
# The code selects all necessary columns for correlation (RPI, Decisions, Odds).
correlation_cols = RPI_COLS + [ODDS_COLS_MANGLED[0], ODDS_COLS_MANGLED[1]] # Penalties, Red Cards, and first two Odds


# Ensure columns are numeric (Necessary for correlation)
df_corr = df[correlation_cols].apply(pd.to_numeric, errors='coerce')


correlation_matrix = df_corr.corr()


plt.figure(figsize=(10, 8))
# cmap='coolwarm' shows positive/negative correlations effectively.
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, linecolor='black')
plt.title('Correlation Between RPI, Decisions, and Betting Odds', fontsize=16)
plt.show()


# --- HYPOTHESIS TEST (t-Test) ---


# 1. Define High RPI Group (Top 20th percentile threshold)
rpi_threshold = df['RPI'].quantile(0.80)
df_high_rpi = df[df['RPI'] >= rpi_threshold]
df_low_rpi = df[df['RPI'] < rpi_threshold]


# 2. Prepare Samples for Testing (Penalty Counts)
# This tests if the RPI successfully segregated the population based on penalty rate.
sample_high = df_high_rpi['Penalties'].dropna()
sample_low = df_low_rpi['Penalties'].dropna()


# 3. Apply T-Test
t_stat, p_value = stats.ttest_ind(sample_high, sample_low, equal_var=False)


print("\n--- T-TEST RESULTS ---")
print(f"High RPI Group Average Penalties: {sample_high.mean():.4f}")
print(f"Normal RPI Group Average Penalties: {sample_low.mean():.4f}")
print(f"P-Value (Significance): {p_value:.8f}")


# 4. Interpretation of Result (Mandatory for Report)
if p_value < 0.05:
   print("\nResult: P-value is less than 0.05.")
   print("Null Hypothesis rejected. A STATISTICALLY SIGNIFICANT DIFFERENCE EXISTS in the average penalty rate between high-RPI referees and others.")
else:
   print("\nResult: P-value is greater than 0.05.")
   print("Null Hypothesis not rejected. No statistically significant difference found.")