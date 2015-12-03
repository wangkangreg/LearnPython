# -*- coding:utf-8 -*-
'''
Created on 2015年11月5日

@author: Administrator
'''

numbers = raw_input('输入几个数字，用逗号分隔：').split(',')
print numbers
x = 0
while x < len(numbers):
    print numbers[x]
    x += 1