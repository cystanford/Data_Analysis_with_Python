# 使用request + BeautifulSoup提取安居客北京二手房信息
import requests
from bs4 import BeautifulSoup
 
# 请求URL
url = 'https://beijing.anjuke.com/sale/p1'

# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(url,headers=headers,timeout=10)
content = html.text
#print(content)

# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
#输出第一个 title 标签
print(soup.title)
#输出第一个 title 标签的标签名称
print(soup.title.name)
#输出第一个 title 标签的包含内容
print(soup.title.string)


# 找到class="list-item"下面的所有li标签
house_list=soup.find_all('li',class_="list-item")
# 提取房源信息
for house in house_list:
    # 提取房源信息
    name = house.find('div',class_="house-title").a.text.strip()
    details = house.find('div',class_='details-item').text.strip()
    address = house.find('span',class_="comm-address").text.strip()
    print('address', address)
    tags = house.find('div',class_='tags-bottom').text.strip()
    print('tags', tags)
    broker = house.find('div',class_="broker-item").text.strip()
    print('broker', broker)
    price = house.find('span',class_="price-det").text.strip()
    print('price', price)
    unit_price = house.find('span',class_="unit-price").text.strip()
    print('unit_price', unit_price)
    print(name, details, address, tags, broker, price, unit_price)
