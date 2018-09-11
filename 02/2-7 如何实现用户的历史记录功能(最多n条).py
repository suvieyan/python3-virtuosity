"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
# deque 双端队列
from collections import deque
from random import randint

import pickle
# 把双端队列保存到pickle,实现永久化存储
# pickle.dump(q,open('save.pkl','wb'))
# pickle.load(open('save.pkl','rb'))

def guess(n,k):
    if n ==k:
        print('猜对了，数字是%d',k)
        return True
    if n<k:
        print('猜大了，比%d小',k)
    elif n>k:
        print('猜小了，比%d大',k)
    return False

def main():
    n = randint(1,100)
    i = 1
    hq = deque([],5)# 入队之后，会pop之前入队的内容
    while True:
        num = input('【%d】请输入一个数字'%i)
        if num.isdigit():
            k = int(num)
            hq.append(k)
            pickle.dump(hq, open('save.pkl', 'wb'))
            i += 1
            if guess(n,k):
                break
        elif num == 'quite':
            break
        elif num == 'h?':
            print(list(hq))
            ret = pickle.load(open('save.pkl','rb'))
            print(ret)



if __name__ == '__main__':
    main()
