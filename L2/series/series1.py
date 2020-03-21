# series使用
from pandas import Series, DataFrame
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
# 使用字典来进行创建
d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)

print(x1)
print(x2)
print(x3)