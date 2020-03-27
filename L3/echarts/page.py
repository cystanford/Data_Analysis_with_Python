# 多图表page
import pyecharts.options as opts
from pyecharts.charts import Bar

# 多page
from pyecharts.charts import Page,Bar,Funnel 

page=Page() 
bar=Bar("商品销量","各季度的商品销量") 
bar.add("2018Q3",["轴承","弹簧","齿轮","导轨","丝杠"],[25,23,17,14,17]) 
bar.add("2018Q4",["轴承","弹簧","齿轮","导轨","丝杠"],[23,21,19,19,13]) 
page.add_chart(bar,name="bar") 
funnel=Funnel("订单转化效率","今日用户的订单转化效率") 
funnel.add("",["访问","搜索","点击","加购","订单"],[100.00,78.12,35.74,17.17,2.62]) 
page.add_chart(funnel,name="funnel") 
page.render("page.html") 

