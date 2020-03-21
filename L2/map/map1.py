# 计算平方数
def square(x):
	return x * x
# 计算列表各个元素的平方
print(list(map(square, [1,2,3,4,5])))

# lambda函数
add = lambda x, y: x + y
print(add(5, 6))

# 按照x[1]进行列表排序
a = [(2, 56), (3, 12), (6, 10), (9, 13)]
a.sort(key=lambda x: x[1])
print(a)
