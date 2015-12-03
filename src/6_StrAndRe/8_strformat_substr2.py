# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''

sentence = 'Bob said:1, 2, 3, 4'
print sentence.split() #['Bob', 'said:1,', '2,', '3,', '4']
print sentence.split(',') #['Bob said:1', ' 2', ' 3', ' 4']
print sentence.split(',', 2) #['Bob said:1', ' 2', ' 3, 4']
