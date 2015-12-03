# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''
word = 'hello world'
print 'hello' == word[0:5]
print word.startswith('hello')
print word.endswith('ld', 6)
print word.endswith('ld', 6, 10) #False，不包括位置10
print word.endswith('ld', 6, len(word))