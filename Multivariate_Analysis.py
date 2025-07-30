import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("titanic.csv")
# Columns : Index(['PassengerId', ' Survived', ' Pclass',
#        ' Name                                                                                ',
#        ' Sex   ', ' Age  ', ' SibSp', ' Parch', ' Ticket            ',
#        ' Fare    ', ' Cabin          ', ' Embarked'],
#       dtype='object')

df.columns = df.columns.str.strip()

# sns.pairplot(df[['Age','Sex','Pclass','Fare']])
# plt.suptitle("It show pair relation between 4 columns",y=1.02)
# plt.show()


# sns.boxplot(x='Sex',y='Age' ,hue='Fare',data=df)
# plt.title("Grouped Boxplot")
# plt.show()

g = sns.FacetGrid(df,col='Sex')
g.map(sns.histplot , 'Fare',bins = 20)
plt.show()

# g = sns.FacetGrid(df, row='Pclass', col='Sex')
# g.map(sns.histplot, 'Age')
# plt.show()
# correlation = df.corr(numeric_only=True)

# plt.figure(figsize=(10, 6))
# sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title("Correlation Matrix Heatmap")
# plt.show()
