# -*- coding:utf-8 -*-
'''
Created on 2015年10月27日

@author: Administrator
'''

obj = 10

try:
    obj.write
except AttributeError:
    print 'blabla'
else:
    print 'The object is writeable'