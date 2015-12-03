# -*- coding:utf-8 -*-
'''
Created on 2015年12月3日

@author: Administrator
'''
import urllib2
req = urllib2.Request('http://www.pythontab.com') 
try: urllib2.urlopen(req) 
except urllib2.URLError, e: 
    print e.reason
