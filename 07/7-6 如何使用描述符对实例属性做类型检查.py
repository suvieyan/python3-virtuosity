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

