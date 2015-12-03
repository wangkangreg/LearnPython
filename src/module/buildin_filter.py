# -*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: Administrator
'''
def func(x):
    if x > 0:
        return True

print filter(func, range(-9, 10)) #1, 2, 3, 4, 5, 6, 7, 8, 9]