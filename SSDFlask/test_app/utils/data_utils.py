import pandas as pd
import os

def load_election_data(filename):
    # 1. Get the absolute path of the directory containing THIS file (utils/)
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go up one level to 'test_app' and then into 'data'
    # We join (utils_dir) + (up one) + (data folder) + (filename)
    base_dir = os.path.dirname(utils_dir)
    data_path = os.path.join(base_dir, 'data', filename)
    
    # 3. Validation
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at expected path: {data_path}")
        
    return pd.read_csv(data_path)

def filter_data_by_year(df, year):
   return df[df['Year'].astype(str) == str(year)]

def get_winner(df, year):
   subset = df[(df['Year'].astype(str) == str(year)) & (df['Method'].str.contains("Actual"))]
   if subset.empty: return None
   return subset.loc[subset['Votes'].idxmax(), 'Candidate']