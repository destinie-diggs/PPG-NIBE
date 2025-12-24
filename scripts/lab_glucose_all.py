import pandas as pd
import vitaldb
import os
#This script is used to download all (35,358) of the lab glucose samples and save to a CSV

# Downloading labs file 
VITALDB_LABS_URL = "https://api.vitaldb.net/labs"
df_labs = pd.read_csv(VITALDB_LABS_URL)
#df_labs.to_csv("vitaldb_labs.csv", index=False) #as csv

#Downloading case files
VITALDB_DATA_URL = "https://api.vitaldb.net/cases"
df_cases = pd.read_csv(VITALDB_DATA_URL)

#Filter labs to only get gluc results
labs_gluc_cases = df_labs.loc[df_labs['name'] == 'gluc', :]

#Save to csv
labs_gluc_cases.to_csv("labs_gluc_all.csv", mode='a', header=header, index=False)
print("CSV files saved successfully!")
