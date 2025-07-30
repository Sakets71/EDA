import pandas as pd

df = pd.read_csv("titanic.csv")
All =df.head()
# print(All)

# Now we can get null valus rows
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






