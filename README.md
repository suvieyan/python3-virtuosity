# python3实用编程技巧

[toc]



## 第2章数据结构与算法相关问题与解决技巧
### 2-1如何在列表、字典和集合中根据条件筛选数据

- 过滤列表当中的负数
- 筛选字典当中value高于90 的项
- 筛选集合当中能被3整除的元素

列表处理：列表解析、filter
```python
from random import randint
li = [randint(-10,10) for _ in range(10)]  # 没有用到迭代次数
# 方法一,推荐，更快
l1 = [x for x in li if x>=0 ]
print(l1)

# 方法二
l2 = filter(lambda x:x>=0,li)  # <filter object at 0x00000000028C1D68>
print(list(l2))
```
字典处理：字典解析、filter
```python
from random import randint
dic = {'student%d'%i:randint(50,100) for i in range(1,21)}
print(dic)

dic1 = {k:v for k,v in dic.items() if v>=90}
print(dic1)

dic2 = filter(lambda item:item[1]>=90,dic.items())
# print(list(dic2))  # [('student8', 100), ('student15', 93), ('student17', 98), ('student19', 92), ('student20', 90)]
print(dict(dic2))  # {'student2': 100, 'student11': 96, 'student12': 93, 'student13': 93, 'student15': 95}

```
集合：集合解析，filter
```python
from random import randint
s = {randint(0,20) for _ in range(20)}

ret = {x for x in s if x%3==0}
print(ret)
ret1 = filter(lambda x:x%3==0,s)
print(set(ret1)) # {0, 3, 12, 15, 18}
```
### 2-2如何为元组中的每个元素命名，提高程序可读性

实际案例：学生信息系统当中数据固定格式为：（名字，年龄，性别，邮箱）

比如：('Jim',16,male,'1@1.com')
元组存储节省空间，但是因为使用索引，降低程序的可读性

```python
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
```
### 2-3 如何根据字典中值的大小, 对字典中的项排序

实际案例：某班级英语成绩按照字典排序，如下：如何根据成绩高低，计算学生排名

```python
{
    "yan": 99,
    "li": 23,
    "wang":88
  ...
}
```



#### 元组排序
```python
# 方案：字典中的项转换成元组、在转换成列表、再sorted
# 元组的比较,先比较第0个元素，元素相等，比较第一个元素，不等，则返回大小的true和False

t1 = (3,1)
t2 = (2,1)
print(t1>t2)
```
#### 字典排序方法一,转换成元组、放在列表中排序
```python
# 字典的value，可以转换成value为第一个元素的元组，然后比较
from random import randint

d1 = {k:randint(60,100) for k in 'abcdefg'}
l = [(v,k) for k,v in d1.items()]
print(sorted(l,reverse=True))
```

#### 字典排序方法二：zip函数排序
```python
from random import randint

d1 = {k:randint(60,100) for k in 'abcdefg'}
l1 = list(zip(d1.values(),d1.keys()))
print(sorted(l1,reverse=True))
```
#### 字典排序方法三：字典自己的sorted
```python
from random import randint

p = sorted(d1.items(),key=lambda item:item[1],reverse=True)
new_dic = {k:(i,v) for i,(k,v) in enumerate(p,1)}
print(new_dic)
```

### 2-4 如何统计序列中元素的频度

实际案例：

- 某随机序列[12,5,6,4,7,3,5]中，找到出现次数最高的3个元素，他们出现次数是多少？
- 对一篇英文文章的单词，进行词频统计，找到出现次数最高的10个单词，他们出现的次数是多少？

#### 普通获取字典中元素的频率
```python
from random import randint
data = [randint(0,5) for _ in range(30)]
print(data)
d = dict.fromkeys(data,0)

for x in data:
    d[x] += 1
print(d)
```
#### sorted获取
```python
from random import randint
data = [randint(0,5) for _ in range(30)]
d = dict.fromkeys(data,0)
new_dic = sorted(((v,k) for k,v in d.items()),reverse=True)

print(new_dic)
```
#### 数据量很大的时候，不能遍历，采用堆的概念
```python
from random import randint
data = [randint(0,10) for _ in range(1000)]
# 10000个数据，取前几个，列表很大，遍历是不好的，通常使用堆
import heapq
d1 = heapq.nlargest(3,((v,k) for k,v in d.items()))
print(d1)

```
#### 采用counter获取
```python
from random import randint
data = [randint(0,10) for _ in range(1000)]
# counter
from collections import Counter

c = Counter(data)
print(c.most_common(3))

```
#### 词频统计的典型应用
```python
# 词频统计
import re
f = open('article').read()
word_list = re.split('\W+',f)# 非字符进行分隔
# print(word_list)
c2 = Counter(word_list)
print(c2.most_common(10))
```

### 2-5 如何快速找到多个字典中的公共键(key)

实际案例：

- 西班牙足球甲级联赛，每轮球员进球统计
- 第一轮：{'苏亚雷斯':1,'梅西':2,'本泽马':1,'C罗':3...}
- 第二轮：{'苏亚雷斯':2,'C罗':1,'格里兹曼':2,'贝尔':1...}
- 第三轮：{'苏亚雷斯':1,'托雷斯':2,'贝尔':1,'内马尔':3...}
  .....
  统计出前N轮，每场比赛都有进球的球员.

#### 方法一：
```python
from random import randint,sample
temp = 'abcde'

# 创建字典
d1 = {k:randint(1,4) for k in sample(temp,3)}
d2 = {k:randint(1,4) for k in sample(temp,3)}
d3 = {k:randint(1,4) for k in sample(temp,3)}
# 方法一：
for k in d1:
    if k in d2 and k in d3:
        print(k)
```
#### 方法二：
```python
from random import randint,sample
temp = 'abcde'

# 创建字典
d1 = {k:randint(1,4) for k in sample(temp,3)}
d2 = {k:randint(1,4) for k in sample(temp,3)}
d3 = {k:randint(1,4) for k in sample(temp,3)}
# 实际情况,给一个字典列表，找出公共的键
dl = [d1,d2,d3]
for k in dl[0]:
    if map(lambda d:k in d,dl[1:]):
        print(k)
```
#### 方法三：reduce和map
```python
from random import randint,sample
temp = 'abcde'

# 创建字典
d1 = {k:randint(1,4) for k in sample(temp,3)}
d2 = {k:randint(1,4) for k in sample(temp,3)}
d3 = {k:randint(1,4) for k in sample(temp,3)}
# reduce 用法,前边的结果和后边的数字进行这个操作
from functools import reduce
ret = reduce(lambda a,b:a*b,range(1,11))
print(ret)

# set方法实现

ret1 = reduce(lambda a,b:a&b,map(dict.keys,dl))
print(ret1)
```
### 2-6 如何让字典保持有序

实际案例

某编程竞赛系统，对参赛选手编程解题进行计时，选手完成题目后，把该选手解题用时记录到字典中，以便赛后按选手名查询成绩。（答题用时越短，成绩越优。）如： 
{‘Li’:(1, 29), ‘Jim’:(3, 36), ‘Jack’:(2, 35), …} 
比赛结束后，需按排名顺序依次打印选手成绩，如何实现？

众所周知，Python内置的dict类型是无序的，那我们要如何解决该问题呢？这时，我们可以使用collections.OrderedDict来处理该问题。代码如下：

```python
from collections import OrderedDict

from random import shuffle
players = list('abcdefgh')
shuffle(players)
print(players)
od = OrderedDict()
for i,p in enumerate(players,1):
    od[p] = i
print(od)

def query_by_name(d,name):
    """
    通过名字查询
    :param d:有序字典
    :param name:查找的名字
    :return:名次
    """
    return d[name]

ret = query_by_name(od,'c')
print(ret)

from itertools import islice
# islice(range(10),3,6)# 可迭代对象的切片操作

def query_by_order(d,a,b=None):
    a -= 1
    if b is None:
        b = a+1
    return list(islice(d,a,b))
ret1 = query_by_order(od,2,4)
print(ret1)
```
### 2-7 如何实现用户的历史记录功能(最多n条)

