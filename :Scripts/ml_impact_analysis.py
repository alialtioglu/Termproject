import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


# Load the final ready-for-analysis file
df = pd.read_csv('processed_data_final_eda_ready.csv')


# --- 1. SCORE PARSING (Final Error Resolution) ---


# Solution: Replace all non-numeric characters with a standard hyphen (-)
# This ensures a clean 'number-number' format by stripping extra hyphens and non-digits.
df['Score_Clean'] = df['Score'].astype(str).str.replace(r'[^0-9]', '-', regex=True).str.replace(r'-+', '-', regex=True).str.strip('-')


# Now, split the clean score column using the standard hyphen
df[['Home_Score_Str', 'Away_Score_Str']] = df['Score_Clean'].str.split('-', expand=True)


# Extract numerical scores, converting non-numeric values to NaN
df['Home_Score'] = pd.to_numeric(df['Home_Score_Str'], errors='coerce')
df['Away_Score'] = pd.to_numeric(df['Away_Score_Str'], errors='coerce')


# Drop rows where scores couldn't be parsed (final cleanup)
df.dropna(subset=['Home_Score', 'Away_Score'], inplace=True)
# Define the Target Variable (Y): Home Win (1) vs. Not Win (0)
df['Home_Win'] = np.where(df['Home_Score'] > df['Away_Score'], 1, 0)




# --- 2. LOGISTICS REGRESSION MODEL SETUP ---
# X variables: Decision frequency (used to calculate the impact ratio)
X = df[['Penalties', 'Red Cards']]
# Y variable: Match result
Y = df['Home_Win']


if len(X) > 0:
   try:
       # Fit the model
       model = LogisticRegression(solver='liblinear', random_state=42)
       model.fit(X, Y)


       # Extract Coefficients (Beta values)
       # These coefficients represent the statistical power of the decision on the outcome.
       beta_penalty = model.coef_[0][0]
       beta_redcard = model.coef_[0][1]
      
       # Calculate the Impact Ratio (Absolute value of Beta_Penalty / Beta_RedCard)
       impact_ratio = abs(beta_penalty / beta_redcard) if beta_redcard != 0 else float('inf')


       print("\n--- STATISTICAL IMPACT STRENGTH RESULTS ---")
       print(f"Number of matches included in analysis: {len(X)}")
       print(f"Penalty decision influences the match result approximately {impact_ratio:.2f} times more than the Red Card decision.")


   except Exception as e:
       print(f"\nMODEL ERROR: {e}")
else:
   print("\nMODEL FAILED: Zero matches remain after cleaning. Analysis cannot proceed.")