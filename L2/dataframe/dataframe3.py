import pandas as pd
from pandas import DataFrame

df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(1,6)})
df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(1,6)})
#print(df1)
#print(df2)
df3 = pd.merge(df1, df2, on='name')
#print(df3)
df3 = pd.merge(df1, df2, how='inner')
#print(df3)
df3 = pd.merge(df1, df2, how='left')
df3 = pd.merge(df1, df2, how='right')
#print(df3)
df3 = pd.merge(df1, df2, how='outer')
print(df3)
