"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
# l = [1,2,3,4,5]
# l.reverse()  # 列表改变
# l[::-1]  # 生成一个等大的新列表

# 调用reversed，必须是内部实现了__调用reversed__的
# ret = reversed(l,)  # <list_reverseiterator object at 0x00000000021E9320>
# for x in reversed(l):
#     print(x)

from decimal import Decimal

class FloatRange:
    def __init__(self, a, b, step):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step

    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step

fr = FloatRange(3.0, 4.0, 0.2)
for x in fr:
    print(x)
print('-' * 20)
for x in reversed(fr):
    print(x)