实际案例：

- 很多应用程序都有浏览用户的历史记录的功能：
- 浏览器可以查看最近访问过的网页
- 视频播放器可以查看最近播放过视频文件
- Shell可以查看用户输入过的命令

我们制作了一个简单的猜数字的小游戏，添加历史记录功能，显示用户最近猜过的数字，如何实现？

解决方案：

- 使用容量为n的队列存储历史记录
- 使用标准库collections中的deque,它是一个双端循环队列。
- 程序退出前，可以使用pickle将队列对象存入文件，再次运行时将其导入。

```python
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

```

## 第3章 复杂场景下字符串处理相关问题与解决技巧

### 3-1 如何拆分含有多种分隔符的字符串

```
实际案例：
        把某个字符串依据分割符号拆分不同的字段，该字段包含多种不同的分隔符
        list0 = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"
        其中 <,>,<;>,<|>,<\> 都是分隔符
```


#### 方法一：split处理,分隔，再合并，再分隔，一个一个特殊字符进行处理
```python
s = 'avsbd&6s#qwe&7890#'
def my_split(s,seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss:t.extend(ss.split(sep)),res))
        res = t
    return res

ret = my_split(s,'#&')
print(ret)

from functools import reduce
my_split2 = lambda s,seps:reduce(lambda l,sep:sum(map(lambda ss:ss.split(sep),l),[]),seps,[s])
ret1 = my_split(s,'#&')
print(ret1)
```
#### 方法二：re处理(推荐)
```python
s = 'avsbd&6s#qwe&7890#'
# 正则表达式处理
import re
ret2 = re.split('[;,|#&]',s)
print(ret2)

```

### 3-2 如何判断字符串a是否以字符串b开头或结尾

实际案例：

- 系统当中存在一系列的文件，编写程序给文件夹中所有的.sh文件和.py文件，加上用户可执行权限

方案1:使用正则表达式的^和$实现
方案2:startwith 和endwith 的处理

#### 普通修改
```python
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
```
#### state修改
```python
# state实现，不需要八进制

import stat
for fn in os.listdir('.'):
    if fn.endswith(('.py','.sh')):
        fs = os.stat(fn)
        os.chmod(fn,fs.st_mode|stat.S_IXUSR)
```

### 3-3 如何调整字符串中文本的格式

实际案例，比如log文件当中日期格式为‘yyyy-mm-dd’想变为'mm/dd/yyyy'

解决方案：re.sub()作字符串替换

```python
import re
# log是读取到的日志，可以为组命名
log = ''
re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2-\3-\1',log)
```
### 3-4 如何将多个小字符串拼接成一个大的字符串

实际案例

```python
在设计某网络程序时，我们自定义了一个基于UDP的网络协议，按照固定次序向服务器传递一系列参数： 
　　hwDetect: “<0112>” 
　　gxDepthBits “<32>” 
　　gxResolution: “<1024x768>” 
　　gxRefresh: ”<60>” 
　　fullAlpha: “<1>” 
　　lodDist: “<100.0>” 
　　DistCull: “<500.0>” 
在程序中我们将各个参数按次序收集到列表中： 
[“<0112>”, “<32>”, “<1024x768>”, “<60>”, “<1>”, “<100.0>”, “<500.0>”] 
最终我们要把各个参数拼接成一个数据报进行发送： 
“<0112><32><1024x768><60><1><100.0><500.0>>”
```



解决方案： 
- 方法一：迭代列表，连续使用‘+’操作依次拼接每一个字符串 
- 方法二：使用str.join()，更加快速的拼接列表中所有字符串

列表很长采用Join方法
```python
s1 = 'abcdefg'
s2 = '12345'
ret = s1+s2
print(ret)

# 列表相加：Join，‘；’.join(list)
```
### 3-5 如何对字符串进行左, 右, 居中对齐

实际案例

```python
某个字典存储了一系列属性值，

{
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip": 477
}

在程序中，我们想以如下工整的格式将其内容输出，如何处理？

 SmallCull : 0.04
 lodDist   : 100.0
 DistCull  : 500.0
 trilinear : 40
 farclip   : 477
```



解决方案：

方法一：使用字符串的str.ljust(), str.rjust()和str.center()进行左、右和居中对齐

方法二：使用format()，传递类似’<20’, ‘>20’, ‘^20’参数完成同样任务

####字符串的方法
```python
s = 'abc'
print(s.ljust(10,'*'))
print(s.rjust(10,'*'))
print(s.center(10,'*'))
```
#### format的方法
```python
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
```
### 3-6 如何去掉字符串中不需要的字符

实际案例

- 过滤掉用户输入中前后多余的空白字符：”　　hello　　”
- 过滤某Windows系统下某编辑文件应用在编辑文本时插入的”\r”

解决方案： 

- 方法一：字符串strip()，lstrip()和rstrip()方法去掉字符串两端，左边和右边的字符； 
- 方法二：删除单个固定位置的字符，可以使用切片+拼接的方式； 
- 方法三：字符串的replace()方法或正则表达式re.sub()删除任意位置字符。




```python
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
# 拼音有声调问题
u = u'zhào'

print u.translate({0xe0:None})
```

#### 拼音有声调的解决办法

```python
import sys
import unicodedata

u = "Zhào"

'''
　　通过使用dict.fromkeys() 方法构造一个字典，每个Unicode和音调作为键，对于的值全部为None
　　然后使用unicodedata.normalize() 将原始输入标准化为分解形式字符
　　sys.maxunicode : 给出最大Unicode代码点的值的整数，即1114111（十六进制的0x10FFFF）。
　　unicodedata.combining:将分配给字符chr的规范组合类作为整数返回。 如果未定义组合类，则返回0。
'''
s = unicodedata.normalize('NFD', u)
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
'''
　　　调用translate 函数删除所有音调
'''
print(s.translate(cmb_chrs))

```



## 第4章 对象迭代与反迭代相关问题与解决技巧

### 4-1 如何实现可迭代对象和迭代器对象(1)

实际案例

某软件要求，从网站抓取各个城市气温信息，并依次显示：

　　北京：15~20 
　　天津：17~22 
　　长春：12~18 
　　……

如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，并且浪费存储空间。我们期望以“用时访问”的策略，并且能把所有城市气温封装到一个对象里，可用for语句进行迭代。那么具体如何解决？

我们要实现可迭代对象和迭代对象，就先要了解什么是可迭代对象和迭代对象。为了说明这两个概念，我们先看如下代码：

```python
l = [1, 2, 3, 4]
s = 'abcd'

for x in s:
    print x

for i in l:
    print i
```



相信大家都能看懂上述代码并能够知道该代码的输出结果。那么我们现在来分析一下代码：代码中两个for分别循环遍历列表、字符串，其实这里的两个for循环实质上是在对列表、字符串进行迭代。因此，列表和字符串这种可以可迭代的对象称为可迭代对象。

此处以列表l为例，其迭代（循环遍历）的原理为：

1.列表l实现`__iter__()`，返回一个迭代器，所谓的迭代器就是具有next方法的对象，即迭代器对象；

2.迭代器对象在调用next方法时，迭代器对象会返回它的下一值。如果next方法被调用，但迭代器对象没有值返回，就会引发一个StopIterration异常。

```python
from collections import Iterable,Iterator
l = [1,2,3,4,5]
# 能for循环必须是可迭代对象，
# 内部调用iter方法，即调用可迭代对象内部__iter__方法，生成一个迭代器对象
# 迭代器对象调用__next__方法，最终报错stopIteration的异常

```

### 4-2 如何实现可迭代对象和迭代器对象(2)

解决方案如下： 

1. 实现一个迭代器对象WeatherIterator，`__next__`方法每次返回一个城市的气温； 
2. 实现一个可迭代对象WeatherIterable，`__iter__`方法返回一个迭代器对象。

