import functools


# 1.
def log(func):
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


# 2.
# log2
# now = log('log2')(now) = decorator(now) = wrapper
def log2(text='log2'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'calling with input {text} to function {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator


# 3.
def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


# 4.
def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'calling with input {text} to function {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator


# 5
class Log5:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'log 5 calling {self.func.__name__}')
        return self.func(*args, **kwargs)


# 6
class Log6:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'log 6 calling {self.func.__name__}')
        return self.func(*args, **kwargs)


# singleton
class Singleton:
    def __init__(self, a_class):
        self.a_class = a_class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.a_class(*args, **kwargs)  # 注意要还给人家实例
        return self.instance


# @log2()
@log4('log4')
# @Log5
def now(input):
    print('it is now1')
    print(f'input is {input}')


now('hector')  # now = log(now) = wrapper, wrapper is the closure, so it knows which is the function


@Singleton
class A:
    def __init__(self, mark):
        print('i am a')
        self.mark = mark

    def my_method(self):
        print(f'mark is {self.mark}')

@Singleton
class B:
    def __init__(self):
        print('i am b')

    def my_method(self):
        print(' I am still B')


a = A('first')
a.my_method()
b = A('second')
a.my_method()
