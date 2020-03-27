"""
    从丁香园接口获取整体数据
   	国外的时序数据（没有精确到具体城市）
"""
import requests
import json
import time
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

# 将timestamp转换为日期类型
def timestamp_to_date(timestamp, format_string="%Y-%m-%d"):
    time_array = time.localtime(timestamp)
    str_date = time.strftime(format_string, time_array)
    return str_date

# 从row中得到数据
def get_data_from_row(row, province, city, updateTime):
    confirmedCount = row['confirmedCount']
    confirmedCount = row['confirmedCount']
    suspectedCount = row['suspectedCount']
    curedCount = row['curedCount']
    deadCount = row['deadCount']
    temp_dict = {'province': province, 'city': city, 'updateTime': updateTime, 'confirmedCount': confirmedCount, 'suspectedCount': suspectedCount, 'curedCount': curedCount, 'deadCount': deadCount}
    return temp_dict

# 返回某个省份下面所有城市的数据
def get_data_from_cities(results, province, updateTime):
    data = []
    for row in results:
        print(row)
        cityName = row['cityName']
        temp_dict = get_data_from_row(row, province, cityName, updateTime)
        data.append(temp_dict)
    return data        

# 得到指定的省份数据
def get_data_from_country(country='中国'):
    if country == '中国':
        page_url = "https://lab.isaaclin.cn/nCoV/api/overall?latest=0"
    else:
        page_url = 'https://lab.isaaclin.cn/nCoV/api/area?latest=0&province=' + country

    data = []
    text = get_html_text(page_url)
    results = json.loads(text)["results"]
    for row in results:
        if 'updateTime' in row:
            updateTime = timestamp_to_date(row['updateTime'] / 1000)
        else:
            updateTime = timestamp_to_date(row['modifyTime'] / 1000)
        if 'currentConfirmedCount' in row:
            currentConfirmedCount = row['currentConfirmedCount']
        else:
            currentConfirmedCount = 0
        temp_dict = {'country': country, 'updateTime': updateTime, 'currentConfirmedCount': currentConfirmedCount, 'confirmedCount': row['confirmedCount'], 'suspectedCount': row['suspectedCount'], \
                    'curedCount': row['curedCount'], 'deadCount': row['deadCount']}            
        data.append(temp_dict)
        #print(row)

    df = pd.DataFrame(data)
    # 数据清洗，每个国家每天只保留最新的数据
    clean_df = df.drop_duplicates(['country', 'updateTime'], keep = 'first')
    print(clean_df)
    return clean_df

# 从API中获取省份列表province_list
def get_foreign_name():
    #获取Json
    page_url = "https://lab.isaaclin.cn/nCoV/api/provinceName"
    text = get_html_text(page_url)
    all_list = set(json.loads(text)["results"])
    # 国外的名称 = 所有国家 - 中国省份
    china_city = set(["上海市", "云南省", "内蒙古自治区", "北京市", "台湾", "吉林省", "四川省", "天津市", "宁夏回族自治区", "安徽省", "山东省", "山西省", "广东省", "广西壮族自治区", "新疆维吾尔自治区", "江苏省", "江西省", "河北省", "河南省", "浙江省", "湖北省", "湖南省", "澳门", "甘肃省", "福建省", "西藏自治区", "贵州省", "辽宁省", "重庆市", "陕西省", "青海省", "香港", "黑龙江省"])
    foreign_list = all_list - china_city
    return foreign_list

# 从API中获取国外国家列名
foreign_list = get_foreign_name()

# 得到中国的总统计数据
result = get_data_from_country('中国')
# 得到国外的总统计数据
for country in foreign_list:
    df = get_data_from_country(country)
    #print(df)
    result = pd.concat([result, df])
# 保存为csv
result.to_csv('./country_data.csv', index=False)