```python
"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""

from collections import Iterator,Iterable
import requests

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        """
        next方法，获取每一个城市的天气的数据
        :return:
        """
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self,city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        ret = requests.get(url)
        data = ret.json()['data']['forecast'][0]
        return city,data['high'],data['low']

class WeatherIterable(Iterable):
    """
    可迭代对象，内部实现iter方法，调用迭代器的next方法
    """
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(w):
    """
    显示气温
    :param w:可迭代对象
    :return:
    """
    for x in w:
        print(x)

w = WeatherIterable(['北京','上海','广州','郑州']) # 可迭代对象
show(w)
```
### 4-3 如何使用生成器函数实现可迭代对象

实际案例

实现一个可迭代对象的类，它能迭代出给定范围内所有素数：

```python
pn = PrimeNumbers(1, 30)
for k in pn:
    print k
# 输出结果为：
2 3 5 7 11 13 17 19 23 29
```

解决方案：将该类的`__iter__`方法实现成生成器函数，每次yield返回一个素数。


```python
"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/7/28'
"""
from collections import Iterable

class PrimeNumbers(Iterable):
    """
    寻找素数范围
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        for k in range(self.a, self.b + 1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        """
        判断是素数
        小于2，都不是素数
        大于2，k，模[2,k-1],没有能够整除的，就可以
        :param k:
        :return:
        """
        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))

pn = PrimeNumbers(1, 30)
for n in pn:
    print(n)
```
### 4-4 如何进行反向迭代以及如何实现反向迭代

实际案例

实现一个连续浮点数发生器FloatRange（和xrange类似），根据给定范围（start，end）和步进值（step）产生一系列连续浮点数，如迭代FloatRange(3.0, 4.0. 0.2)可产生序列：

正向：3.0 -> 3.2 -> 3.4 -> 3.6 -> 3.8 -> 4.0

反向：4.0 -> 3.8 -> 3.6 -> 3.4 -> 3.2 -> 3.0

#### 列表的迭代,正向迭代：iter，反向迭代reversed
```python
l = [1,2,3,4,5]
l.reverse()  # 列表改变
l[::-1]  # 生成一个等大的新列表

# 调用reversed，必须是内部实现了__调用reversed__的
ret = reversed(l,)  # <list_reverseiterator object at 0x00000000021E9320>
for x in reversed(l):
    print(x)
```
#### 反响迭代，实现了`__reversed__`和`__iter__`的方法
```python
from decimal import Decimal

class FloatRange:
    def __init__(self, a, b, step):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step

    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step

fr = FloatRange(3.0, 4.0, 0.2)
for x in fr:
    print(x)
print('-' * 20)
for x in reversed(fr):
    print(x)

```
#### 0.2的不同
```python
>>> from decimal import Decimal
>>> Decimal(0.2)
Decimal('0.200000000000000011102230246251565404236316680908203125')
>>> Decimal('0.2')
Decimal('0.2')
>>>
```
### 4-5 如何对迭代器做切片操作

实际案例

有某个文本文件，我们想读取其中某范围的内容如100~300行之间的内容，Python中文本文件是可迭代对象，我们是否可以使用类似列表切片的方式得到一个100~300行文件内容的生成器？

#### 切片的实质调用`__getitem__`
```python
# 切片的实质
l = [0,1,2,3,4,5,6,7]
l[3]  # 调用l.__getitem__(3)
l[2:8:2]
#l.__getitem__(slice(2,8,2))
```
#### 读取日志的100-300行
```python
# islice原理，前100行还在读，不要丢掉，后边的不读
#  可迭代对象的切片
from itertools import islice
f = open('/var/log/dpkg.log')
# 获取日志100-300行内容
for line in islice(f,100-1,300):
    print(line)
```
#### 自己实现islice 的作用
```python
def my_islice(iterable,start,end,step=1):
    for i,x in enumerate(iterable):
        if i >= end:
            break
        if i>=start:
            yield x
print(list(my_islice(range(100,150),10,20)))
```
### 4-6 如何在一个for语句中迭代多个可迭代对象

实际案例

- 某班学生期末考试成绩，语文、数学和英语分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分。（并行）
- 某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，依次迭代每个列表，统计全学年成绩高于90分人数。（串行）

解决方案：

