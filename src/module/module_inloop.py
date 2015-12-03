# -*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: Administrator
'''

import module_forimport
if module_forimport.count > 1:
    module_forimport.count = 1
else:
    import module_forimport
print 'count = ', module_forimport.count