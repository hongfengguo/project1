import gevent
from time import sleep

def foo(a,b):
    print('foo',a,b)
    gevent.sleep(2)
    print('running foo')

def bar():
    print('bar')
    gevent.sleep(3)
    print('running bar')

f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)
while True:
    gevent.sleep(2)
