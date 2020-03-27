# 柱状图绘制
import pyecharts.options as opts
from pyecharts.charts import Bar

# 绘制单列柱状图
def work1():
	country = ["美国","西班牙","意大利","法国","德国","伊朗","英国","以色列","荷兰","奥地利"]
	data = [13981, 7457, 5210, 2933, 1970, 1700, 1452, 1000, 852, 684]    
	bar = (    
		Bar()    
		.add_xaxis(country)    
		.add_yaxis("新增确诊", data)
		.set_series_opts(label_opts=opts.LabelOpts(is_show=False))    
		.set_global_opts(title_opts=opts.TitleOpts(title="昨日新增确诊国家 Top10"))
		)
	bar.render('temp.html')
	#bar.render_notebook()

# 绘制多列柱状图
def work2():
	# 绘制多列柱状图
	country = ["美国","西班牙","意大利","法国","德国","伊朗","英国","以色列","荷兰","奥地利"]
	data1 = [69223, 49515, 74386, 25233, 37323, 27017, 9529, 2369, 6412, 5560]    
	data2 = [13981, 7457, 5210, 2933, 1970, 1700, 1452, 1000, 852, 684]    
	bar = (    
		Bar()    
		.add_xaxis(country)    
		.add_yaxis("累计确诊", data1)
		.add_yaxis("新增确诊", data2)
		.set_series_opts(label_opts=opts.LabelOpts(is_show=False))    
		.set_global_opts(title_opts=opts.TitleOpts(title="昨日新增确诊国家 Top10"))
		)
	bar.render('temp.html')

#work1()
work2()


