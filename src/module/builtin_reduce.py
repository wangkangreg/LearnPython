# -*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: Administrator
'''
def sum(x, y):
    return x + y

print reduce(sum, range(0, 10)) #45
print reduce(sum, range(0, 10), 10) #55
print reduce(sum, range(0, 0), 10) #10