"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
# 切片的实质
# l = [0,1,2,3,4,5,6,7]
# l[3]  # 调用l.__getitem__(3)
# l[2:8:2]
#l.__getitem__(slice(2,8,2))
#  可迭代对象的切片
from itertools import islice
f = open('/var/log/dpkg.log')
# 获取日志100-300行内容
for line in islice(f,100-1,300):
    print(line)

# islice原理，前100行还在读，不要丢掉，后边的不读

def my_islice(iterable,start,end,step=1):
    for i,x in enumerate(iterable):
        if i >= end:
            break
        if i>=start:
            yield x
print(list(my_islice(range(100,150),10,20)))