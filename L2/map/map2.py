"""
	新列表 = 原列表的平方
	使用map, lambda两种方法完成
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 计算平方数
def square(x):
	return x * x
print(list(map(square, numbers)))

# 使用lambda定义函数
print(list(map(lambda x: x*x, numbers)))

