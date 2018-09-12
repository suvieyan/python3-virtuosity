"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
# strip去掉
s = 'abc:234'
s.strip()
s.lstrip()
s.rstrip()

# 切片
s = 'abc:234'
# replace替换
s = '  abc  234  '
s.replace(' ','')

# 多种的空白符号，' ',\t
# re模块


# 字符串的translate方法
s = 'abc1234xyz'
s1 =s.translate({ord('a'):'X'})
print(s1)

s2 = s.translate(s.maketrans('abc','XYZ'))
print(s2)

# 删除字符,映射值为None就删除
s1 =s.translate({ord('a'):None})
print(s1)
# 拼音带有声调
import unicodedata
c = 'abc'
ret = unicodedata.combining(c[1])
print(ret)