- 案例一：推荐zip,可以合并多个对象，每次迭代返回一个元祖
- 案例二：使用标准库中的[itertools.chain](https://docs.python.org/2/library/itertools.html?highlight=chain#itertools.chain)，它能将多个可迭代对象连接。



#### 并行
```python
from random import randint
chinese = [randint(60,100) for _ in range(20)]
english = [randint(60,100) for _ in range(20)]
math = [randint(60,100) for _ in range(20)]

# zip 的长度等于所有的当中最小的那个
t = []
for s1,s2,s3 in zip(chinese,math,english):
    t.append(s1+s2+s3)
```
#### map实现，注意打散
```python
from random import randint
chinese = [randint(60,100) for _ in range(20)]
english = [randint(60,100) for _ in range(20)]
math = [randint(60,100) for _ in range(20)]

ret = map(lambda *args:args,chinese,math,english)
print(list(ret)) [(99, 87, 77), (70, 84, 94), (77, 98, 89), (93, 90, 79), (63, 69, 100), (82, 86, 87), (70, 85, 89), (77, 90, 89), (80, 73, 82), (71, 82, 65), (79, 100, 81), (74, 61, 66), (78, 86, 80), (72, 98, 77), (65, 100, 76), (70, 76, 92), (60, 94, 73), (71, 97, 86), (87, 68, 95), (95, 73, 99)]

```
#### 串行chain实现
```python
from itertools import chain
ret = chain([1,2],[3,4,5])

s = 'abc;123|XYZ;678|fgh\tjz'
from functools import reduce
ret = reduce(lambda it_s,sep:chain(*map(lambda ss:ss.split(sep),it_s)),';|\t',[s])
print(list(ret))  # ['abc', '123', 'XYZ', '678', 'fgh', 'jz']
```

## 第5章 文件I/O效率相关问题与解决技巧
### 5-1 如何读写文本文件

实际案例

某文本文件编码格式已知（如UTF-8，GBK，BIG5），在Python 2.X和Python 3.X中分别如何读取该文件？

解决方案： 
- Python 2.X：写入文件前对Unicode编码，读入文件后对二进制字符串编码； 
- Python 3.X：open函数指定’t’的文本模式，encoding指定编码格式。

注：

```
　　　　　 字符串的语义发生了变化 
　　　　Python 2.X　　　　Python 3.X 
　　　——————————————– 
　　　　　str　　　　 ->　　　bytes 
​        unicode　　->　　　str
```

解决方案：

- Py2写入前进行unicode编码，读入文件后对字节进行解码
- Py3 open指定‘t’的文本模式，encoding指定编码模式


python3读取文件

```python
s = '我爱python'  # s是字符串
f = open('b.txt','w',encoding='gbk') # wt文本模式打开,t不写
f.write(s)
f.flush()

f = open('b.txt',encoding='gbk')
txt = f.read()
print(txt) # 我爱python

```
### 5-2 如何处理二进制文件

实际案例

WAV是一种音频文件的格式，音频文件为二进制文件。WAV文件由头部信息和音频采样数据构成。前44个字节为头部信息，包括声道数、采样频率和PCM位宽等，后面是音频采样数据。

解决方案： 
- open函数以二进制模式打开文件，指定mode参数为’b’ 
- 二进制数据可以用readinto读入到提取分配好的buffer中，便于数据处理 
- 解析二进制数据可以使用标准库中的struct模块的unpack方法

注：关于unpack()的参数问题，Python官方文档中并没用明确说明。因此，可查看https://www.cnblogs.com/gala/archive/2011/09/22/2184801.htm。



```python
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

```
### 5-3 如何设置文件的缓冲

实际案例

将文件内容写入到硬件设备时，使用系统调用，这类I/O操作的时间很长。为了减少I/O操作的次数，文件通常使用缓冲区，当有足够多的数据时才进行系统调用。文件的缓冲行为，分为全缓冲、行缓冲和无缓冲。

那么如何设置Python中文件对象的缓冲行为？

解决方案： 
- 全缓冲：open函数的buffering设置为大于1的整数n，n为缓冲区大小 
- 行缓冲：open函数的buffering设置为1 
- 无缓冲：open函数的buffering设置为0



#### 全缓冲
二进制打开的文件，默认缓冲区4096
```python
f = open('a.bin','wb')
f.write(b'abc')
f.write(b'efg')

linux命令：
监控文件末尾：tail -f a.bin
磁盘的驱动信息：dmeg |grep block
二进制打开文件python缓冲区大小：4096
import io
io.BufferedWriter
io.DEFAULT_BUFFER_SIZE  # 8192
缓冲区满了，才会输出

# 文件打开
io.TextIOWrapper

二进制模式下全缓冲
f = open('a.bin','wb',buffering=8192)

二进制下不缓冲
f = open('a.bin','wb',buffering=0)
f.raw.write(b'abc')

```
文本模式全缓冲，默认缓冲区8192


文件的三层模型：TextIO/ B/ Raw
行缓冲：换行输出，一直换行就是全缓冲`\n`

交互设备就是行缓冲，tty设备


文本模式下才行缓冲



### 5-4 如何将文件映射到内存

实际案例

- 在访问某些二进制文件时，希望能把文件映射到内存中，可以实现随机访问（如 framebuffer设备文件）；
- 某些嵌入式设备，寄存器被编址到内存地址空间，我们可以映射/dev/mem某范围，去访问这些寄存器；
- 如果多个进程映射同一个文件，还能实现进程通信的目的。

解决方案：使用标准库中mmap模块的mmap()函数，它需要一个打开的文件描述符作为参数。

注：本案例在Linux系统下实验。

在shell下，我们通过dd命令创建了一个数据全为0且大小为1M的二进制文件，通过od -x命令以十六进制的方式查看该文件。



```python
import mmap

f = open('/dev/fb0', 'r+b')

size = 8294400
# f.fileno() 获取文件描述符
# size 一页一页映射，mmap.PAGESIZE
m = mmap.mmap(f.fileno(), size)
# 索引写入值
m[:size//2] = b'\xff\xff\xff\x00' * (size // 4 // 2)

m.close()
f.close()

```

### 5-5 如何访问文件的状态

实际案例

在某些项目中，我们需要获得文件状态，例如：

文件的类型（普通文件、目录、符号链接和设备文件等）；
文件的访问权限；
文件的最后访问、修改和节点状态更改时间；
普通文件的大小； 
……
解决方案： 
- 系统调用：标准库中os模块下的三个系统调用stat，fstat，lstat获取文件状态； 
- 快捷函数：标准库中os.path下一些函数，使用起来更加简洁。
#### 文件类型：st_mode

```shell
>>> import os
>>> os.stat('a.txt')
posix.stat_result(st_mode=33188, st_ino=6256574, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1582968376, st_mtime=1582968376, st_ctime=1582968376)
>>> s=os.stat('a.txt')
>>> bin(s.st_mode)
'0b1000000110100100'

```

#### 文件权限

```shell
>>> import os
>>> os.stat('a.txt')
posix.stat_result(st_mode=33188, st_ino=6256574, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1582968376, st_mtime=1582968376, st_ctime=1582968376)
>>> s=os.stat('a.txt')
>>> s
posix.stat_result(st_mode=33188, st_ino=6256574, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1582968376, st_mtime=1582968376, st_ctime=1582968376)
>>> stat.S_IRUSR & s.st_mode
256
>>> stat.S_IXOTH & s.st_mode
0
```



#### 连接
硬链接(表象指向的数据块一致)：ln a.txt b.txt  

```python
# -*- coding: utf-8 -*-

import os
import stat
import time

s = os.stat('test.txt')

# 文件类型
print stat.S_ISREG(s.st_mode)

# 文件的执行权限
print s.st_mode & stat.S_IXUSR

# 文件的读权限
print s.st_mode & stat.S_IRUSR

# 文件的最后访问时间
print time.localtime(s.st_atime)

# 文件的最后修改时间
print time.localtime(s.st_mtime)

# 文件的节点状态更改时间
print time.localtime(s.st_ctime)

# 文件的大小
print s.st_size

```



### 5-6 如何使用临时文件

实际案例

某项目中，我们从传感器采集数据，每收集到1G数据后，做数据分析，最终只保存分析结果。这样很大的临时数据如果常驻内存，将消耗大量内存资源，我们可以使用临时文件存储这些临时数据（外部存储）。

临时文件不用命名，且关闭后会自动删除。

解决方案：使用标准库中tempfile下的TemporaryFile，NamedTemporaryFile。

测试使用临时文件
```python
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
```

## 第6章 数据解析与构建相关问题与解决技巧
### 6-1 如何读写csv数据

我们可以通过雅虎网址获取中国股市（深市）数据集，它以csv数据格式存储：

Date,Open,High,Low,Close,Volume,Adj Close 
2016-06-30,8.69,8.74,8.66,8.70,36220400,8.70 
2016-06-29,8.63,8.69,8.62,8.69,36961100,8.69 
2016-06-28,8.58,8.64,8.56,8.63,33651900,8.63 
……

请将平安银行这支股票，在2016年中成交量超过50000000的记录存储到另一个csv文件中。

解决方案：使用标准库中的csv模块，可以使用其中reader和writer完成csv文件读写。

#### csv文件读写
```python
import csv

with open('books.csv') as rf:
    reader = csv.reader(rf)  # reader可迭代对象
    headers = next(reader)  # 头部行内容
    with open('books_out.csv', 'w') as wf:
        writer = csv.writer(wf,delimiter= ' ') # delimiter分隔符
        writer.writerow(headers)  # 写头部
        # 循环写入
        for book in reader:
            price = book[-2]
            # 判断价格是否存在
            if price and float(price) >= 80.00:
                writer.writerow(book)
```

### 6-2 如何读写json数据

json 模块

### httpbin：测试 HTTP 请求及响应的网站
httpbin这个网站能测试 HTTP 请求和响应的各种信息，比如 cookie、ip、headers 和登录验证等，且支持 GET、POST 等多种方法，对 web 开发和测试很有帮助。它用 Python + Flask 编写，是一个开源项目。
官方网站：http://httpbin.org/开源地址：https://github.com/Runscope/httpbin
#### 读取json
```python
import requests

r = requests.get('http://www.httpbin.org/headers')
print(r)  # <Response [200]>
print(r.content)
"""
b'{\n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Host": "www.httpbin.org", \n    "User-Agent": "python-requests/2.18.1"\n  }\n}\n'
"""
print(r.text)
"""
{
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "www.httpbin.org", 
    "User-Agent": "python-requests/2.18.1"
  }
}
"""
import json
ret = json.loads(r.text)
print(ret)
"""
{'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Host': 'www.httpbin.org', 'User-Agent': 'python-requests/2.18.1'}}
"""
```



### 6-3 如何解析简单的xml文档

```python
from xml.etree import ElementTree

et = ElementTree.parse('demp.xml')
et = ElementTree.parse(open('demp.xml'))
et = ElementTree.fromstring('字符串')

root = et.getroot() # 元素对象，根元素
root.tag  # 标签
root.attrib  # 属性
list(root)  # 子元素列表
c1 = list(root)[0]
c1.get('name')
c1.text
c1.tail

c1.find('year')
c1.findall('year')

c1.iter('year')
```
### 6-4 如何构建xml文档

把CSV转换成XML



#### 代码
```python
"""
读取CSV的数据渲染到xml当中
"""
import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement

def csv_to_xml(csv_path, xml_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        headers = next(reader)

        root = Element('Data')
        root.text = '\n\t'
        root.tail = '\n'

        for row in reader:
            book = SubElement(root, 'Book')  # 子元素
            book.text = '\n\t\t'
            book.tail = '\n\t'

            for tag, text in zip(headers, row):
                e = SubElement(book, tag)
                e.text = text
                e.tail = '\n\t\t'
            e.tail = '\n\t'

        ElementTree(root).write(xml_path, encoding='utf8')  # 把xml内容写入到xml文件

csv_to_xml('books.csv', 'books.xml')
'''
结果
<?xml version='1.0' encoding='utf8'?>
<Data>
	<Book>
		<书名>python1</书名>
		<作者>wu</作者>
		<出版社>北京</出版社>
		<价格>60</价格>
	</Book>
	<Book>
		<书名>python2</书名>
		<作者>yan</作者>
		<出版社>上海</出版社>
		<价格>80</价格>
	</Book>
	</Data>

'''
```


### 6-5 如何读写excel文件

xlrd xlwt模块

```python
import xlrd, xlwt

rbook = xlrd.open_workbook('test.xlsx')  # 一个文件就是一个workbook
# rbook.sheets()  # 所有的表
rsheet = rbook.sheet_by_index(0)


k = rsheet.ncols  # 多少列
rsheet.put_cell(0, k, xlrd.XL_CELL_TEXT, '总分', None)  # 添加表头

for i in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(i, 1))  # row的每一行的，从第一列开始
    rsheet.put_cell(i, k, xlrd.XL_CELL_NUMBER, t, None)  # 每一行添加一列，类型，，总分，值


#  写入值
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)  # 传入值

for i in range(rsheet.nrows):
    for j in range(rsheet.ncols):
        # 写入的行坐标、列坐标、值
        wsheet.write(i, j, rsheet.cell_value(i, j))

wbook.save('out.xlsx')

```

## 第7章 类与对象深度问题与解决技巧
### 7-1 如何派生内置不可变类型并修其改实例化行为

自定义一种新类型的元组，对传入的可迭代对象，我们只保留其中int类型且值大于0的元素，例如IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])  => （1， 6， 3）

