# -*- coding:utf-8 -*-
'''
Created on 2015年10月27日

@author: Administrator
'''
try:
    1 / 0
except NameError:
    print 'Unknown variable'
else:
    print 'That went well!'
finally:
    print 'Cleaning up.'