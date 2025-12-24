import pandas as pd
import vitaldb

#This script is used to download the clinical information file and track list file from VitalDB as CSV

# URLs for VitalDB dataset
VITALDB_DATA_URL = "https://api.vitaldb.net/cases"
VITALDB_TRACKS_URL = "https://api.vitaldb.net/trks"

# 1. Read the CSVs from the URLs
df_cases = pd.read_csv(VITALDB_DATA_URL)
df_trks = pd.read_csv(VITALDB_TRACKS_URL)

# 2. Save them locally as CSV files
df_cases.to_csv("vitaldb_cases.csv", index=False)
df_trks.to_csv("vitaldb_tracks.csv", index=False)

print("CSV files saved successfully!")
