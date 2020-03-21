import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics.api as smg
import patsy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from scipy import stats
import seaborn as sns
import datetime, os, warnings

warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #可以显示负号

# 设置起始时间
start = datetime.datetime(2019,1,1)
end = datetime.datetime(2019,12,31)
#print(start)

from pandas_datareader.data import DataReader
# 读取上证综指 及 探路者数据
def load_data():
	if os.path.exists('000001.csv'):
		data_ss = pd.read_csv('000001.csv')
		data_tlz = pd.read_csv('300005.csv')
	else:
		# 上证综指
		data_ss = DataReader("000001.SS", "yahoo",start,end)
		# 300005 探路者股票 深证
		data_tlz = DataReader("300005.SZ", "yahoo",start,end)
		data_ss.to_csv('000001.csv')
		data_tlz.to_csv('300005.csv')
	return data_ss, data_tlz

data_ss, data_tlz = load_data()

print(data_ss.head())
print(data_tlz.head())

# 探路者与上证综指
close_ss = data_ss["Close"]
close_tlz = data_tlz["Close"]

# 将探路者与上证综指进行数据合并
stock = pd.merge(data_ss, data_tlz, left_index = True, right_index = True)
stock = stock[["Close_x","Close_y"]]
stock.columns = ["上证综指","探路者"]

# 统计每日收益率
daily_return = (stock.diff()/stock.shift(periods = 1)).dropna()
print(daily_return.head())
# 找出当天收益率大于10%的，应该是没有，因为涨停为10%
print(daily_return[daily_return["探路者"] > 0.1])

# 每日收益率可视化
fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(15,6))
daily_return["上证综指"].plot(ax=ax[0])
ax[0].set_title("上证综指")
daily_return["探路者"].plot(ax=ax[1])
ax[1].set_title("探路者")
plt.show()


# 散点图
fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(12,6))
plt.scatter(daily_return["探路者"],daily_return["上证综指"])
plt.title("每日收益率散点图 from 探路者 & 上证综指")
plt.show()

# 回归分析
import statsmodels.api as sm
# 加入截距项
daily_return["intercept"]=1.0
model = sm.OLS(daily_return["探路者"],daily_return[["上证综指","intercept"]])
results = model.fit()
print(results.summary())



