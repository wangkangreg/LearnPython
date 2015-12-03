# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
f = open('hello.txt')
while True:
    line = f.readline()
    if line:
        print line,
    else:
        break
f.close()