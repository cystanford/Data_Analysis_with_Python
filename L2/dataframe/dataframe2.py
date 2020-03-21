import pandas as pd
from pandas import Series, DataFrame

# 读取xlsx文件
score = DataFrame(pd.read_excel('heros.xlsx'))
score.to_excel('result.xlsx')
print(score)
# 读取csv文件
score = pd.read_csv('heros.csv')
score.to_csv('result.csv')
