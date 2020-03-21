# pandas读取imagenet classID表示
import pandas as pd
classes = pd.read_csv('imagenet_class.csv', sep=',', header=None)
#print(classes)
# 查看id=207的含义
print(classes[classes[0]==207])

