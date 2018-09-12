from functools import total_ordering

from abc import ABCMeta, abstractclassmethod

@total_ordering
class Shape(metaclass=ABCMeta):
    @abstractclassmethod
    def area(self):
        pass

    def __lt__(self, obj):
        print('__lt__', self, obj)
        return self.area() < obj.area()

    def __eq__(self, obj):
        return self.area() == obj.area()

    def __gt__(self, obj):
        print('__gt__', self, obj)
        return self.area() > obj.area()

class Rect(Shape):
    """
    矩形类
    """
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return 'Rect:(%s, %s)' % (self.w, self.h)

import math
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi


rect1 = Rect(6, 9) # 54
rect2 = Rect(7, 8) # 56
c = Circle(8)

print(rect1 < c)  # 调用lt方法
print(c > rect2)  # 调用gt方法
