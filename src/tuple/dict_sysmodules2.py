# -*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: Administrator
'''
import sys
d = sys.modules.copy() #当前导入的模块信息保存到d中
import copy, string #此时modules包含了原有的和新导入的模块
#set(sys.modules) - set(d)：返回在d中不存在，而在modules中存在的模块
#zip对set集合解包，返回一个列表
print zip(set(sys.modules) - set(d)) #[('copy',), ('strop',), ('string',)]
