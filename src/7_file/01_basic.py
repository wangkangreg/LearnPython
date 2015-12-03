# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
context = '''hello world
hello China
'''

f = file('hello.txt', 'w')
f.write(context)
f.close()
