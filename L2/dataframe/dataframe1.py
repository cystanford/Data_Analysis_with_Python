# dataframe使用
from pandas import Series, DataFrame
data = {'Chinese': [66, 95, 93, 90,80], 'Math': [30, 98, 96, 77, 90], 'English': [65, 85, 92, 88, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
print(df1)
print(df2)

# 对列名进行更换
df2.rename(columns={'Chinese': '语文', 'English': '英语', 'Math': '数学'}, inplace = True)
print(df2.isnull())
# 输出df2的概要
print(df2.describe())