如何继承内置tuple实现IntTuple？

#### new 和init

```python
class A:
    # 先new一个
    def __new__(cls, *args, **kwargs):
        print('A.__new__')
        return object.__new__(cls)

    # 再init这个对象
    def __init__(self,*args):
        print('A.__init__')

a = A(1,2)
```

#### 代码

```python
class IntTuple(tuple):
    # 要在new的时候，进行过滤，否则在init当中，对象已经不可变了
    def __new__(cls, iterable):
        # 过滤iterable
        f_it = (e for e in iterable if isinstance(e, int) and e > 0)
        return super().__new__(cls, f_it)


int_t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(int_t)

```

### 7-2 如何为创建大量实例节省内存

#### 案例

某网络游戏中，定义了玩家类Player(id, name, status,....)，每有一个在线玩家，在服务器程序内有一个Player的实例，当在线人数很多时，将产生大量实例（百万级别）

**需求：**

　　如何降低这些大量实例的内存开销？

#### 解决方案

定义类的`__slots__`属性,声明实例有哪些熟悉(关闭动态绑定)

#### 代码

```python
class Player1:
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level

class Player2:
    __slots__ = ['uid', 'name', 'level']  # 关闭掉动态添加属性，只有这3个属性，不能再次添加了，初始化的时候分配好了
    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level

# 动态添加的属性，都是在__dict__ 当中的维护的，占用的内存比较多
p1 = Player1('1','wallis','100')
import sys
size_dict = sys.getsizeof(p1.__dict__)
print(size_dict)  # 获取占据的内存：112


import tracemalloc
tracemalloc.start()
# start
# la = [Player1(1,2,3) for _ in range(100000)]  # size=16.8 MiB,
lb = [Player2(1,2,3) for _ in range(100000)]  # size=7056 KiB,
# end
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
for stat in top_stats[:10]: print(stat)
```

### 7-3 如何让对象支持上下文管理

#### 案例

我们实现一个telnet客户端的类TelnetClient, 调用实例的connect(),login(),interact方法启动客户端与服务器交互，交互完毕后需要调用cleanup()方法，关闭已连接的socket，以及将操作历史记录写入文件并关闭。

能否让TelnetClient的实例支持上下文管理协议，从而代替手工调用connect()，cleanup()方法。

#### 解决方案

实现上下文管理协议，即实现类的__enter__， __exit__方法，

它们分别在with开始和结束时被调用。

#### 代码

```python
"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/16'
"""

from sys import stdin, stdout
import getpass
import telnetlib
from collections import deque

class TelnetClient:
    def __init__(self, host, port=23):
        self.host = host
        self.port = port

    def __enter__(self):
        # 进入环境之前的操作
        self.tn = telnetlib.Telnet(self.host, self.port)
        self.history = deque([])
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('IN __exit__', exc_type, exc_value, exc_tb)

        self.tn.close()
        self.tn = None

        with open('history.txt', 'a') as f:
            f.writelines(self.history)
# 异常不再向上提交
        return True

    def login(self):
        # user
        self.tn.read_until(b"login: ")
        user = input("Enter your remote account: ")
        self.tn.write(user.encode('utf8') + b"\n")

        # password
        self.tn.read_until(b"Password: ")
        password = getpass.getpass()
        self.tn.write(password.encode('utf8') + b"\n")
        out = self.tn.read_until(b'$ ')
        stdout.write(out.decode('utf8'))

    def interact(self):
        while True:
            cmd = stdin.readline()
            if not cmd:
                break

            self.history.append(cmd)
            self.tn.write(cmd.encode('utf8'))
            out = self.tn.read_until(b'$ ').decode('utf8')

            stdout.write(out[len(cmd)+1:])
            stdout.flush()

# client = TelnetClient('192.168.0.105')
# client.connect()
# client.login()
# client.interact()
# client.cleanup()

with TelnetClient('10.0.0.103') as client:
    raise Exception('TEST')
    client.login()
    client.interact()

print('END')


```

### 7-4 如何创建可管理的对象属性

#### 实际案例

在面向对象编程中，我们把方法（函数）看作对象的接口。

直接访问对象的属性可能是不安全的，或设计上不够灵活。

但是使用调用方法在形式上不如访问属性简洁。

circle.setRadius(5.0) #繁

circle.radius = 5.0

能否在形式上是属性访问，但实际上调用方法？



#### 解决方案:property装饰器

使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问

#### 代码

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return round(self.radius, 1)

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('wronge type')
        self.radius = radius

    @property
    def S(self):
        return self.radius ** 2 * math.pi

    @S.setter
    def S(self, s):
        self.radius = math.sqrt(s / math.pi)

    R = property(get_radius, set_radius)

c = Circle(5.712)

c.S = 99.88
print(c.S)
print(c.R)

#print(c.get_radius())
#c.radius = '31.98'


```



### 7-5 如何让类支持比较操作

#### 实际案例

有时我们希望自定义类的实例间可以使用<, <=, >, >=, ==, !=符号进行比较，我们自定义比较的行为。

比如，有一个矩形，比较两个矩形的实例时，我们希望比较的是面积。

比如，有一个矩形和一个圆形，我们希望比较一个矩形实例和一个圆形实例，

我们希望它们比较的是面积。

#### 解决方案

（1）比较运算符重载，需要实现以下方法

`__lt__`, `__le__`, `__gt__`, `__ge__`, `__eq__`, `__ne__`

（2）使用标准库functions下的装饰器，total_ordering可以简化此过程。

1.int的比较，实际调用`__gt__`和`__lt__`进行比较的

2.字符串比较,比较的是字符的ASCII码

```shell
>>> s1 = 'abc'
>>> s2 = 'abd'
>>> s1>s2
False
```

3.集合比较：比较的是一种包含的关系

```shell
>>> {1,2,3}>{4}
False
>>> {1,2,3}<{4}
False
>>> {1,2,3}<{1}
False
>>> {1,2,3}>{1}
True
```

#### 代码：

```python
from functools import total_ordering

from abc import ABCMeta, abstractclassmethod

@total_ordering
class Shape(metaclass=ABCMeta):
    @abstractclassmethod
    def area(self):
        pass

    def __lt__(self, obj):
        print('__lt__', self, obj)
        return self.area() < obj.area()

    def __eq__(self, obj):
        return self.area() == obj.area()

    def __gt__(self, obj):
        print('__gt__', self, obj)
        return self.area() > obj.area()

