# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''
def func(n):
    for i in range(n):
        return i
    
def func2(n):
    for i in range(n):
        yield i
        
print func(3) #0
f = func2(3)
print f #<generator object func2 at 0x025F17B0>
print f.next() #0
print f.next() #1
    