# -*- coding:utf-8 -*-
'''
Created on 2015年10月21日

@author: Administrator
'''
#新式类的语法中，需要在模块或者脚本开始的地方放置该赋值语句
__metaclass__ = type #确定使用新式类

class Person:
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def greet(self):
        print 'Hello, world! I am %s.' % self.name
        
foo = Person() 
bar = Person()
foo.setName('wang')
bar.setName('kang')

foo.greet() #可以看做Person.greet(foo)的简写
bar.greet()