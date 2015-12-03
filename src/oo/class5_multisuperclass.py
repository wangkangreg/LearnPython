# -*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: Administrator
'''

class Caculator:
    def calculate(self, expression):
        self.value = eval(expression)
        
class Talker:
    def talk(self):
        print 'Hi, my value is', self.value
        
class TalkingCalculator(Caculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk() #Hi, my value is 7

print hasattr(tc, 'talk') #True
print hasattr(tc, 'fnord') #False

print callable(getattr(tc, 'talk', None)) #True
print callable(getattr(tc, 'fnord', None)) #False

setattr(tc, 'name', 'Mr. Gumby')
print tc.name #Mr. Gumby

print tc.__dict__ #{'name': 'Mr. Gumby', 'value': 7}

