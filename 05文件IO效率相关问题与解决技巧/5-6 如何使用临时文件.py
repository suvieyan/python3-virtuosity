"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/13'
"""
from tempfile import TemporaryFile,NamedTemporaryFile
# 文件当中找不到，只能查看磁盘使用量
tf = TemporaryFile() # 操作系统级别的临时文件
tf.write(b'*'*1024*1024)
tf.seek(0)
tf.read(1024)

# 自动删除
tf.close()


# open可以创建操作系统级别的文件

ntf = NamedTemporaryFile(delete=False)  # 默认自动删除，delete=False，默认不删除
# 创建的文件名字
print(ntf.name)
ntf.close()