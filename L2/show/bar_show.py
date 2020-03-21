import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10,4), columns=['a','b','c','d'])
# 使用bar()生成直方图，barh()生成水平条形图（要生成一个堆积条形图，需要指定stacked=True）
df.plot.bar()
df.plot.bar(stacked=True)
df.plot.barh(stacked=True)
plt.show()