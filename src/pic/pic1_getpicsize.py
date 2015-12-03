# -*- coding:utf-8 -*-
'''
Created on 2015年10月27日

@author: Administrator
'''
# home.zhenliang@gmail.com
# http://t.qq.com/zhenliang
# 获取指定文件夹下所有图片的名字、长和宽

import Image

def GetPicInfo(mfile):
    try:    
        image = Image.open(mfile)
        print 'image width is: ', image.size[0]
        print 'image height is: ', image.size[1]
    except IOError, e:
        print 'Ah, something is wrong'
        print e
        pass

if __name__ == '__main__':
    GetPicInfo(r'C:\Users\Administrator\Desktop\1.jpg')
