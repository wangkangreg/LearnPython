# -*- coding:utf-8 -*-
'''
Created on 2015年10月27日

@author: Administrator
'''
while True:
    try:
        x = input('Enter the first number:')
        y = input('Enter the second number:')
        value =  x / y
        print 'x / y is: ', value
    except:
        print 'Invalid value. Please try again.'
    else:
        break;