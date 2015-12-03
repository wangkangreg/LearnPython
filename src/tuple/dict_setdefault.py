# -*- coding:utf-8 -*-
'''
Created on 2015年11月5日

@author: Administrator
'''

dict = {}
dict.setdefault('a')
print dict #{'a': None}
dict['a'] = 'apple'
dict.setdefault('a', 'default')
print dict #{'a': 'apple'}