# 读取heros2.csv数据表，按照role进行groupby
import numpy as np
import pandas as pd
# 因为文件中有中文，所以采用gbk编码读取
data = pd.read_csv('heros2.csv', encoding='gbk')

result = data.groupby('role').agg([np.sum, np.mean])
print(result)

