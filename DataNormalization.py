import pandas as ps
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df= ps.read_csv('titanic.csv')

df_num = df.select_dtypes(include='number')
