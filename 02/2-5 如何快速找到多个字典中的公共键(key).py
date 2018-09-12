"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
from random import randint,sample
temp = 'abcde'

# 创建字典
d1 = {k:randint(1,4) for k in sample(temp,3)}
d2 = {k:randint(1,4) for k in sample(temp,3)}
d3 = {k:randint(1,4) for k in sample(temp,3)}
# 方法一：
for k in d1:
    if k in d2 and k in d3:
        print(k)
# 实际情况,给一个字典列表，找出公共的键
dl = [d1,d2,d3]
for k in dl[0]:
    if map(lambda d:k in d,dl[1:]):
        print(k)

# reduce 用法,前边的结果和后边的数字进行这个操作
from functools import reduce
ret = reduce(lambda a,b:a*b,range(1,11))
print(ret)

# set方法实现

ret1 = reduce(lambda a,b:a&b,map(dict.keys,dl))
print(ret1)