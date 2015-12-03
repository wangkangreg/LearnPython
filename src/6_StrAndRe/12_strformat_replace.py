# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''
sentence = 'hello world, hello China'
print sentence.replace('hello', 'hi') #hi world, hi China
print sentence.replace('hello', 'hi', 1) #hi world, hello China
print sentence.replace('abc', 'hi') #hello world, hello China