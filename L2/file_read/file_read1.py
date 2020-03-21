# 读取imagenet的分类ID说明

# 读文件
f = open('imagenet_class.csv')
text = f.read()
#print(text)

# 读文件，按行来读取
f = open('imagenet_class.csv')
lines = f.readlines()
#print(lines)
print(len(lines))
print(lines[0])

# 写文件
f = open('temp.txt', 'w')
f.write('hello world!')
f.close()
