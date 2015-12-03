# -*- coding:utf-8 -*-
'''
Created on 2015年10月29日

@author: Administrator
'''
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

#label: first, middle, last
#return 包含全名的列表 
def lookup(data, label, name):
    return data[label].get(name)   
  
def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
        labels = 'first', 'middle', 'last'
        
        
    
storage = {}
init(storage)
print storage #{'middle': {}, 'last': {}, 'first': {}}