import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
# Columns : Index(['PassengerId', ' Survived', ' Pclass',
#        ' Name                                                                                ',
#        ' Sex   ', ' Age  ', ' SibSp', ' Parch', ' Ticket            ',
#        ' Fare    ', ' Cabin          ', ' Embarked'],
#       dtype='object')

# sns.scatterplot(x=' Fare    ',y=' Age  ',data=df, s=40, alpha=0.5)
# plt.title("Age vs Fare")
# plt.show()
# df_clen =df [df[' Fare    '] <800]
# sns.boxplot(y=' Fare    ',x =' Pclass',data=df_clen)
# plt.title("This is fare vs pclass")
# plt.show()

# sns.violinplot(y=' Fare    ',x =' Pclass',data=df)
# plt.title("violinplot")
# plt.show()


# pd.crosstab(df[' Pclass'], df[' Survived'], margins=True)
# sns.countplot(x=' Survived' ,hue=' Sex   ',data=df )
# plt.title("compere betnn ")
# plt.xlabel(" Survived (yes = 1, No = 0)")
# plt.show()





