import os
import glob
import pandas as pd

# Directory containing the downloaded .csv.gz files
DATA_DIR = "./Yellow_taxi_data/"

# Use glob to find all .csv.gz files
file_paths = glob.glob(os.path.join(DATA_DIR, "*.csv"))

# List to store individual DataFrames
dataframes = []

# Loop through all matching files
for file_path in file_paths:
    # Read the .csv.gz file into a DataFrame
    print(f"Reading {os.path.basename(file_path)}...")
    df = pd.read_csv(file_path, low_memory=False)

    # Append the DataFrame to the list
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Print the total row count
print(f"Total number of rows: {len(combined_df)}")
