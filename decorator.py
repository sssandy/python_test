#-*-coding:utf-8-*-
#装饰器
import functools

def log(arg):
    def decorator(func=arg):
        text='call' if func==arg else arg
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return (func(*args, **kw), print('end %s %s():' % (text, func.__name__)))[0]
        return wrapper
    return decorator() if callable(arg) else decorator

# 相当于 test1 = log(test1) = decorator() = wrapper
@log
def test1():
    print("test1")

# 相当于 test2 = log('excute')(test2) = decorator(test2) = wrapper
@log('excute')
def test2():
    print("test2")

test1()
test2()
