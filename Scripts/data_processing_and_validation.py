import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LogisticRegression
import re
import warnings
warnings.filterwarnings('ignore') # Turns off some Pandas warnings


# --- I. CONSTANTS AND FILENAMES ---
#  Ensure these files are uploaded to the Colab session.
MASTER_FILE = 'master_stats_manual_entry.csv.csv'
ODDS_FILE = 'betting_odds_raw.csv.csv'
FINAL_CSV_NAME = 'processed_data_final_eda_ready.csv'


# RPI and Decision Columns
NEW_PENALTY_WEIGHT = 0.87
REDCARD_WEIGHT = 1.0
CRITICAL_ANOMALY_COLS = ['Penalties', 'Red Cards']




# --- II. DATA LOADING, CLEANING, AND MERGING ---


def prepare_data():
   """Loads, cleans, calculates RPI, and merges all data."""
  
   # 1. Load Files (with encoding fix for Turkish characters)
   df_master = pd.read_csv(MASTER_FILE, encoding='latin1')
   df_odds = pd.read_csv(ODDS_FILE, encoding='latin1')


   # Strip whitespace from column names
   df_master.columns = df_master.columns.str.strip()
   df_odds.columns = df_odds.columns.str.strip()


   # Dynamic Column Names (Fix for character encoding issue)
   ODDS_COLS = [col for col in df_odds.columns if 'Oran' in col]
   JOIN_TAKIM_COLS = [col for col in df_odds.columns if 'Takım' in col or 'TakÄ±m' in col or 'TakÄ±mÄ±' in col]




   # 2. MASTER DATA CLEANING (Penalty/Card Imputation and Date Fix)
  
   # Drop rows with missing critical info (to remove header remnants)
   df_master.dropna(subset=['Date', 'Referee', 'Home'], inplace=True)
  
   # Fill NaN Penalties/Red Cards with 0 and convert to integer
   df_master[CRITICAL_ANOMALY_COLS] = df_master[CRITICAL_ANOMALY_COLS].fillna(0).astype(int)


   # Prepare Date Format for Merging
   df_master['Date_Clean'] = pd.to_datetime(df_master['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
   df_master.dropna(subset=['Date_Clean'], inplace=True) # Drop rows where date conversion failed




   # 3. BETTING ODDS CLEANING
   df_odds['Date_Clean'] = pd.to_datetime(df_odds['Tarih'], errors='coerce').dt.strftime('%Y-%m-%d')
  
   # Convert Odds Columns to Numeric (Fixes '-' and other strings)
   for col in ODDS_COLS:
       df_odds[col] = df_odds[col].replace('-', np.nan)
       df_odds[col] = pd.to_numeric(df_odds[col], errors='coerce')




   # 4. FINAL MERGE (Uses dynamic column names determined by the previous step)
  
   # Merge Master and Odds dataframes
   df_final_merged = pd.merge(
       df_master,
       df_odds,
       left_on=['Date_Clean', 'Home', 'Away'],
       right_on=['Date_Clean'] + JOIN_TAKIM_COLS, # Dynamic Join
       how='left'
   )


   # Drop rows where Odds are missing (Analysis requirement)
   df_final_merged.dropna(subset=[ODDS_COLS[0]], inplace=True)




   # 5. RPI CALCULATION (Feature Engineering)
   df_referee_stats = df_final_merged.groupby('Referee')[CRITICAL_ANOMALY_COLS].mean()
   df_referee_stats.columns = ['Avg_RedCards', 'Avg_Penalties']
  
   # RPI Formula (using 0.87 statistical weight)
   df_referee_stats['RPI_NEW'] = (df_referee_stats['Avg_RedCards'] * REDCARD_WEIGHT) + \
                                (df_referee_stats['Avg_Penalties'] * NEW_PENALTY_WEIGHT)


   # Merge RPI back to the main data
   df_final_adjusted = pd.merge(
       df_final_merged.drop(columns=['RPI'], errors='ignore'),
       df_referee_stats[['RPI_NEW']].rename(columns={'RPI_NEW': 'RPI'}),
       on='Referee',
       how='left'
   )
  
   # Final Index Reset (Ensures t-Test/Filtering works without KeyError)
   df_final_adjusted = df_final_adjusted.reset_index(drop=True)
  
   # Save Final CSV
   df_final_adjusted.to_csv(FINAL_CSV_NAME, index=False)
  
   return df_final_adjusted




# --- III. STATISTICAL PROOF FUNCTION (t-Test) ---


def run_t_test_and_report(df):
   """Performs the Hypothesis Test (t-Test) using the updated RPI."""
  
   # 1. Separate Groups (Top 20% by RPI)
   rpi_threshold = df['RPI'].quantile(0.80)
   df_high_rpi = df[df['RPI'] >= rpi_threshold].copy()
   df_low_rpi = df[df['RPI'] < rpi_threshold].copy()


   # 2. Prepare Samples for Testing
   sample_high = df_high_rpi['Penalties'].dropna()
   sample_low = df_low_rpi['Penalties'].dropna()


   # 3. Apply T-Test
   t_stat, p_value = stats.ttest_ind(sample_high, sample_low, equal_var=False)


   print("\n--- FINAL STATISTICAL EVIDENCE: T-TEST RESULTS ---")
   print(f"High RPI Group Avg. Penalties: {sample_high.mean():.4f}")
   print(f"Normal RPI Group Avg. Penalties: {sample_low.mean():.4f}")
   print(f"P-Value (Significance): {p_value:.8f}")


   if p_value < 0.05:
       print(" Conclusion: P-value is less than 0.05.")
       print("Null Hypothesis rejected. A STATISTICALLY SIGNIFICANT DIFFERENCE EXISTS in the average penalty rate.")
   else:
       print(" Conclusion: P-value is greater than 0.05.")
       print("Null Hypothesis not rejected. No statistically significant difference found.")


# --- IV. MAIN EXECUTION ---


if __name__ == "__main__":
   print("--- DSA-210 PROJECT DATA PROCESSING STARTED ---")
  
   try:
       df_processed = prepare_data()
      
       # Run the T-Test
       run_t_test_and_report(df_processed)
      
       print("\n--- OPERATION SUCCESSFUL ---")
       print(f"Data successfully processed and saved to '{FINAL_CSV_NAME}'.")


   except Exception as e:
       print(f"\nFATAL ERROR: Data processing failed. Error: {e}")