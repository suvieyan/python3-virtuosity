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
