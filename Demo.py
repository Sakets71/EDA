import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print("first 5 lines and row")
print(df.head())

print("Shape of col and row:" )
print(df.shape)

print("Colums :")
print(df.columns.tolist())

print("Types of data :")
print(df.dtypes)