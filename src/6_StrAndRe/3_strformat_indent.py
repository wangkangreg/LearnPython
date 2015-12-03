# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''
word = 'version3.0'
print word.center(20) #总长度为20，居中对齐
print word.center(20, '*')
print word.ljust(0) #左对齐
print word.rjust(20) #总长度为右对齐，左边填充10个个空格
print '%30s' % word #先输出20个空格，类似于word.rjust(30)