class Rect(Shape):
    """
    矩形类
    """
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return 'Rect:(%s, %s)' % (self.w, self.h)

import math
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi


rect1 = Rect(6, 9) # 54
rect2 = Rect(7, 8) # 56
c = Circle(8)

print(rect1 < c)  # 调用lt方法
print(c > rect2)  # 调用gt方法

```





### 7-6 如何使用描述符对实例属性做类型检查

#### 实际案例

在某些项目中，我们实现一些类，并希望能像静态类型语言(C,C++,Java)那样对它们的

实例属性做类型检查：

```Python
p = Persosn()
p.name = 'tom' #必须是str
p.age = 18       #必须是int
```



要求：

（1）可对实例属性指定类型

（2）赋予不正确类型时抛出异常

#### 解决方案

使用描述符来实现需要类型检查的属性：分别实现`__get__`, `__set__`, `__delete__`方法，在`__set__`中使用isinstance函数做类型检查

 

#### 代码

为实例赋值的本质：`a.__dict__['x'] = value`

```python
class Attr:
    def __init__(self, key, type_):
        self.key = key
        self.type_ = type_

    def __set__(self, instance, value):
        print('in __set__')
        if not isinstance(value, self.type_):
            raise TypeError('must be %s' % self.type_)
        instance.__dict__[self.key] = value

    def __get__(self, instance, cls):
        print('in __get__', instance, cls)
        return instance.__dict__[self.key]

    def __delete__(self, instance):
        print('in __del__', instance)
        del instance.__dict__[self.key]

class Person:
    name = Attr('name', str)
    age = Attr('age', int)

p = Person()
p.name = 'liushuo'
p.age = '32'

执行结果：
in __set__
Traceback (most recent call last):
in __set__
  File "D:/pycharm-projects/Python3实用编程/07/7-6 如何使用描述符对实例属性做类型检查.py", line 26, in <module>
    p.age = '32'
  File "D:/pycharm-projects/Python3实用编程/07/7-6 如何使用描述符对实例属性做类型检查.py", line 9, in __set__
    raise TypeError('must be %s' % self.type_)
TypeError: must be <class 'int'>


```





### 7-7 如何在环状数据结构中管理内存

#### 实际案例：

在python中，垃圾回收器通过引用计数来回收垃圾对象，但某些环状数据结构（树，图....），存在对象间的循环引用，比如树的父节点引用子节点，子节点也同时引用父节点。此时同时del掉引用父子节点，两个对象不能被立即回收。

如何解决此类的内存管理内存管理问题？

#### 解决方案

使用标准库weakref，它可以创建一种能访问对象但不增加引用计数的对象。

#### 知识储备：引用计数为0，立即删除

```python
class A:
    def __del__(self):
        print('in __del__')

a = A()
a2 = a  # 引用计数为1
a2 = 1  # a2重新赋值，a，引用计数为0,就立即被删除了
```

#### 代码：

```python
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
print(head.right, head.right.left)
input()
head = None

import time
for _ in range(1000):
    time.sleep(1)
    print('run...')
input('wait...')

```



### 7-8 如何通过实例方法名字的字符串调用方法

#### 实际案例

在某项目当中,我们使用了三个不同的图形库,Circle, Triangle, Rectangle.他们都有一个获取图形面积的接口,但是接口名字不同.我们实现一个统一的获取面积的函数,使用每种方法名字进行尝试,调用相应类的接口.



#### 解决方案

1.使用内置`getter`,通过m,ingz获取方法,然后调用

2,使用标准库operator下的methodcaller函数调用

#### 代码：

```python
"""
三个图形获取面积的接口不一样，如果形状有这个属性
"""
# from lib1 import Circle
# from lib2 import Triangle
# from lib3 import Rectangle
from operator import methodcaller

class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r **2 *3.14

class Triangle:
    def __init__(self,a,b,c):
        self.a,self.b,self.c = a,b,c

    def get_area(self):
        a, b, c = self.a,self.b,self.c
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))*0.5

class Rectangle:
    def __init__(self,a,b):
        self.a,self.b = a,b

    def getArea(self):
        return self.a*self.b

def get_area(shape, method_name = ['area', 'get_area', 'getArea']):

    for name in method_name:
        if hasattr(shape, name):
            # methodcaller（方法，参数）（谁调用）
            return methodcaller(name)(shape)
        # f = getattr(shape, name, None)
        # if f:
        #     return f()


shape1 = Circle(1)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(4, 6)

shape_list = [shape1, shape2, shape3]
# 获得面积列表
area_list = list(map(get_area, shape_list))
print(area_list)
```





## 第8章 多线程并发相关问题与解决技巧

### 8-1 如何使用多线程

使用多线程提高并发效率

#### 解决方案

#### 代码：

```python
import requests
import base64
from io import StringIO
import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement

USERNAME = b'7f304a2df40829cd4f1b17d10cda0304'
PASSWORD = b'aff978c42479491f9541ace709081b99'

def download_csv(page_number):
    """
    下载csv数据
    :param page_number:
    :return:
    """
    print('download csv data [page=%s]' % page_number)
    url = "http://api.intrinio.com/prices.csv?ticker=AAPL&hide_paging=true&page_size=200&page_number=%s" % page_number
    auth = b'Basic ' + base64.b64encode(b'%s:%s' % (USERNAME, PASSWORD))
    headers = {'Authorization' : auth}
    response = requests.get(url, headers=headers)

    if response.ok:
        # 保存到内存
        return StringIO(response.text)

def csv_to_xml(csv_file, xml_path):
    """
    csv文件转换成xml
    :param csv_file:
    :param xml_path:
    :return:
    """
    print('Convert csv data to %s' % xml_path)
    reader = csv.reader(csv_file)
    headers = next(reader)

    root = Element('Data')
    root.text = '\n\t'
    root.tail = '\n'

    for row in reader:
        book = SubElement(root, 'Row')
        book.text = '\n\t\t'
        book.tail = '\n\t'

        for tag, text in zip(headers, row):
            e = SubElement(book, tag)
            e.text = text
            e.tail = '\n\t\t'
        e.tail = '\n\t'

    ElementTree(root).write(xml_path, encoding='utf8')

def download_and_save(page_number, xml_path):
    """
    调用上边的方法
    :param page_number:
    :param xml_path:
    :return:
    """
    # IO
    csv_file = None
    while not csv_file:
        csv_file = download_csv(page_number)
    # CPU
    csv_to_xml(csv_file, 'data%s.xml' % page_number)

from threading import Thread
class MyThread(Thread):
    """
    多线程
    """
    def __init__(self, page_number, xml_path):
        super().__init__()
        self.page_number = page_number
        self.xml_path = xml_path

    def run(self):
        download_and_save(self.page_number, self.xml_path)

if __name__ == '__main__':
    import time
    t0 = time.time()
    thread_list = []
    for i in range(1, 6):
        t = MyThread(i, 'data%s.xml' % i)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()
    # for i in range(1, 6):
    #      download_and_save(i, 'data%s.xml' % i)
    print(time.time() - t0)
    print('main thread end.')

```



### 8-2 如何线程间通信

使用队列线程间通信

#### 代码：

```python
import requests
import base64
from io import StringIO
import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement
from threading import Thread

USERNAME = b'7f304a2df40829cd4f1b17d10cda0304'
PASSWORD = b'aff978c42479491f9541ace709081b99'


class DownloadThread(Thread):
    def __init__(self, page_number, queue):
        super().__init__()
        self.page_number = page_number
        self.queue = queue

    def run(self):
        csv_file = None
        while not csv_file:
            csv_file = self.download_csv(self.page_number)
        self.queue.put((self.page_number, csv_file))

    def download_csv(self, page_number):
        print('download csv data [page=%s]' % page_number)
        url = "http://api.intrinio.com/prices.csv?ticker=AAPL&hide_paging=true&page_size=200&page_number=%s" % page_number
        auth = b'Basic ' + base64.b64encode(b'%s:%s' % (USERNAME, PASSWORD))
        headers = {'Authorization' : auth}
        response = requests.get(url, headers=headers)

        if response.ok:
            return StringIO(response.text)

