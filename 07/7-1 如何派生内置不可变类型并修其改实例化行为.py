"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/16'
"""

class A:
    # 先new一个
    def __new__(cls, *args, **kwargs):
        print('A.__new__')
        return object.__new__(cls)

    # 再init这个对象
    def __init__(self,*args):
        print('A.__init__')

a = A(1,2)

class IntTuple(tuple):
    # 要在new的时候，进行过滤，否则在init当中，对象已经不可变了
    def __new__(cls, iterable):
        # 过滤iterable
        f_it = (e for e in iterable if isinstance(e, int) and e > 0)
        return super().__new__(cls, f_it)


int_t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(int_t)
