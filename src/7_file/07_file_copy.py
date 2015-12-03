# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
src = open('hello.txt', 'w')
li = ['test1\n', 'test2\n']
src.writelines(li)
src.close()

src = open('hello.txt', 'r')
dst = open('hello2.txt', 'w')
dst.write(src.read())
src.close()
dst.close()
