# -*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: Administrator
'''
try:
    x = input('Enter the first number:')
    y= input('Enter the second number:')
    print x/y
except ZeroDivisionError:
    print 'The second number can not be zero!'
except TypeError:
    print "That wasn't a number, was it?"