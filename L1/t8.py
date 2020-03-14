import numpy as np
# ndarray使用
def work1():
	a = np.array([1, 2, 3])
	b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	b[1,1]=10
	print(a.shape)
	print(b.shape)
	print(a.dtype)
	print(b)

# 结构化数组的使用
def work2():
	persontype = np.dtype({'names':['name', 'age', 'chinese', 'math', 'english'], \
							'formats':['S32','i', 'i', 'i', 'f']})
	peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5), \
						("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)], dtype=persontype)
	ages = peoples['age']
	chineses = peoples['chinese']
	maths = peoples['math']
	englishs = peoples['english']
	print(np.mean(ages))
	print(np.mean(chineses))
	print(np.mean(maths))
	print(np.mean(englishs))

#work1()
work2()


