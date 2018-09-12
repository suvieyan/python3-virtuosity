"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/19'
"""
# eg:('Jim',16,male,'1@1.com')
# 元组存储：提升性能和可读性
# 方案一：定义数值常量或者枚举类型
# 方案二：使用nametuple
NAME ,AGE ,SEX ,EMAIL = range(4)
student = ('Jim',16,'male','1@1.com')
def func(student):
    if student[AGE]<18:
        print(student[NAME])

# 弊端：多种类似数据难以、处理

# 枚举

from enum import IntEnum


class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3

print(StudentEnum.NAME)
print(student[StudentEnum.NAME]) # Jim

# nametuple处理
from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
print(Student)  # <class '__main__.Student'>
s2 = Student('Jim',16,'male','1@1.com')
print(s2.name)