class ConvertThread(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            page_number, csv_file = self.queue.get()
            self.csv_to_xml(csv_file, 'data%s.xml' % page_number)

    def csv_to_xml(self, csv_file, xml_path):
        print('Convert csv data to %s' % xml_path)
        reader = csv.reader(csv_file)
        headers = next(reader)

        root = Element('Data')
        root.text = '\n\t'
        root.tail = '\n'

        for row in reader:
            book = SubElement(root, 'Row')
            book.text = '\n\t\t'
            book.tail = '\n\t'

            for tag, text in zip(headers, row):
                e = SubElement(book, tag)
                e.text = text
                e.tail = '\n\t\t'
            e.tail = '\n\t'

        ElementTree(root).write(xml_path, encoding='utf8')


from queue import Queue

if __name__ == '__main__':
    queue = Queue()
    thread_list = []
    for i in range(1, 6):
        t = DownloadThread(i, queue)
        t.start()
        thread_list.append(t)

    convert_thread = ConvertThread(queue)
    convert_thread.start()

    for t in thread_list:
        t.join()
    print('main thread end.')
```



### 8-3 如何在线程间进行事件通知

Event:wait 等待事件, set通知事件

#### 代码

```python
import requests
import base64
from io import StringIO
import csv
from xml.etree.ElementTree import ElementTree, Element, SubElement
from threading import Thread
from queue import Queue
import tarfile
import os

USERNAME = b'7f304a2df40829cd4f1b17d10cda0304'
PASSWORD = b'aff978c42479491f9541ace709081b99'

class DownloadThread(Thread):
    def __init__(self, page_number, queue):
        super().__init__()
        self.page_number = page_number
        self.queue = queue

    def run(self):
        csv_file = None
        while not csv_file:
            csv_file = self.download_csv(self.page_number)
        self.queue.put((self.page_number, csv_file))

    def download_csv(self, page_number):
        print('download csv data [page=%s]' % page_number)
        url = "http://api.intrinio.com/prices.csv?ticker=AAPL&hide_paging=true&page_size=100&page_number=%s" % page_number
        auth = b'Basic ' + base64.b64encode(b'%s:%s' % (USERNAME, PASSWORD))
        headers = {'Authorization' : auth}
        response = requests.get(url, headers=headers)

        if response.ok:
            return StringIO(response.text)

class ConvertThread(Thread):
    def __init__(self, queue, c_event, t_event):
        super().__init__()
        self.queue = queue
        self.c_event = c_event
        self.t_event = t_event

    def run(self):
        count = 0
        while True:
            page_number, csv_file = self.queue.get()
            if page_number == -1:
                self.c_event.set()
                self.t_event.wait()
                break

            self.csv_to_xml(csv_file, 'data%s.xml' % page_number)
            count += 1
            if count == 2:
                count = 0
                # 通知转换完成
                self.c_event.set()
                
                # 等待打包完成
                self.t_event.wait()
                self.t_event.clear()
                

    def csv_to_xml(self, csv_file, xml_path):
        print('Convert csv data to %s' % xml_path)
        reader = csv.reader(csv_file)
        headers = next(reader)

        root = Element('Data')
        root.text = '\n\t'
        root.tail = '\n'

        for row in reader:
            book = SubElement(root, 'Row')
            book.text = '\n\t\t'
            book.tail = '\n\t'

            for tag, text in zip(headers, row):
                e = SubElement(book, tag)
                e.text = text
                e.tail = '\n\t\t'
            e.tail = '\n\t'

        ElementTree(root).write(xml_path, encoding='utf8')

class TarThread(Thread):
    def __init__(self, c_event, t_event):
        super().__init__(daemon=True)
        self.count = 0
        self.c_event = c_event
        self.t_event = t_event

    def run(self):
        while True:
            # 等待足够的xml
            self.c_event.wait()
            self.c_event.clear()
            
            print('DEBUG')
            # 打包
            self.tar_xml()

            # 通知打包完成
            self.t_event.set()

    def tar_xml(self):
        self.count += 1
        tfname = 'data%s.tgz' % self.count
        print('tar %s...' % tfname)
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()

        if not tf.members:
            os.remove(tfname)

from threading import Event

if __name__ == '__main__':
    queue = Queue()
    c_event= Event()
    t_event= Event()
    thread_list = []
    for i in range(1, 15):
        t = DownloadThread(i, queue)
        t.start()
        thread_list.append(t)

    convert_thread = ConvertThread(queue, c_event, t_event)
    convert_thread.start()

    tar_thread = TarThread(c_event, t_event)
    tar_thread.start()
    
    # 等待下载线程结束
    for t in thread_list:
        t.join()

    # 通知Convert线程退出
    queue.put((-1, None))

    # 等待转换线程结束
    convert_thread.join()
    print('main thread end.')

```



### 8-4 如何使用线程本地数据



threading.local函数可以创建线程本地数据空间,其下属性对每个线程独立存在,

#### 解决方案

#### 代码

```python
"""
Python安装OpenCV依赖包
pip install --upgrade setuptools
pip install numpy Matplotlib
pip install opencv-python
"""
import os, cv2, time, struct, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer, ThreadingTCPServer
from threading import Thread, RLock
from select import select

class JpegStreamer(Thread):
    """
    使用摄像头采集数据
    """
    def __init__(self, camera):
        super().__init__()
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self, pr):
        self.lock.acquire()
        pw = self.pipes.pop(pr)
        self.lock.release()
        os.close(pr)
        os.close(pw)

    def capture(self):
        """
        从摄像头获取数据
        :return:
        """
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.tostring()

    def send_frame(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.values(), [], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send_frame(frame)

class JpegRetriever:
    """
    从JpegStreamer获取数据
    """
    def __init__(self, streamer):
        self.streamer = streamer
        self.local = threading.local()

    def retrieve(self):
        while True:
            ns = os.read(self.local.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.local.pipe, n)
            yield data

    def __enter__(self):
        if hasattr(self.local, 'pipe'):
            raise RuntimeError()

        self.local.pipe = streamer.register()
        return self.retrieve()

    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True

class WebHandler(BaseHTTPRequestHandler):
    retriever = None

    @staticmethod
    def set_retriever(retriever):
        WebHandler.retriever = retriever

    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')

        if self.path != '/':
            return

        self.send_response(200)
        self.send_header('Content-type', 'multipart/x-mixed-replace;boundary=jpeg_frame')
        self.end_headers()

        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)

    def send_frame(self, frame):
        sh  = b'--jpeg_frame\r\n'
        sh += b'Content-Type: image/jpeg\r\n'
        sh += b'Content-Length: %d\r\n\r\n' % len(frame)
        self.wfile.write(sh)
        self.wfile.write(frame)

from concurrent.futures import ThreadPoolExecutor
class ThreadingPoolTCPServer(ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True, thread_n=100):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate=True)

        self.executor = ThreadPoolExecutor(thread_n)

    def process_request(self, request, client_address):
        self.executor.submit(self.process_request_thread, request, client_address)

if __name__ == '__main__':
    # 创建Streamer，开启摄像头采集。
    streamer = JpegStreamer(0)
    streamer.start()

    # http服务创建Retriever
    retriever = JpegRetriever(streamer)
    WebHandler.set_retriever(retriever)

    # 开启http服务器
    HOST = 'localhost'
    PORT = 9000
    print('Start server... (http://%s:%s)' % (HOST, PORT))
    httpd = ThreadingPoolTCPServer((HOST, PORT), WebHandler, thread_n=3)
    #httpd = ThreadingTCPServer((HOST, PORT), WebHandler)
    httpd.serve_forever()

```



### 8-5 如何使用线程池



### 8-6 如何使用多进程

#### 实际案例

#### 解决方案

#### 代码:

```python
"""
Python安装OpenCV依赖包
pip install --upgrade setuptools
pip install numpy Matplotlib
pip install opencv-python
"""
import os, cv2, time, struct, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer, ThreadingTCPServer
from threading import Thread, RLock
from select import select

