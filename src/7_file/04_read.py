# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
f = open('hello.txt')
# context = f.read()
# print context
context = f.read(5)
print context #hello
print f.tell() #5
context = f.read(5)
print context # worl 
print f.tell() #10
f.close()
