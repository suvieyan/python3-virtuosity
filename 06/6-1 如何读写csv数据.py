"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/15'
"""
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
            if price and float(price) >= 80.00:
                writer.writerow(book)