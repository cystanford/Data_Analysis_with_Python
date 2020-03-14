# 字典的使用
#定义一个dictionary
score = {'guanyu':96,'zhangfei':95}

#添加一个元素
score['zhaoyun'] = 98
print(score)

#删除一个元素
score.pop('zhangfei')

#查看key是否存在
print('zhangfei' in score)

#查看一个key对应的值
print(score.get('zhangfei'))
print(score.get('dianwei',99))