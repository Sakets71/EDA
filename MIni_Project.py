import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('sales_data.csv')
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
df['month'] =df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.weekday
df.set_index('Date',inplace=True)
df['Sales'].plot(marker ='o',color ='teal',figsize=(10,5))
plt.title("This Weekly Sales of Shop")
plt.ylabel("sale")
plt.grid()
plt.show()

