# HSC4933 Lab 5: Dataset Conversion #
# Ankita Nair #
# XLSX #

# Import Libraries
import pandas as pd

# open the .csv
df = pd.read_csv("Maternal Health Risk Data Set.csv")

# save it as a .xlsx
df.to_excel("Maternal Health Risk Data Set.xlsx", index=False)