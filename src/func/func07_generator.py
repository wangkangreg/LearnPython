# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''
def func(n):
    for i in range(n):
        yield i
        
for i in func(3):
    print i
    
r = func(3)
print r.next() #0
print r.next() #1
print r.next() #2
print r.next() #StopIteration
