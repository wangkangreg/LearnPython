# -*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: Administrator
'''
import module_forimport

print 'count=', module_forimport.func() #2
module_forimport.count = 10
print 'count=', module_forimport.count #10

import module_forimport
print 'count = ', module_forimport.func() #11