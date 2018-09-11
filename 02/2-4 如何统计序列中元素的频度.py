"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/27'
"""
from random import randint
data = [randint(0,5) for _ in range(30)]
print(data)
d = dict.fromkeys(data,0)

for x in data:
    d[x] += 1
print(d)


new_dic = sorted(((v,k) for k,v in d.items()),reverse=True)

print(new_dic)

# 10000个数据，去前几个，列表很大，遍历是不好的，通常使用堆
import heapq
d1 = heapq.nlargest(3,((v,k) for k,v in d.items()))
print(d1)

# counter
from collections import Counter

c = Counter(data)
print(c.most_common(3))

# 词频统计
import re
f = open('article').read()
word_list = re.split('\W+',f)# 非字符进行分隔
# print(word_list)
c2 = Counter(word_list)
print(c2.most_common(10))