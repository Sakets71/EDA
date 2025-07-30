import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("titanic.csv")

# Index(['PassengerId', ' Survived', ' Pclass',
    #    ' Name                                                                                ',
    #    ' Sex   ', ' Age  ', ' SibSp', ' Parch', ' Ticket            ',
    #    ' Fare    ', ' Cabin          ', ' Embarked'],


# plt.hist(df[' Age  '].dropna(), bins= 20, color='Skyblue', edgecolor ='black')
# plt.title("This is histrogran")
# plt.xlabel("Age")
# plt.ylabel("Frequenscy")
# plt.show()


# we are going to draw 

# sns.boxplot(y=' Sex   ',data=df )
# plt.title("This is seaborn boxplot")
# plt.show()


df.columns = df.columns.str.strip()  # Clean column names first
df['Age'] = df['Age'].str.strip()    # Remove spaces from values

# Now convert to numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')


# sns.kdeplot(df['Age'].dropna(),fill=True ,color ='Skyblue')
# plt.title("Smooth histrogram")
# plt.xlabel("Age")
# plt.show()

print("Summary of age :",df['Age'].describe())
