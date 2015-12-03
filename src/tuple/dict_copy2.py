# -*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: Administrator
'''

import copy
dict1 = {'a':'apple', 'b':{'g':'grage', 'o':'orange' }}
dict2 = copy.deepcopy(dict1)
dict3 = copy.copy(dict1)
dict2['b']['g'] = 'orange'
print dict1 #{'a': 'apple', 'b': {'o': 'orange', 'g': 'grage'}}
dict3['b']['g'] = 'orange'
print dict1 #{'a': 'apple', 'b': {'o': 'orange', 'g': 'orange'}}