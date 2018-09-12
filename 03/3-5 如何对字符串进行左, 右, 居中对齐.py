"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
s = 'abc'
print(s.ljust(10,'*'))
print(s.rjust(10,'*'))
print(s.center(10,'*'))
format(s,'*<10')  # 星号填充，左对齐
format(s,'*>10')  # 星号填充，右对齐
format(s,'*^10')  # 星号填充，居中
# +总输出符号
f1 = format(123,'+')
print(f1)
f2 = format(-123,'>+10') # 右对齐，输出符号
print(f2)  #       -123

f2 = format(-123,'=+10')# 居中输出符号
print(f2)  #-      123

f2 = format(123,'0=+10')# 0填充居中，输出符号
print(f2)  #+000000123

d = {
    'lodDist':100.0,
    'SmallCull':0.04,
    'DistCull':500,
    'triLinear':40,
    'farcLip':477,
}
# 获取最长的键
max_length = max(map(len,d.keys()))
for k,v in d.items():
    print(k.ljust(max_length),':',v)

"""
执行结果
lodDist   : 100.0
SmallCull : 0.04
DistCull  : 500
triLinear : 40
farcLip   : 477
"""