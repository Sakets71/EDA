import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('titanic.csv')
df.columns = df.columns.str.strip()
df_num = df.select_dtypes(include='number')
# print(df_num)

df_mat = df_num.corr()
# print(df_mat)

# plt.figure(figsize=(10,6))
# sns.heatmap(df_mat ,annot=True,cmap='coolwarm',fmt='.2f')
# plt.title("Correlation of titanic Dataset")
# plt.show()

Corr_with_Survived = df_mat['Survived'].sort_values(ascending=False)
# print(Corr_with_Survived)

# sns.scatterplot(x='Survived',y='Fare',data=df)
# plt.title("Fare vs Survived")
# plt.show()





