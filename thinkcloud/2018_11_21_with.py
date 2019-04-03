#!/usr/bin/env python
# coding=utf-8


from contextlib import contextmanager

@contextmanager
def demo():
    print '这里的代码相当于__enter__里面的代码'
    yield 'i ma value'
    print '这里的代码相当于__exit__里面的代码'

with demo() as value:
	pass

    # print  value

class closing(object):
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()

class A():
    def __init__(self):
        self.thing=open('file_name','w')
    def f(self):
        print '运行函数'
    def close(self):
        self.thing.close()

with closing(A()) as a:
    a.f()