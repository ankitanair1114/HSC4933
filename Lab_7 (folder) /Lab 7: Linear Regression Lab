# HSC4933 Lab 7: Linear Regression Lab #
# Ankita Nair #

# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm


# The following lines of code is the input the user can put in
print("Choose a dataset:")
print("1. birthwt.csv")
print("2. places_2025.csv")
dataset_choice = input("Enter 1 or 2: ")

# "If" statements and the CSV_PATH for each file/dataset
if dataset_choice == "1":
    CSV_PATH = "birthwt.csv"
elif dataset_choice == "2":
    CSV_PATH = "places_2025.csv"
else:
    print("Invalid dataset choice")
    exit()

# Load csv and perform sanity check
df = pd.read_csv(CSV_PATH)

# Clean column names to snake_case
df.columns = (df.columns
              .str.strip()
              .str.lower()
              .str.replace(" ", "_")
              .str.replace("-", "_"))

# List available column names
print("Available columns:")
print(df.columns.tolist())

#  Variables for the X and Y columns
X_COL = input("Enter X variable column name: ")
Y_COL = input("Enter Y variable column name: ")

#The following line of code lets the user known if they typed in the wrong X/Y column name or if they made a spelling mistake whule typing it out.
if X_COL not in df.columns or Y_COL not in df.columns:
    print("Invalid column name")
    exit()

# Select data and remove missing values
data = df[[X_COL, Y_COL]].dropna()

# Create scatterplot
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(data[X_COL], data[Y_COL],
           alpha=0.6, edgecolor="k", linewidth=0.3)
ax.set_xlabel(X_COL)
ax.set_ylabel(Y_COL)
ax.set_title(f"{Y_COL} vs. {X_COL} (n = {len(data)})")
ax.grid(alpha=0.3)
fig.tight_layout()

# Ask whether to save scatterplot
save_scatter = input(
    "Would you like to save the scatterplot without the regression line? (yes/no): "
)

if save_scatter.lower() == "yes":
    scatter_file = input("Enter filename for scatterplot: ")
    if not scatter_file.endswith(".png"):
        scatter_file = scatter_file + ".png"
    fig.savefig(scatter_file, dpi=300)
    print(f"Saved scatterplot -> {scatter_file}")

# Perform linear regression
X = sm.add_constant(data[X_COL])
model = sm.OLS(data[Y_COL], X).fit()

# Print regression summary
print("OLS Regression Summary: ")
print(model.summary())

# Scatterplot with regression line (creating a new one)
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(data[X_COL], data[Y_COL],
           alpha=0.6, edgecolor="k", linewidth=0.3)

x_line = np.linspace(data[X_COL].min(), data[X_COL].max(), 100)
y_line = model.params["const"] + model.params[X_COL] * x_line

ax.plot(x_line, y_line, color="crimson", linewidth=2,
        label=f"OLS line (R² = {model.rsquared:.3f})")
ax.set_xlabel(X_COL)
ax.set_ylabel(Y_COL)
ax.set_title(f"{Y_COL} vs. {X_COL} with OLS line (n = {len(data)})")
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()

# Saving the scatterplot without the regression line
save_ols = input(
    "Would you like to save the scatterplot with the OLS regression line? Answer choices are (Y/N): "
)

if save_ols.lower() == "Y":
    ols_file = input("Enter filename for OLS scatterplot: ")
    if not ols_file.endswith(".png"):
        ols_file = ols_file + ".png"
    fig.savefig(ols_file, dpi=300)
    print(f"Saved scatterplot with OLS line -> {ols_file}")

# Display plots
plt.show()
