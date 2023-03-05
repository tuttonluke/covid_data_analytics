#%%
import pandas as pd
import re
import os
# %%
def clean_country_data():
    """Removes unwanted columns from DataFrame and replaces
    nan values with 0.
    """
    # cycle through all country csv files
    for root, dirs, files in os.walk("country_csv_files"):
        for file in files:
            df = pd.read_csv(f"country_csv_files/{file}")
            for col in df:
                df[col] = df[col].fillna(0)
                if re.search("^search_trends_", col) != None:
                    del df[col]
            df.to_csv(f"country_csv_files/{file[:-4]}.csv")
#%%
if __name__ == "__main__":
    clean_country_data()