"""
    从腾讯新闻接口获取当天数据
    下载国外数据（国家每个城市的 最新数据，非时序）
"""
import requests
import json
import pandas as pd

# 获取HTML文本
def get_html_text(url):
    for i in range(5):
        try:
            res = requests.get(url,timeout = 10)
            res.raise_for_status()
            res.encoding = res.apparent_encoding
            return res.text
        except:
            print('发现错误，等待1秒 继续重试')
            time.sleep(1)
    return "Error"

# 解析该国家的疫情数据
def parse_children(country, children):
	result = []
	for row in children:
		if 'nameMap' in row:
			nameMap = row['nameMap']
		else:
			nameMap = ''
		temp = {'country': country, 'name':row['name'], 'nameMap':nameMap, 'confirmAdd':row['confirmAdd'], 'confirmAddCut':row['confirmAddCut'], \
				'confirm':row['confirm'],'suspect':row['suspect'], 'dead':row['dead'], 'heal':row['heal']} 
		result.append(temp)
	return pd.DataFrame(result)

# 腾讯新闻对应的API地址
page_url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
#获取Json
text = get_html_text(page_url)
#将json数据中的data字段的数据提取处理
json_text = json.loads(text)["data"]
#将提取出的字符串转换为json数据
json_text = json.loads(json_text)

foreign_data = json_text["foreignList"]
# 需要抓取的国外国家
foreign_country = ['韩国', '日本本土', '意大利']

result = []
for row in foreign_data:
	if row['name'] in foreign_country:
		df = parse_children(row['name'], row['children'])
		if len(result) == 0:
			result = df
		else:
			result = pd.concat([result, df])

result.to_csv('foreign_country_data.csv', index=False)
