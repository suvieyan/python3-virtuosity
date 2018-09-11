"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
fn = 'aaa.py'
fn.endswith(('py','sh'))
import os
dirs = os.listdir('.')
print(dirs)
s = os.stat('3-1 如何拆分含有多种分隔符的字符串.py')
print(s)
print(s.st_mode)  # 33206
print(oct(s.st_mode))  # 0o100666
# 修改st_mode 就能够修改文件的权限
print(oct(s.st_mode|0o100))

# 修改文件权限
os.chmod('3-1 如何拆分含有多种分隔符的字符串.py',s.st_mode|0o100)
dirs = os.listdir('.')
print(dirs)

# state实现，不需要八进制

import stat
for fn in os.listdir('.'):
    if fn.endswith(('.py','.sh')):
        fs = os.stat(fn)
        os.chmod(fn,fs.st_mode|stat.S_IXUSR)


