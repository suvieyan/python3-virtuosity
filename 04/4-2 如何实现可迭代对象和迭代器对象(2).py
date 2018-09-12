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