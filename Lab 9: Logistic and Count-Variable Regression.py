########################
# Lab 9: Logistic and Count-Variable Regression #
########################

#Imports
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools import add_constant

# Load data
df = pd.read_csv('heart_data.csv')

#

# List of continuous variables as predictors
predictors = [
    'creatinine_phosphokinase',
    'ejection_fraction',
    'platelets',
    'serum_creatinine',
    'serum_sodium'
]

df_scaled =df.copy()
for col in predictors:
    df_scaled[col] = (df_scaled[col] - df_scaled[col].mean()) / df_scaled[col].std()

# Calculate and display VIF
X = add_constant(df_scaled[predictors])
vif_df = pd.DataFrame()
vif_df["Feature"] = X.columns
vif_df["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_df.to_string(index=False))
print("-" * 40)

# Make formula
formula = 'age ~ ' + '+'.join(predictors)

# Run model
print ("Fitting model...")
model = smf.poisson(formula, data=df_scaled).fit()

# Print model summary
print(model.summary())
