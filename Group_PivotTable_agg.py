import pandas as pd

df = pd.read_csv("titanic.csv")
df.columns = df.columns.str.strip()

# Men =df.groupby('Pclass')['Fare'].mean()
# print("average :",Men)

# Count = df.groupby('Sex')['Survived'].mean()
# print(Count)

# Mul_Avg =df.groupby('Pclass')['Fare'].agg(['max','mean'])
# print(Mul_Avg)

# mul_col = df.groupby(['Pclass','Sex'])['Fare'].mean()
# print(mul_col)

# Total = pd.pivot_table(df,values='Survived',index='Sex',columns='Pclass',aggfunc='sum')
# print(Total)

# Sort = df.groupby('Embarked')['Fare'].mean().sort_index(ascending=True)
# print(Sort)


