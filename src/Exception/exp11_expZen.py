# -*- coding:utf-8 -*-
'''
Created on 2015年10月27日

@author: Administrator
'''
def person(person):
    print 'Desc of'  , person['name']
    print 'Age: ', person['age']
    if 'occup' in person:
        print 'Occup: ', person['occup']
        
def personAdv(person):
    print 'Desc of'  , person['name']
    print 'Age: ', person['age']
    try:
        print 'Occup: ' + person['occup']
    except KeyError:
        pass
        
person1 = {'name':'Wang', 'age':10, 'occup':'Test'}
person2 = {'name':'Wang', 'age':10}

person(person1)
personAdv(person2)