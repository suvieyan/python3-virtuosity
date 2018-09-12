"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/8'
"""
import struct

def find_subchunk(f, chunk_name):
    """
    找到子trunk，获取size，调到size末尾
    :param f:
    :param chunk_name:
    :return:
    """
    f.seek(12)  # 前12位头部描述信息
    while True:
        name = f.read(4) # trunkID
        chunk_size, = struct.unpack('i', f.read(4))  # subtrunksize
        print(name)

        if name == chunk_name:
            return f.tell(), chunk_size

        f.seek(chunk_size, 1)

f = open('demo.wav', 'rb')
# offset :偏移；size：文件大小
offset, size = find_subchunk(f, b'data')  # 找到data之后，后边就是数据

import numpy as np
buf = np.zeros(size//2,dtype=np.short)
f.readinto(buf)  # 把数据读取到buf
f = buf // 8 # 对文件处理到buffer当中，音频采样数据进行处理
f2 = open('out.wav','wb')
# 重新读取数据
f.seek(0)
info = f.read(offset)
f2.write(info)
buf.tofile(f2)# buf写到文件当中
f2.close()