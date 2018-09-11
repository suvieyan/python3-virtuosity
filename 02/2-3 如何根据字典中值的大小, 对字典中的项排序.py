"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/27'
"""
# 方案：字典中的项转换成元组、在转换成列表、再sorted
# 元组的比较,先比较第0个元素，元素相等，比较第一个元素，不等，则返回大小的true和False

t1 = (3,1)
t2 = (2,1)
print(t1>t2)

# 字典的value，可以转换成value为第一个元素的元组，然后比较
from random import randint

d1 = {k:randint(60,100) for k in 'abcdefg'}
l = [(v,k) for k,v in d1.items()]
print(sorted(l,reverse=True))

# zip函数实现
l1 = list(zip(d1.values(),d1.keys()))
print(sorted(l1,reverse=True))

# 更新到字典


# 字典直接排序
p = sorted(d1.items(),key=lambda item:item[1],reverse=True)
new_dic = {k:(i,v) for i,(k,v) in enumerate(p,1)}
print(new_dic)

