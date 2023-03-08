# %%
import pandas as pd
import re
import os
# %%
def clean_country_data():
    df_clean = pd.DataFrame()
    root_path = "country_csv_files"
    # cycle through all country csv files
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # read in country csv file as DataFrame
            df = pd.read_csv(f"{root_path}/{file}")
            
            # drop final four rows will null values
            df.drop(index=df.iloc[-4:,:].index, inplace=True)
            
            # fill nan with 0s
            df.fillna(0, inplace=True)
            
            # remove all unwanted search query columns
            for col in df:
                if re.search("^search_trends_", col) != None:
                    del df[col]

            # concatenate country to df_clean
            df_clean = pd.concat([df_clean, df], ignore_index=True)
    df_clean.to_csv("clean_country_data.csv")
    return df_clean

def check_same_number_of_rows_for_each_country(df_clean):
    bad_locations = []
    for i in range(len(df_clean["location_key"].unique())):
        location_key = df_clean["location_key"].unique()[i]
        

        if df_clean["location_key"].value_counts()[location_key] != 987:
            bad_locations.append(location_key)
    
    if len(bad_locations) == 0:
        return True
    else:
        print(bad_locations)
        return False


# %%
if __name__ == "__main__":
    df_clean = clean_country_data()
    print(check_same_number_of_rows_for_each_country(df_clean))