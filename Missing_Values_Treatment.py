import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('titanic.csv')
df.columns = df.columns.str.strip()

# per =df['Pclass'].isnull().sum().sum()
# print(per)

# sns.heatmap(df.isnull(), cbar=False ,cmap='viridis')
# plt.title("Heatmap")
# plt.show()


df_clen = df.dropna()

df_age = df.dropna(subset='Sex')

df_fill = df['Cabin'].fillna('Unknow')
df['Age'] =pd.to_numeric(df['Age'], errors='coerce')
df_fill_with =df['Age'].fillna(df['Age'].mean())
df.ffill(inplace=True)

df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x : x.fillna(x.median()))
