# -*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: Administrator
'''
class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print "Division by zero is illegal"
            else:
                raise
            
mc = MuffledCalculator()
print mc.calc("4/2") #2
mc.muffled = True
print mc.calc('4/0') #Division by zero is illegal, None