# -*- coding:utf-8 -*-
'''
Created on 2015年11月11日

@author: Administrator
'''
import time, datetime
#localtime()返回：2015-11-11 21:23:38
print time.strftime('%Y-%m-%d %X', time.localtime()) #2015-11-11 21:23:38
t = time.strptime('2008-08-08', '%Y-%m-%d')
y, m, d = t[0:3] 
print datetime.datetime(y, m, d) #2008-08-08 00:00:00
