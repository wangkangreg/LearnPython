# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
import os
file('hello.txt', 'w')
if os.path.exists('hello.txt'):
    os.remove('hello.txt')
