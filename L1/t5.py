# 元组的使用
tuples = ('zhangfei','65')
print(tuples[0])

# 返回字典key组成的元组
print(tuple({'zhangfei':65, 'guanyu':99}))

# 列表转化为元组
temp_list = [123, 'zhangfei', 'guanyu', 'liubei'];
temp_tuple = tuple(temp_list)
print(temp_tuple)
