# numpy中统计函数的使用
import numpy as np
# 最大、最小值
def work1():
	a = np.array([[1,2,3], [4,5,6], [7,8,9]])
	print(np.min(a))
	print(np.min(a,0))
	print(np.min(a,1))
	print(np.max(a))
	print(np.max(a,0))
	print(np.max(a,1))

# 统计百分位数
def work2():
	a = np.array([[1,2,3], [4,5,6], [7,8,9]])
	print(np.percentile(a, 50))
	print(np.percentile(a, 50, axis=0))
	print(np.percentile(a, 50, axis=1))

# 中位数、平均数
def work3():
	a = np.array([[1,2,3], [4,5,6], [7,8,9]])
	#求中位数
	print(np.median(a))
	print(np.median(a, axis=0))
	print(np.median(a, axis=1))
	#求平均数
	print(np.mean(a))
	print(np.mean(a, axis=0))
	print(np.mean(a, axis=1))

# 加权平均值
def work4():
	a = np.array([1,2,3,4])
	weights = np.array([1,2,3,4])
	print(np.average(a))
	print(np.average(a,weights=weights))

# 标准差、方差
def work5():
	a = np.array([1,2,3,4])
	print(np.std(a))
	print(np.var(a))

# 对数组进行排序
def work6():
	a = np.array([[4,3,2],[2,4,1]])
	print(np.sort(a))
	print(np.sort(a, axis=None))
	print(np.sort(a, axis=0))
	print(np.sort(a, axis=1))
	print(type(a))
	
# 对数组进行排序
def work7()
	# 使用List进行排序
	a = [4,3,2,2,4,1]
	print(type(a))
	a.sort()
	print(a)
	a.sort(reverse=True)
	print(a)

#work1()
#work2()
#work3()
#work4()
#work5()
work6()
