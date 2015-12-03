# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
import os

li = os.listdir('.') #表示当前目录
print li
if os.path.exists('hello.txt'):
    os.rename('hello.txt', 'hi.txt')
elif os.path.exists('hi.txt'):
    os.rename('hi.txt', 'hello.txt')