class JpegStreamer(Thread):
    """
    使用摄像头采集数据
    """
    def __init__(self, camera):
        super().__init__()
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self, pr):
        self.lock.acquire()
        pw = self.pipes.pop(pr)
        self.lock.release()
        os.close(pr)
        os.close(pw)

    def capture(self):
        """
        从摄像头获取数据
        :return:
        """
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.tostring()

    def send_frame(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.values(), [], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send_frame(frame)

class JpegRetriever:
    """
    从JpegStreamer获取数据
    """
    def __init__(self, streamer):
        self.streamer = streamer
        self.local = threading.local()

    def retrieve(self):
        while True:
            ns = os.read(self.local.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.local.pipe, n)
            yield data

    def __enter__(self):
        if hasattr(self.local, 'pipe'):
            raise RuntimeError()

        self.local.pipe = streamer.register()
        return self.retrieve()

    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True

class WebHandler(BaseHTTPRequestHandler):
    retriever = None

    @staticmethod
    def set_retriever(retriever):
        WebHandler.retriever = retriever

    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')

        if self.path != '/':
            return

        self.send_response(200)
        self.send_header('Content-type', 'multipart/x-mixed-replace;boundary=jpeg_frame')
        self.end_headers()

        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)

    def send_frame(self, frame):
        sh  = b'--jpeg_frame\r\n'
        sh += b'Content-Type: image/jpeg\r\n'
        sh += b'Content-Length: %d\r\n\r\n' % len(frame)
        self.wfile.write(sh)
        self.wfile.write(frame)

from concurrent.futures import ThreadPoolExecutor
class ThreadingPoolTCPServer(ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True, thread_n=100):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate=True)

        self.executor = ThreadPoolExecutor(thread_n)

    def process_request(self, request, client_address):
        self.executor.submit(self.process_request_thread, request, client_address)

if __name__ == '__main__':
    # 创建Streamer，开启摄像头采集。
    streamer = JpegStreamer(0)
    streamer.start()

    # http服务创建Retriever
    retriever = JpegRetriever(streamer)
    WebHandler.set_retriever(retriever)

    # 开启http服务器
    HOST = 'localhost'
    PORT = 9000
    print('Start server... (http://%s:%s)' % (HOST, PORT))
    httpd = ThreadingPoolTCPServer((HOST, PORT), WebHandler, thread_n=3)
    #httpd = ThreadingTCPServer((HOST, PORT), WebHandler)
    httpd.serve_forever()

```



## 第9章 装饰器使用问题与技巧

### 9-1 如何使用函数装饰器

多个函数添加相同的功能

#### 解决方案:装饰器

#### 代码



```python

def memo(func):
    cache = {}
    def wrap(*args):
        res = cache.get(args)
        if not res:
            res = cache[args] = func(*args)
        return res

    return wrap



# [题目1] 斐波那契数列（Fibonacci sequence）:
# F(0)=1，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2）
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 求数列第n项的值？
@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# fibonacci = memo(fibonacci)
print(fibonacci(50))

# [题目2] 走楼梯问题
# 有100阶楼梯, 一个人每次可以迈1~3阶. 一共有多少走法？ 
@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step, steps)
    return count

print(climb(100, (1,2,3)))

```



### 9-2 如何为被装饰的函数保存元数据

#### 实际案例

#### 解决方案:functools的wraps

#### 代码

```python
from functools import update_wrapper, wraps


def my_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        '''某功能包裹函数'''

        # 此处实现某种功能
        # ...

        return func(*args, **kwargs)
    return wrap

@my_decorator
def xxx_func(a, b):
    '''
    xxx_func函数文档：
    ...
    '''
    pass

print(xxx_func.__name__)
print(xxx_func.__doc__)

```



### 9-3 如何定义带参数的装饰器



#### 实际案例

实现一个装饰器,检查指定的参数类型

#### 代码

```python
import inspect
# inspect 观察对象的内部属性

def type_assert(*ty_args, **ty_kwargs):
    def decorator(func):
        # A...
        func_sig = inspect.signature(func)  # 对象的
        bind_type = func_sig.bind_partial(*ty_args, **ty_kwargs).arguments  # 以参数为例建立字典
        
        def wrap(*args, **kwargs):
            # B...
            for name, obj in func_sig.bind(*args, **kwargs).arguments.items():
                type_ = bind_type.get(name)
                if type_:
                    if not isinstance(obj, type_):
                        raise TypeError('%s must be %s' % (name, type_))
            return func(*args, **kwargs)
        return wrap
    return decorator



@type_assert(c=str)
def f(a, b, c):
    pass

# f(5, 10, 5.3)
f(5, 10, 'yan')


```



### 9-4 如何实现属性可修改的函数装饰器

#### 实际案例

在某项目中， 程序运行效率差， 为了分析哪些函数执行耗时，使用装饰器



#### 解决方案

Nonlocal 访问嵌套作用域的变量

#### 代码

```python
import time
import logging

def warn_timeout(timeout):
    def decorator(func):
        #_timeout = [timeout]
        def wrap(*args, **kwargs):
            #timeout = _timeout[0]
            t0 = time.time()
            res = func(*args, **kwargs)
            used = time.time() - t0
            if used > timeout:
                logging.warning('%s: %s > %s', func.__name__, used, timeout)
            return res
        def set_timeout(new_timeout):
            nonlocal timeout
            timeout = new_timeout
            #_timeout[0] = new_timeout
        wrap.set_timeout = set_timeout
        return wrap
    return decorator

import random
@warn_timeout(1.5)
def f(i):
    print('in f [%s]' % i)
    while random.randint(0, 1):
        time.sleep(0.6)

for i in range(30):
    f(i)

f.set_timeout(1)  # 修改装饰器参数
for i in range(30):
    f(i)

```

### 9-5 如何在类中定义装饰器

#### 实际案例

实现一个能将函数调用信息记录到日志的装饰器：

1.把每次函数的调用时间，执行时间， 调用次数写入日志

2.对装饰器函数分组， 调用信息记录到不同的日志

3.动态修改参数，比如日志格式

4.动态打开关闭日志输出功能



#### 解决方案

类的实例方法作为装饰

#### 代码

```python
import time
import logging

DEFAULT_FORMAT = '%(func_name)s -> %(call_time)s\t%(used_time)s\t%(call_n)s'


class CallInfo:
    def __init__(self, log_path, format_=DEFAULT_FORMAT, on_off=True):
        self.log = logging.getLogger(log_path)
        self.log.addHandler(logging.FileHandler(log_path))
        self.log.setLevel(logging.INFO)
        self.format = format_
        self.is_on = on_off

    # 装饰器方法
    def info(self, func):
        _call_n = 0

        def wrap(*args, **kwargs):
            func_name = func.__name__
            call_time = time.strftime('%x %X', time.localtime())
            t0 = time.time()
            res = func(*args, **kwargs)
            used_time = time.time() - t0
            nonlocal _call_n
            _call_n += 1
            call_n = _call_n
            if self.is_on:
                self.log.info(self.format % locals())
            return res

        return wrap

    def set_format(self, format_):
        self.format = format_

    def turn_on_off(self, on_off):
        self.is_on = on_off


# 测试代码
import random

ci1 = CallInfo('mylog1.log')
ci2 = CallInfo('mylog2.log')


@ci1.info
def f():
    sleep_time = random.randint(0, 6) * 0.1
    time.sleep(sleep_time)


@ci1.info
def g():
    sleep_time = random.randint(0, 8) * 0.1
    time.sleep(sleep_time)


@ci2.info
def h():
    sleep_time = random.randint(0, 7) * 0.1
    time.sleep(sleep_time)


for _ in range(30):
    random.choice([f, g, h])()

ci1.set_format('%(func_name)s -> %(call_time)s\t%(call_n)s')
for _ in range(30):
    random.choice([f, g])()

```




