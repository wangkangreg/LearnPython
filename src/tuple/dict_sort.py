# -*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: Administrator
'''

dict = {'a':'apple', 'b':'banana', 'c':'orange', 'd':'banana'}
print dict #{'a': 'apple', 'c': 'orange', 'b': 'banana', 'd': 'banana'}
#按key排序
print sorted(dict.items(), key=lambda d: d[0])  #[('a', 'apple'), ('b', 'banana'), ('c', 'orange'), ('d', 'banana')]
#按value排序
print sorted(dict.items(), key = lambda d: d[1]) #[('a', 'apple'), ('b', 'banana'), ('d', 'banana'), ('c', 'orange')]