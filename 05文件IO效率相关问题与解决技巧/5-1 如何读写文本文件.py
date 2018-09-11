"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/8'
"""
s = '我爱python'  # s是字符串
f = open('b.txt','w',encoding='gbk') # wt文本模式打开,t不写
f.write(s)
f.flush()

f = open('b.txt',encoding='gbk')
txt = f.read()
print(txt) # 我爱python
