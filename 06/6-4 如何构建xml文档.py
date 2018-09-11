"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/16'
"""
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

