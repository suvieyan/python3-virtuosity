"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
from collections import Iterable,Iterator
l = [1,2,3,4,5]
# 能for循环必须是可迭代对象，
# 内部调用iter方法，即调用可迭代对象内部__iter__方法，生成一个迭代器对象
# 迭代器对象调用__next__方法，最终报错stopIteration的异常


