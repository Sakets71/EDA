import pandas as pd
from sklearn.preprocessing import LabelEncoder
df= pd.read_csv("titanic.csv")
le =LabelEncoder()
df.columns = df.columns.str.strip()
df['Age'] = df['Age'].astype(str).str.strip()
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['IsChild'] = df['Age'] < 12
df['IsExpences'] = df['Fare'] > 100

df['AgeGroup'] = pd.cut(df['Age'],bins=[0,13,18,60,100],labels=['Child','Teen','Adult','Seoiur'])
# print(df)

df['FarePerAge'] = df['Fare'] / (df['Age']+1)

df['SexEncodder'] = le.fit_transform(df['Sex'])

print(df)



