# -*- coding:utf-8 -*-
'''
Created on 2015年11月12日

@author: Administrator
'''

import re
s = 'HELLO WORLD'
print re.findall(r'^hello', s) #[]
print re.findall(r'hello', s, re.I) #['HELLO']
print re.findall('WORLD$', s) #['WORLD']
print re.findall(r'WORLD$', s, re.I) #['WORLD']
print re.findall(r'\b\w+\b', s) #['HELLO', 'WORLD']
