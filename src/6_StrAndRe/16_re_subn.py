# -*- coding:utf-8 -*-
'''
Created on 2015年11月12日

@author: Administrator
'''

import re
s = '你好 WORLD2' 
print re.sub(r'\w', 'hi', s) #你好 hihihihihihi,\w不能匹配汉字
print str(re.subn(r'\w', 'hi', s)[1]) #6
print re.sub(r'\W', 'hi', s) #hihihihihihihiWORLD2
print str(re.subn(r'\W', 'hi', s)[1]) #7
print re.sub(r'\s', '*', s) #你好*WORLD2