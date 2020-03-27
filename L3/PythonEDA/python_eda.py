import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os
from matplotlib.font_manager import FontProperties

# 散点图
def scatter():
	# 数据准备
	N = 500
	x = np.random.randn(N)
	y = np.random.randn(N)
	# 用Matplotlib画散点图
	plt.scatter(x, y,marker='x')
	plt.show()
	# 用Seaborn画散点图
	df = pd.DataFrame({'x': x, 'y': y})
	sns.jointplot(x="x", y="y", data=df, kind='scatter');
	plt.show()

# 折线图
def line_chart():
	# 数据准备
	x = [1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910]
	y = [265, 323, 136, 220, 305, 350, 419, 450, 560, 720, 830]
	# 使用Matplotlib画折线图
	plt.plot(x, y)
	plt.show()
	# 使用Seaborn画折线图
	df = pd.DataFrame({'x': x, 'y': y})
	sns.lineplot(x="x", y="y", data=df)
	plt.show()

# 条形图
def bar_chart():
	# 数据准备
	x = ['c1', 'c2', 'c3', 'c4']
	y = [15, 18, 5, 26]
	# 用Matplotlib画条形图
	plt.bar(x, y)
	plt.show()
	# 用Seaborn画条形图
	sns.barplot(x, y)
	plt.show()

# 箱线图
def box_plots():
	# 数据准备
	# 生成0-1之间的20*4维度数据
	data=np.random.normal(size=(10,4)) 
	lables = ['A','B','C','D']
	# 用Matplotlib画箱线图
	plt.boxplot(data,labels=lables)
	plt.show()
	# 用Seaborn画箱线图
	df = pd.DataFrame(data, columns=lables)
	sns.boxplot(data=df)
	plt.show()

# 饼图
def pie_chart():
	# 数据准备
	nums = [25, 33, 37]
	# 射手adc：法师apc：坦克tk
	labels = ['ADC','APC', 'TK']
	# 用Matplotlib画饼图
	plt.pie(x = nums, labels=labels)
	plt.show()

# 饼图
def pie_chart2():
	# 数据准备
	data = {}
	data['ADC'] = 25
	data['APC'] = 33
	data['TK'] = 37
	data = pd.Series(data)
	data.plot(kind = "pie", label='heros')
	plt.show()

# 热力图
def thermodynamic():
	# 数据准备
	np.random.seed(33)
	data = np.random.rand(3, 3)
	heatmap = sns.heatmap(data)
	plt.show()

# 蜘蛛图
def spider_chart():
	# 数据准备
	labels=np.array([u"推进","KDA",u"生存",u"团战",u"发育",u"输出"])
	stats=[76, 58, 67, 97, 86, 58]
	# 画图数据准备，角度、状态值
	angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
	stats=np.concatenate((stats,[stats[0]]))
	angles=np.concatenate((angles,[angles[0]]))
	# 用Matplotlib画蜘蛛图
	fig = plt.figure()
	ax = fig.add_subplot(111, polar=True)   
	ax.plot(angles, stats, 'o-', linewidth=2)
	ax.fill(angles, stats, alpha=0.25)
	# 设置中文字体
	font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  
	ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=font)
	plt.show()

# 二元变量分布图
def jointplot():
	# 数据准备
	flights = sns.load_dataset("flights")
	# 用Seaborn画二元变量分布图（散点图，核密度图，Hexbin图）
	sns.jointplot(x="year", y="passengers", data=flights, kind='scatter')
	sns.jointplot(x="year", y="passengers", data=flights, kind='kde')
	sns.jointplot(x="year", y="passengers", data=flights, kind='hex')
	plt.show()

# 成对关系图
def pairplot():
	# 数据准备
	flights = sns.load_dataset('flights')
	# 用Seaborn画成对关系
	sns.pairplot(flights)
	plt.show()

def thermodynamic2():
	flights = sns.load_dataset('flights')
	print(flights)
	flights=flights.pivot('month','year','passengers') #pivot函数重要
	print(flights)
	sns.heatmap(flights) #注意这里是直接传入数据集即可，不需要再单独传入x和y了
	sns.heatmap(flights,linewidth=.5,annot=True,fmt='d')
	plt.show()


# 散点图
#scatter()
# 折线图
#line_chart()
# 条形图
bar_chart()
# 箱线图
#box_plots()
# 饼图
#pie_chart()
#pie_chart2()
# 热力图
#thermodynamic()
#thermodynamic2()
# 蜘蛛图
#spider_chart()
# 二元变量分布图
#jointplot()
# 成对关系图
#pairplot()