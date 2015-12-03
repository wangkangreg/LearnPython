# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''

def reverse(s):
    out = ''
    li = list(s)
    for i in range(len(li), 0, -1):
        out += ''.join(li[i-1])
    return out

def reverse2(s):
    li = list(s)
    li.reverse()
    return ''.join(li)
  
print reverse('wang') #gnaw
print reverse2('wang') #gnaw
print 'wang'[::-1] #gnaw

