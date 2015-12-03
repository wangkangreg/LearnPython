# -*- coding:utf-8 -*-
'''
Created on 2015年11月12日

@author: Administrator
'''

import re
s = 'hello world'
print re.sub('hello', 'hi', s) #hi world
print re.sub('hello', 'hi', s[-4:]) #orld
print re.sub('world', 'China', s[-5:]) #China
