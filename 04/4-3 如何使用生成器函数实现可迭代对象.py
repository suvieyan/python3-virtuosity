"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
from collections import Iterable

class PrimeNumbers(Iterable):
    """
    寻找素数范围
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b + 1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        """
        判断是素数
        小于2，都不是素数
        大于2，k，模[2,k-1],没有能够整除的，就可以
        :param k:
        :return:
        """
        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))

pn = PrimeNumbers(1, 30)
for n in pn:
    print(n)