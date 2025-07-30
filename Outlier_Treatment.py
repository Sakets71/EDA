import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("titanic.csv")
df.columns=df.columns.str.strip()
# print(df.columns)

# print("Fare Describe :",df['Fare'].describe())

# sns.boxplot(x='Fare' ,data=df,color="Tomato")
# plt.title("This Boxplot of Fare")
# plt.show()

Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 -Q1

lower = Q1 - 1.5 *IQR
Upper = Q1 + 1.5 *IQR


outlir = df[(df['Fare']<lower) |(df['Fare']> Upper)]


# Remove
no_outlirs = df[(df['Fare']>=lower) & (df['Fare']<=( Upper))]

df['Fare_Capped'] = df['Fare'].clip(lower, Upper)

midean = df['Fare'].median()
df['Fare_Fixed'] = df['Fare'].apply(lambda X : midean if X >Upper else X )

sns.scatterplot(x= 'Fare',y='Age' ,data=df)
plt.title("This is outlirs")
plt.show()

