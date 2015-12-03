# -*- coding:utf-8 -*-
'''
Created on 2015年11月5日

@author: Administrator
'''
x = input('Input x:')
i = 0
while x <> 0:
    if  x > 0:
        x -= 1
    else:
        x += 1
    i += 1
    print 'Circle %d' % i, x
else:
    print 'x = 0: ', x