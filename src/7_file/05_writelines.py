# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
f = open('hello.txt', 'w+')
li = ['wang\n', 'kang\n'] #不会自动添加分隔符，不会添加空行
f.writelines(li)
f.close()