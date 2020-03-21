# 使用time处理时间
import time
timestamp = time.time()
print("当前时间戳为:", timestamp)
# 转化为struct_time类型
localtime = time.localtime(timestamp)
print("本地时间为 :", localtime)
print(type(localtime))


import datetime
date = datetime.date(2020, 3, 1)
print(date)

time_now = datetime.datetime.now()
delta1 = datetime.timedelta(days=30)
print(time_now)
print(time_now + delta1)
