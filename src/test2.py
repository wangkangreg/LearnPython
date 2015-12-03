# -*- coding:utf-8 -*-
'''
Created on 2015年11月17日

@author: Administrator
'''

def buy():
    bigPrice = 15
    middlePrice = 9
    littlePrice = 1
    totalPrice = 300
    
    for x in range(totalPrice / bigPrice):
        for y in range(totalPrice / middlePrice):
            z = 100 - x - y
            if x * bigPrice + y * middlePrice + z * littlePrice == totalPrice:
                print '方案：x=%d, y=%d, z=%d' % (x, y, z)
                
buy()

