import pandas as pd

data = {
    'date' : ['2002-01-01','2003-03-03','2004-04-04'],
    'Sale' :['200','300','400']
}

df =pd.DataFrame(data)



# Type convert str to Date time

df['date']= pd.to_datetime(df['date'])
# # print(df['date'].dtypes)
# df['year'] = df['date'].dt.year
# df['month'] = df['date'].dt.month
# df['day'] = df['date'].dt.day
# df['time'] = df['date'].dt.time
# df['weekday'] = df['date'].dt.weekday
# print(df)
# Get = df[df['date'] > '2003-03-03']
df.set_index('date',inplace=True)
total = df['Sale'].resample('M').sum()

print("Sum is :",total)
