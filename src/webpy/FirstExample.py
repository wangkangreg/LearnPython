# -*- coding:utf-8 -*-
'''
Created on 2015年10月21日

@author: Administrator
'''
import web

render = web.template.render('templates/') #告诉web.py到你的模板目录中去查找模板

urls = (
    '/(.*)', 'index'
    )

class index:
    def GET(self, name):
        return render.index(name) 

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()