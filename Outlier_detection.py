import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv("titanic.csv")

from scipy import stats

z_scores = stats.zscore(df['Fare'], nan_policy='omit')
df['Fare_z'] = z_scores

# Outliers if Z > 3 or Z < -3
df_z_outliers = df[(df['Fare_z'] > 3) | (df['Fare_z'] < -3)]
print("Outliers by Z-score:", df_z_outliers.shape[0])
