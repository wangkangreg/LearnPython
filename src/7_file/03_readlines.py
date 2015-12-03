# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
f = open('hello.txt')
lines = f.readlines()
for line in lines:
    print line,