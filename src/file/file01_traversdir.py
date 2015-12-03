# -*- coding:utf-8 -*-
'''
Created on 2015年10月27日

@author: Administrator
'''
import os
import os.path

rootdir = "d:\\temp"
for parent, dirnames, filenames in os.walk(rootdir):
    for dirname in dirnames:
        print 'parent is: ' +parent
        print 'dirname is: ' + dirname
        
    for filename in filenames:
        print 'parent is: ' + parent
        print 'filename is: ' + filename
        print 'The full name of the file is: ' + os.path.join(parent, filename)