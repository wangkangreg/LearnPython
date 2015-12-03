# -*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: Administrator
'''
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
    
#重新父类init的定义
#filter方法直接继承父类
class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']
        
f = Filter()
f.init()
s = SPAMFilter()
s.init()
 
print f.filter([1, 2, 3]) #[1, 2, 3]
print s.filter(['SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']) #['eggs', 'bacon']

print issubclass(SPAMFilter, Filter) #True
print issubclass(Filter, SPAMFilter) #False

print SPAMFilter.__bases__ #(<class __main__.Filter at 0x0257A930>,)
print Filter.__bases__ #()

print isinstance(s, SPAMFilter) #True
print isinstance(s, Filter) #True
print isinstance(s, str)  #False

print s.__class__ #__main__.SPAMFilter
print type(s) #<type 'instance'>
