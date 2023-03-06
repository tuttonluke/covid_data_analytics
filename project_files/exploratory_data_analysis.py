#%%
import pandas as pd
import re
import os
from sklearn.impute import KNNImputer
# %%
def clean_region_data():
    """Removes unwanted columns from DataFrame and replaces
    nan values with 0.
    """
    # cycle through all region csv files
    for root, dirs, files in os.walk("region_csv_files"):
        for file in files:
            df = pd.read_csv(f"region_csv_files/{file}")
            for col in df:
                # drop final three rows will null values
                df.drop(index=df.iloc[-3:,:].index, inplace=True)
                # fill other missing values with 0
                df[col] = df[col].fillna(0)
                # remove all search trend columns
                if re.search("^search_trends_", col) != None:
                    del df[col]
            df.to_csv(f"region_csv_files/{file[:-4]}_clean.csv")
#%%
if __name__ == "__main__":
    clean_region_data()






# %% KNN Imputation
df = pd.read_csv("region_csv_files/GB_London.csv")
df_imputer_knn_sklearn = df.copy(deep=True)
df_imputer_knn_sklearn = df_imputer_knn_sklearn.fillna(0)
df_imputer_knn_sklearn.isna().sum()
knn_imputer = KNNImputer(n_neighbors=3)
df_imputer_knn_sklearn["new_confirmed"] = knn_imputer.fit_transform(df_imputer_knn_sklearn["new_confirmed"].values.reshape(-1, 1))

