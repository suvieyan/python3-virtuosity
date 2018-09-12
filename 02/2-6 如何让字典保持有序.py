"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
from collections import OrderedDict

from random import shuffle
players = list('abcdefgh')
shuffle(players)
print(players)
od = OrderedDict()
for i,p in enumerate(players,1):
    od[p] = i
print(od)

def query_by_name(d,name):
    """
    通过名字查询
    :param d:有序字典
    :param name:查找的名字
    :return:名次
    """
    return d[name]

ret = query_by_name(od,'c')
print(ret)

from itertools import islice
# islice(range(10),3,6)# 可迭代对象的切片操作

def query_by_order(d,a,b=None):
    a -= 1
    if b is None:
        b = a+1
    return list(islice(d,a,b))
ret1 = query_by_order(od,2,4)
print(ret1)