# -*- coding:utf-8 -*-
'''
Created on 2015年11月5日

@author: Administrator
'''

dict = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
dict2 = {'x':'xxx', 'y':'yyy'}
dict.update(dict2)
print dict #{'a': 'apple', 'b': 'banana', 'g': 'grape', 'y': 'yyy', 'x': 'xxx', 'o': 'orange'}