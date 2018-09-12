"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/16'
"""
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

