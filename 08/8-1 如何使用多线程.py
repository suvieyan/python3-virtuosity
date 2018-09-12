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
