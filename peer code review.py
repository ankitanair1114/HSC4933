################################
# Lab 7: Linear Regression Lab #
# ---------------------------- #
# efaustin@usf.edu # (C) 2026  #
################################

# Code is peer reviewed by Ankita Nair #
# HSC4933 IC6 #

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


# Prompt user to choose a specific dataset

print("Datasets")
print("-----------------------")
print("1. birthwt.csv")
print("2. places_2025.csv")

csv_file = input("Enter specific dataset:")

if csv_file == "1":
    csv_file = "birthwt.csv"

elif csv_file == "2":
    csv_file = "places_2025.csv"

else:
    print("Invalid Selection. Please enter 1 or 2.")
    exit()


# Load the entered dataset
df = pd.read_csv(csv_file)
print(df)

# Clean the column names to 'snake_case' format
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# List available column names
print("Available Columns:")
print(df.columns)


# Prompts the user for the X and Y variable column names
X_COL = input("Enter column name for the X variable:")
Y_COL = input("Enter column name for the Y variable:")

# Column names need to be stated in a valid manner - Ankita
if X_COL not in df.columns or Y_COL not in df.columns:
    print("Invalid column name. Please choose from the available columns.")
    exit()

# Convert the selected columns to numeric values
df[X_COL] = pd.to_numeric(df[X_COL], errors="coerce")
df[Y_COL] = pd.to_numeric(df[Y_COL], errors="coerce")

# Removes rows missing either of the values used for the regression
df_rows = df.dropna(subset=[X_COL, Y_COL]).copy()

# Specified values for X - Ankita
if len(df_rows) < 2 or df_rows[X_COL].nunique() < 2:
    print("Not enough valid data to perform regression.")
    exit()

# create scatterplot without a regression line
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df_rows[X_COL], df_rows[Y_COL], alpha=0.6, edgecolor="k", linewidth=0.3)
ax.set_xlabel(X_COL)
ax.set_ylabel(Y_COL)
ax.set_title(f"{X_COL} vs {Y_COL} (n = {len(df_rows)})")
ax.grid(alpha=0.3)
fig.tight_layout()


# Ask the user if they would like to save the scatterplot file
scatter_file = input("Would you like to save the scatterplot file? (y/n):")
if scatter_file == "y":
    scatter_file = f"{X_COL}_vs_{Y_COL}_scatter.png"
    fig.savefig(scatter_file, dpi=300)
    print(f"Saved scatterplot -> {scatter_file}")
else:
    print("Scatterplot Not Saved")

# Calculate the OLS regression line
X = sm.add_constant(df_rows[X_COL])
model = sm.OLS(df_rows[Y_COL], X).fit()


#print regression summary
print("OLS Regression Summary: ")
print(model.summary())

# Creates fig1 anf 2ig2 - Ankita
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.scatter(df_rows[X_COL], df_rows[Y_COL],
            alpha=0.6, edgecolor="k", linewidth=0.3)

# Plot the OLS regression line
x_line = np.linspace(df_rows[X_COL].min(), df_rows[X_COL].max(), 100)
y_line = model.params["const"] + model.params[X_COL] * x_line
ax2.plot(x_line, y_line, color="crimson", linewidth=2,
         label=f"OLS line (R² = {model.rsquared:.3f})")
ax2.set_xlabel(X_COL)
ax2.set_ylabel(Y_COL)
ax2.set_title(f"{Y_COL} vs. {X_COL} with OLS line (n = {len(df_rows)})")
ax2.grid(alpha=0.3)
ax2.legend()
fig2.tight_layout()

# Ask the user if they would like to save the scatterplot w/ the OLS regression line
ols_file = input("Would you like to save the scatterplot w/ the OLS regression line? (y/n):")
if ols_file == "y":
    ols_file = f"{X_COL}_vs_{Y_COL}_ols.png"
    fig2.savefig(ols_file, dpi=300)
    print(f"saved scatterplot with OLS line -> {ols_file}")
else:
    print("Scatterplot w/ OLS regression line Not Saved")

# display OLS regression
plt.show()