import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('titanic.csv')
df.columns=df.columns.str.strip()
# print("Here We can Explore data :",df.select_dtypes(include='object').columns)

# print("Value Count of Sex :",df['Sex'].value_counts())
# print("Value persentage of Embarked :",df['Embarked'].value_counts(normalize=True) * 100)

# sns.countplot(x = 'Sex',hue='Survived',data=df)
# plt.title("Count Plot of passenager")
# plt.show()


# print(df.groupby('Pclass')['Fare'].mean())


# print(df.groupby('Embarked')['Survived'].mean())

le = LabelEncoder()

df['Sex_Encoder'] = le.fit_transform(df['Sex'])
df_encode = pd.get_dummies(df , columns=['Embarked'],drop_first=True )
print(df_encode)

