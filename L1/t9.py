import numpy as np

# 连续数组的创建：arange 或 linspace
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print('x1=', x1)
print('x2=', x2)

print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))