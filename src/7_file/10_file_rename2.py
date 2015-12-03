# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''
import os

items = os.listdir('.')
for item in items:
    index =  item.find('.html')
    if index <> -1:
        os.rename(item, item[:-1])
        