# 使用BeautifulSoup分析HTML页面内容
from bs4 import BeautifulSoup

#待分析字符串
html_doc = """
<html>
<head>
    <title>BeautifulSoup Demo</title>
</head>
<body>
<p class="title aq">
    <b>
        Here is the content
    </b>
</p>
<p class="story">Python爬虫有很多优秀的工具
    <a href="https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/" class="tools" id="link1">BeautifulSoup</a>,
    <a href="http://www.selenium.org.cn/" class="sisttoolser" id="link2">Selenium</a> 
    and
    <a href="https://scrapy.org/" class="tools" id="link3">Scrapy</a>
    他们都可以帮你爬虫想要的页面内容
</p>
<p class="story">...</p>
"""
 
# 通过html字符串创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

#输出第一个 title 标签
print(soup.title)
#输出第一个 title 标签的标签名称
print(soup.title.name)
#输出第一个 title 标签的包含内容
print(soup.title.string)
#输出第一个 title 标签的父标签的标签名称
print(soup.title.parent.name)
 

#输出第一个p标签
print(soup.p)
 #输出第一个  p 标签的 class 属性内容
print(soup.p['class'])
 
#输出第一个  a 标签的  href 属性内容
print(soup.a['href'])
# soup的属性操作方法与字典一样，可以被添加,删除或修改. 
# 修改第一个 a 标签的href属性为 http://www.baidu.com/
soup.a['href'] = 'http://www.baidu.com/'
#给第一个 a 标签添加 name 属性
soup.a['name'] = u'百度'
print(soup.a)
#删除第一个 a 标签的 class 属性为
del soup.a['class']
print(soup.a)
