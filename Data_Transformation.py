import pandas as pd

df = pd.read_csv("titanic.csv")
# print(df.head())
# print(df.columns)

# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],

df.rename(columns= {
    'Pclass' :'ParessClass',
    'Fare': 'TicketFare',
    'SibSp': 'SiblingsSpousesAboard',
    'Parch': 'ParentsChildrenAboard'
 },inplace=True)


# print("After rename Columns :",df.columns)

# Replace 'male' with 'M' and 'female' with 'F'
# print("After Repalce :",df['Sex'].replace({"male" :"M","female":"F"}))

# Convert Sex column to numeric (M: 0, F: 1)

# print("After Repalce :",df['Sex'].map({'male': 1,'female' :0}))
# print(df['Sex'])

# df['PersonType'] = df['Age'].apply(lambda age : 'Chlid'if age <18 else'Adult' )
# print(df['PersonType'])

# print(df.columns)
Duplicate =df.drop_duplicates()
print("Duplicate Valus is Remove :",Duplicate)