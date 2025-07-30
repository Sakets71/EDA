import pandas as pd

url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df.head())

# single col
print(df["PassengerId"])
# multiple lines

print(df[['PassengerId','Pclass']])


print(df.loc[2])

print(df.loc[0:2,['Sex','Age']])
# only col
print(df.iloc[0])
# row+ col
print(df.iloc[0:3, 0:3])


# Passengers older than 60
print(df['Age']>60)

# Female passengers only
print(df['Sex']=='Female')

# Male passengers in class 1

print((df['Pclass']== 1) & (df['Sex']=='Male'))


# Age between 20 and 30

print((df['Age']>=20)& (df['Age']<=30))

# Show all rows where passenger age is above 50.

print(df['Age']>=50)

# Show names of all passengers who paid fare > 100.

print(df['Fare']>100)

# Show only female passengers who survived
print((df['Survived']==1)&df['Sex']=='Female')
