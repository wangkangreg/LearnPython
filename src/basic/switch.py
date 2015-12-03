# -*- coding:utf-8 -*-
'''
Created on 2015年11月4日

@author: Administrator
'''
class switch(object):
    def __init__(self, value):
        self.value = value #初始化需要匹配的值value
        self.fall = False #如果匹配到的case语句中没有break，则fall为true
        
    def __iter__(self):
        yield self.match #调用match方法返回一个生成器
        raise StopIteration #StopIteration异常判断for循环是否结束
    
    def match(self, *args): #模拟case子句的方法
        if self.fall or not args: #如果fall为true，则继续执行下面的case子句。或者case子句没有匹配项，则流转到默认分之
            return True 
        elif self.value in args:    #匹配成功
            self.fall = True
            return True
        else:   #匹配失败
            return False
 
operator = "+"
x = 1
y = 2
for case in switch(operator): #3，只能用于for in循环中
    if case('+'):
        print x + y
        break
    if case('-'):
        print x - y
        break
    if case('*'):
        print x * y
        break
    if case('/'):
        print x / y
        break
    if case():
        print ''
        break
        