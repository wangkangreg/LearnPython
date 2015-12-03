# -*- coding:utf-8 -*-
'''
Created on 2015年10月21日

@author: Administrator
'''
class Bird:
    song = 'Squaawk!'
    def sing(self):
        print self.song
        
bird = Bird()
bird.sing() #Squaawk!
birdsong =bird.sing
birdsong() #Squaawk!