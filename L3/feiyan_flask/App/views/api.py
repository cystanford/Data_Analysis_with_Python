import pandas as pd
import os
from flask import Blueprint, request,render_template,redirect,json,Response
from App.models import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
api = Blueprint("api", __name__, url_prefix='/')
@api.route("")
def home():
    return redirect("/feiyan")

# 返回某个国家的疫情数据
@api.route("detail_linedata/<country>")
def detailLineData(country):
	# 读取抓取的肺炎数据
	data = pd.read_csv(os.path.join(ROOT_PATH, 'country_data.csv'))
	nameMap = {'china': '中国', 'korea': '韩国', 'japan': '日本', 'italy': '意大利', 'iran': '伊朗'}
	result = data[data['country'] == nameMap[country]]
	result = result[['confirmedCount', 'updateTime']]
	# 按照时间从小到大排序
	result = result.sort_values(by="updateTime", ascending=True)
	return Response(json.dumps({'index': result['updateTime'].tolist(), 'value': result['confirmedCount'].tolist()}), content_type='application/json')


# 返回某个国家的疫情数据
@api.route("detaildata/<country>")
def detailData(country):
	# 读取抓取的肺炎数据
	if country == 'world':
		data = pd.read_csv(os.path.join(ROOT_PATH, 'country_data.csv'))
		data = data.drop_duplicates(['country'], keep = 'first')
		# 列名country => name, confirmedCount => value
		result = data[['country', 'confirmedCount']]
		result.rename(columns = {"country": "name", 'confirmedCount': 'value'}, inplace=True)
	else:
		data = pd.read_csv(os.path.join(ROOT_PATH, 'foreign_country_data.csv'))
		result = data[['nameMap', 'confirm']]
		result = result.fillna(0);
		#print(result)
		result.rename(columns = {"nameMap": "name", 'confirm': 'value'}, inplace=True)

	# 转换为字典列表
	return Response(json.dumps(result.to_dict(orient='records')), content_type='application/json')

@api.route("feiyan", methods=["GET", "POST"])
def index():
	# 读取抓取的肺炎数据
	data = pd.read_csv(os.path.join(ROOT_PATH, 'country_data.csv'))
	#country = data.groupby('country')
	country = data.drop_duplicates(['country'], keep = 'first')
	return render_template('feiyan.html', content=country)






