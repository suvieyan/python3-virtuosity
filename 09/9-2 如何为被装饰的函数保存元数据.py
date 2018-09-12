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
