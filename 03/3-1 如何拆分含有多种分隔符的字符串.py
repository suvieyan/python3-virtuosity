"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
s = 'avsbd&6s#qwe&7890#'
def my_split(s,seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss:t.extend(ss.split(sep)),res))
        res = t
    return res

ret = my_split(s,'#&')
print(ret)

from functools import reduce
my_split2 = lambda s,seps:reduce(lambda l,sep:sum(map(lambda ss:ss.split(sep),l),[]),seps,[s])
ret1 = my_split(s,'#&')
print(ret1)
# 正则表达式处理
import re
ret2 = re.split('[;,|#&]',s)
print(ret2)
