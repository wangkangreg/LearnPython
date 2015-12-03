# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''

import operator
strs = ['hello', 'world', 'haha']
result = reduce(operator.add, strs, ' ')
print result # helloworldhaha不知为啥无法输出中间的空格