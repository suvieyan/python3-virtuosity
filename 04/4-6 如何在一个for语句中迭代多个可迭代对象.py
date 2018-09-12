"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
from random import randint
chinese = [randint(60,100) for _ in range(20)]
english = [randint(60,100) for _ in range(20)]
math = [randint(60,100) for _ in range(20)]

# zip 的长度等于所有的当中最小的那个
t = []
for s1,s2,s3 in zip(chinese,math,english):
    t.append(s1+s2+s3)

ret = map(lambda *args:args,chinese,math,english)
print(list(ret))
# [(99, 87, 77), (70, 84, 94), (77, 98, 89), (93, 90, 79), (63, 69, 100), (82, 86, 87), (70, 85, 89), (77, 90, 89), (80, 73, 82), (71, 82, 65), (79, 100, 81), (74, 61, 66), (78, 86, 80), (72, 98, 77), (65, 100, 76), (70, 76, 92), (60, 94, 73), (71, 97, 86), (87, 68, 95), (95, 73, 99)]

from itertools import chain
ret = chain([1,2],[3,4,5])

s = 'abc;123|XYZ;678|fgh\tjz'
from functools import reduce
ret = reduce(lambda it_s,sep:chain(*map(lambda ss:ss.split(sep),it_s)),';|\t',[s])
print(list(ret))  # ['abc', '123', 'XYZ', '678', 'fgh', 'jz']