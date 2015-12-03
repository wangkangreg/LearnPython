# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''

def func():
    x = 1
    y = 2
    m = 3
    n = 4
    sum = lambda x, y: x + y
    print sum #<function <lambda> at 0x029CE330>
    sub = lambda x, y: x - y
    print sub #<function <lambda> at 0x029CE230>
    return sum(x, y) * sub(m, n)

print func() #-3

print (lambda x : -x)(-2) #2

