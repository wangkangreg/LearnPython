# -*- coding:utf-8 -*-
'''
Created on 2015年11月10日

@author: Administrator
'''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print reduce(lambda x, y: x * y, range(1, 6)) #120