import pyecharts.options as opts
from pyecharts.charts import Pie

# 绘制玫瑰图
rose = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["201{}年/{}季度".format(y,z)
            for y in range(2) 
                  for z in range(1,3)], [4.80,4.10,5.80,5.20])],
        #设置内径外径
        radius=["0%", "75%"],
        #玫瑰图有两种类型
        rosetype="radius",          
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
)
rose.render_notebook()