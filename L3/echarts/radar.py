# 绘制雷达图
from pyecharts import options as opts
from pyecharts.charts import Page, Radar

v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

radar = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="KDA", max_=6500),
            opts.RadarIndicatorItem(name="输出", max_=16000),
            opts.RadarIndicatorItem(name="经济", max_=30000),
            opts.RadarIndicatorItem(name="生存", max_=38000),
            opts.RadarIndicatorItem(name="推进", max_=52000),
            opts.RadarIndicatorItem(name="打野", max_=25000),
        ]
    )
    .add("鲁班", v1,            #添加系列名称及数据
         color="red",           #设置边框线的颜色
         areastyle_opts = opts.AreaStyleOpts(#设置填充的属性
             opacity = 0.5,                  #透明度
             color="red"                     #填充颜色
     ),)
    .add("后裔", v2,color="blue",
         areastyle_opts = opts.AreaStyleOpts(
             opacity = 0.5,#透明度
             color="blue"
     ),)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="英雄成长对比"))
)

radar.render_notebook()