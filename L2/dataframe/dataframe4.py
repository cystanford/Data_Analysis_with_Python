# DataFrame练习
from pandas import Series, DataFrame
data = {'Chinese': [66, 95, 93, 90,80], 'Math': [30, 98, 96, 77, 90], 'English': [65, 85, 92, 88, 90]}
df = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])

# 提取Index为ZhangFei的行
print(df.loc['ZhangFei'])
# 提取第0行
print(df.iloc[0])

# 提取列为English的所有行
print(df.loc[:,['English']])
# 提取第2列的所有行
print(df.iloc[:,2])

# 查看ZhangFei, GuanYu的Chinese Math成绩
print(df.loc[['ZhangFei','GuanYu'], ['Chinese','Math']])
print(df.iloc[[0,1],[0,1]])