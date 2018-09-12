"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/16'
"""
class Player1:
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level

class Player2:
    __slots__ = ['uid', 'name', 'level']  # 关闭掉动态添加属性，只有这3个属性，不能再次添加了，初始化的时候分配好了
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level

# 动态添加的属性，都是在__dict__ 当中的维护的，占用的内存比较多
p1 = Player1('1','wallis','100')
import sys
size_dict = sys.getsizeof(p1.__dict__)
print(size_dict)  # 获取占据的内存：112


import tracemalloc
tracemalloc.start()
# start
# la = [Player1(1,2,3) for _ in range(100000)]  # size=16.8 MiB,
lb = [Player2(1,2,3) for _ in range(100000)]  # size=7056 KiB,
# end
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
for stat in top_stats[:10]: print(stat)