"""
三个图形获取面积的接口不一样，如果形状有这个属性
"""
# from lib1 import Circle
# from lib2 import Triangle
# from lib3 import Rectangle
from operator import methodcaller

class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r **2 *3.14

class Triangle:
    def __init__(self,a,b,c):
        self.a,self.b,self.c = a,b,c

    def get_area(self):
        a, b, c = self.a,self.b,self.c
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))*0.5

class Rectangle:
    def __init__(self,a,b):
        self.a,self.b = a,b

    def getArea(self):
        return self.a*self.b

def get_area(shape, method_name = ['area', 'get_area', 'getArea']):

    for name in method_name:
        if hasattr(shape, name):
            # methodcaller（方法，参数）（谁调用）
            return methodcaller(name)(shape)
        # f = getattr(shape, name, None)
        # if f:
        #     return f()


shape1 = Circle(1)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(4, 6)

shape_list = [shape1, shape2, shape3]
# 获得面积列表
area_list = list(map(get_area, shape_list))
print(area_list)
