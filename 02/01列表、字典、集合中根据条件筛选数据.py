"""
__title__ = ''
__au；thor__ = 'Yan'
__mtime__ = '2018/7/19'
"""

# 列表：列表解析，filter
# 字典：字典解析
# 集合：集合解析

from random import randint
li = [randint(-10,10) for _ in range(10)]  # 没有用到迭代次数
# 方法一,推荐，更快
l1 = [x for x in li if x>=0 ]
print(l1)

# 方法二
l2 = filter(lambda x:x>=0,li)  # <filter object at 0x00000000028C1D68>
print(list(l2))

dic = {'student%d'%i:randint(50,100) for i in range(1,21)}
print(dic)

dic1 = {k:v for k,v in dic.items() if v>=90}
print(dic1)

dic2 = filter(lambda item:item[1]>=90,dic.items())
# print(list(dic2))  # [('student8', 100), ('student15', 93), ('student17', 98), ('student19', 92), ('student20', 90)]
print(dict(dic2))  # {'student2': 100, 'student11': 96, 'student12': 93, 'student13': 93, 'student15': 95}



s = {randint(0,20) for _ in range(20)}

ret = {x for x in s if x%3==0}
print(ret)
ret1 = filter(lambda x:x%3==0,s)
print(set(ret1)) # {0, 3, 12, 15, 18}