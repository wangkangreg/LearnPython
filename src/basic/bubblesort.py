# -*- coding:utf-8 -*-
'''
Created on 2015年11月5日

@author: Administrator
'''

def bubblesort(seq):
    for j in xrange(len(seq) - 1,  -1, -1): #循环每次的比较次数
        for i in xrange(j):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                
    return seq
                
myseq = [5, 12, 8, 3, 79, 102, 9]
print bubblesort(myseq)