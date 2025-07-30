import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("titanic.csv")

# plt.plot(df['Fare'][:20])
# plt.title("This is first graph")
# plt.xlabel("Passenger Index")
# plt.ylabel("Fare")
# plt.show()

# df[' Survived'].value_counts().plot(kind='bar',color='Skyblue' )
# plt.title(" Survived bar ")
# plt.xlabel("Survived")
# plt.ylabel("Count")
# plt.show()


plt.hist(df[' Fare    '].dropna(),bins=20,color='salmon',edgecolor='black')
plt.title("This is Histrogram")
plt.xlabel("Fare")
plt.ylabel("Frequnscy ")
plt.show()

# sns.countplot(x=' Sex   ', data=df , palette='pastel')
# plt.title("This count of  male and female passenger")
# plt.show()
# ' Survived'



# sns.countplot(x=' Survived', hue=' Sex   ', data=df, palette='set2')
# plt.title("Survival by Gender")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# plt.show()





