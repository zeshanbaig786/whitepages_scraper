import pandas as pd

df1 = pd.read_csv('..\\StateNames.csv')
print('stateNames read')
df2 = pd.read_csv('..\\NationalNames.csv')
print('national names read')

finalDf = df1.merge(df2, on='Name',how='left')

print(finalDf.head(10))