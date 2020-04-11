# -*- coding: utf-8 -*-
# 使用Selenium, 北京安居客->小区->二手房信息
import json
import requests
from lxml import etree
import time
from selenium import webdriver
import pandas as pd 

# 需要将chromedriver放到Chrome\Application目录下
driver = webdriver.Chrome()

# 去空格，去换行\n
def format_str(str):
    return str.replace('\n', '').replace(' ', '')

# 对页面进行抓取分析
def work(request_url):
    driver.get(request_url)
    time.sleep(1)
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    html = etree.HTML(html)
    # 设置需要抓取字段的xpath
    titles = html.xpath("/html/body/div[@class='w1180']/div[@class='maincontent']/div[@id='list-content']/div[@class='li-itemmod']/div[@class='li-info']//a/@title")
    links = html.xpath("/html/body/div[@class='w1180']/div[@class='maincontent']/div[@id='list-content']/div[@class='li-itemmod']/div[@class='li-info']//a/@href")
    addresses = html.xpath("/html/body/div[@class='w1180']/div[@class='maincontent']/div[@id='list-content']/div[@class='li-itemmod']/div[@class='li-info']/address/text()")
    prices = html.xpath("/html/body/div[@class='w1180']/div[@class='maincontent']/div[@id='list-content']/div[@class='li-itemmod']/div[@class='li-side']/p[1]/strong/text()")
    to_last_months = html.xpath("/html/body/div[@class='w1180']/div[@class='maincontent']/div[@id='list-content']/div[@class='li-itemmod']/div[@class='li-side']/p[2]/text()")
    completion_dates = html.xpath("/html/body/div[@class='w1180']/div[@class='maincontent']/div[@id='list-content']/div[@class='li-itemmod']/div[@class='li-info']/p[1]/text()[1]")
    houses = pd.DataFrame(columns = ['title', 'link', 'address', 'price', 'to_last_month', 'completion_date'])
    for i in range(len(titles)):
        # 设置抓取的房源
        temp = {}
        temp['title'] = format_str(titles[i])
        temp['link'] = format_str(links[i])
        temp['address'] = format_str(addresses[i])
        temp['price'] = format_str(prices[i])
        temp['to_last_month'] = format_str(to_last_months[i])
        temp['completion_date'] = format_str(completion_dates[i])
        # 添加房源
        houses = houses.append(temp,ignore_index=True)
    return houses

# 抓取10页北京房价数据
page_num = 10
base_url = 'https://beijing.anjuke.com/community/p'
houses = pd.DataFrame(columns = ['title', 'link', 'address', 'price', 'to_last_month', 'completion_date'])
for i in range(page_num):
    request_url = base_url+str(i+1)
    print(request_url)
    # 抓取该页的房源信息
    temp = work(request_url)
    houses = houses.append(temp)
    print(temp)
houses.to_csv('house_prices_bj.csv')


