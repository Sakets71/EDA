import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('titanic.csv')
# Day 1 st

print("first 5 lines and row")
print(df.head())

print("Shape of col and row:" )
print(df.shape)

print("Colums :")
print(df.columns.tolist())

print("Types of data :")
print(df.dtypes)


# day 2 

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


# day 3
Null =df.isnull().sum()
print("Before Clean Missing : ",Null)

# Now we can get total count of row where data is missing
Count =df.isnull().sum().sum()
print("Before Clean Missing Data Count :",Count)

# find the % of data missing using "persentage formula "
Per =(df.isnull().sum().sum() /len(df)) *100
print(f"Total  :{Per} %")

# Drop all rowa which have missing valuse

Drop1 =df.dropna()
print("After Drop missing Row :",Drop1)

Col_Drop=df.drop(columns=['Cabin'])
print("After remove Column :",Col_Drop)

Fill =df['Age'].fillna(df['Age'].mean())
print("Filling missing values :",Fill)


# Fill with the most common value (mode)
Fill_Comm =df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print("Filling Comman Valus :",Fill_Comm)



Final_Count =df.isnull().sum().sum()
print("After completing All Opreation :",Final_Count)


FALL =df.dropna(inplace=True)

print("After completing All Opreation :",FALL)


# day 4

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

df['PersonType'] = df['Age'].apply(lambda age : 'Chlid'if age <18 else'Adult' )
print(df['PersonType'])

# print(df.columns)
Duplicate =df.drop_duplicates()
print("Duplicate Valus is Remove :",Duplicate)


# day 5
print(df.describe())

print(df.columns)

print(df['Age'].value_counts())

correlation_matrix = df.corr(numeric_only=True)
# print(correlation_matrix)

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()

# Day 6

sns.boxplot(x=df['Fare'])
plt.title("Boxplot of Fare")
plt.show()

sns.boxplot(x=df['Age'])
plt.title("Boxplot of Age")
plt.show()

# IQR for Fare
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = df[(df['Fare'] < lower_bound) | (df['Fare'] > upper_bound)]
print("Number of Fare outliers:", outliers.shape[0])

from scipy import stats

z_scores = stats.zscore(df['Fare'], nan_policy='omit')
df['Fare_z'] = z_scores

# Outliers if Z > 3 or Z < -3
df_z_outliers = df[(df['Fare_z'] > 3) | (df['Fare_z'] < -3)]
print("Outliers by Z-score:", df_z_outliers.shape[0])

df = df[(df['Fare'] >= lower_bound) & (df['Fare'] <= upper_bound)]

df['Fare'] = df['Fare'].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))



