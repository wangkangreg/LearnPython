# -*- coding:utf-8 -*-
'''
Created on 2015年11月16日

@author: Administrator
'''

import json

nData='''[{"filename":"360cse_8.5.0.120.exe","updatetype":"全量","updateoper":"去掉"},
{"filename":"8.5.0.118到8.5.0.122","updatetype":"增量","updateoper":"新增","rate":"100","othercondition":"win7",
    "conditions":[{"filename":"360chrome.exe","select":"equal","ver1":"8.5.0.118","ver2":""}],
    "size":"8","updatedailyamount":"56","magnitude":"dfd d "},
{"filename":"8.5.0.122","updatetype":"全量","updateoper":"新增","rate":"100","othercondition":"",
    "conditions":[{"filename":"360chrome.exe","select":"between","ver1":"8.0.0.100","ver2":"8.5.0.114"},
{"filename":"360chrome.exe","select":"between","ver1":"7.0.0.100","ver2":"7.2.0.100"}],
    "size":"5","updatedailyamount":"70","magnitude":"erer"}]'''
t = '["foo", {"bar":["baz", null, 1.0, 2]}]'
   
s = json.loads(nData)
print s
#print s.keys()
print s['filename']
print s['conditions']['filename']