import pyecharts.options as opts
from pyecharts.charts import Line

# 设置折线图
line=Line()
# 设置x轴数据
line.add_xaxis(["201{}年/{}季度".format(y,z) 
              for y in range(4) 
              for z in range(1,5)])
# 设置y轴数据
line.add_yaxis(
             "手机销量", 
             [4.80,4.10,6.00,6.50,5.80,5.20,6.80,7.40,
              6.00,5.60,7.50,7.80,6.30,5.90,8.00,8.40]
             )
line.set_global_opts(
	#设置x轴标签旋转角度
	xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-40),),
	#设置y轴名称
	yaxis_opts=opts.AxisOpts(name="销量（单位/百万台）"),
	#设置图表标题
	title_opts=opts.TitleOpts(title="折线图"))

#渲染图表
line.render_notebook() 