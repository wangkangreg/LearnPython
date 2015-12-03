# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
import shutil
shutil.copyfile('hello.txt', 'hello3.txt')
shutil.move('hello.txt', '../') #移动到上一级目录
shutil.move('hello3.txt', 'hello4.txt')