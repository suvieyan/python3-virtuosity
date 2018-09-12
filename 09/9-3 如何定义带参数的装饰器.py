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


