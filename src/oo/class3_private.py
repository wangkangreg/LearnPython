# -*- coding:utf-8 -*-
'''
Created on 2015年10月21日

@author: Administrator
'''
class Secretive:
    def __inaccessible(self):
        print 'Bet you can not see me...'
        
    def accessible(self):
        print 'The secret message is:'
        self.__inaccessible()
        
s = Secretive()
print Secretive._Secretive__inaccessible #<unbound method Secretive.__inaccessible>
s._Secretive__inaccessible() #Bet you can not see me...，了解内部后，还是能在类外访问这些私有方法