# HSC4933 Lab 5: Dataset Conversion #
# Ankita Nair #
# JSON #

# Import Libraries
import pandas as pd

# Open the .csv
df = pd.read_csv("Maternal Health Risk Data Set.csv")

df.to_parquet("Maternal Health Risk Data Set.parquet",\
                engine="pyarrow", index=False)
df.to_json("Maternal Health Risk Data Set.json",\
            orient="records", indent=2)


