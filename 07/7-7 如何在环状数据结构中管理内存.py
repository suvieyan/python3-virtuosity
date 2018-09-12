# 弱引用库，弱引用，不增加引用计数的引用
import weakref
class Node:
    def __init__(self, data):
        self.data = data
        self._left = None
        self.right = None

    def add_right(self, node):
        """
        右边添加节点
        :param node:
        :return:
        """
        self.right = node
        node._left = weakref.ref(self)

    @property
    def left(self):
        return self._left()

    def __str__(self):
        return 'Node:<%s>' % self.data

    def __del__(self):
        print('in __del__: delete %s' % self)

def create_linklist(n):
    """
    创建链表
    :param n:
    :return:
    """
    # 创建头节点
    head = current = Node(1)
    for i in range(2, n + 1):
        node = Node(i)
        # 新创建的节点，在当前节点的右边
        current.add_right(node)
        current = node
    return head

head = create_linklist(1000)
print(head.right, head.right.left)  # Node:<2> Node:<1>
input()
head = None

import time
for _ in range(1000):
    time.sleep(1)
    print('run...')
input('wait...')
