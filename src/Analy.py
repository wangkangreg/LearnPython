# -*- coding: UTF-8 -*-
import os
import winshell
import sys 
import time
import mymail

 
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    from src import json2
    nData='''[{"filename":"360cse_8.5.0.120.exe","updatetype":"全量","updateoper":"去掉"},{"filename":"8.5.0.118到8.5.0.122","updatetype":"增量","updateoper":"新增","rate":"100","othercondition":"win7","conditions":[{"filename":"360chrome.exe","select":"equal","ver1":"8.5.0.118","ver2":""}],"size":"8","updatedailyamount":"56","magnitude":"dfd d "},{"filename":"8.5.0.122","updatetype":"全量","updateoper":"新增","rate":"100","othercondition":"","conditions":[{"filename":"360chrome.exe","select":"between","ver1":"8.0.0.100","ver2":"8.5.0.114"},{"filename":"360chrome.exe","select":"between","ver1":"7.0.0.100","ver2":"7.2.0.100"}],"size":"5","updatedailyamount":"70","magnitude":"erer"}]'''
    locations=json2.loads(nData)
    htmlCont=''
    updateAddContent=''
    conditionsCont=''
    reMoveCont=''
    upDetail='''<p><span style="font-size:14px;font-family:微软雅黑;font-weight:bold">【升级细节】</span></P>'''
    i=1
    content1='''<html><p><font color="black" face="微软雅黑" size='4'>Hi，各位</font></p>               
              <p>&nbsp;&nbsp;<font color="black" face="微软雅黑" size='4'>360安全浏览器8.1.1.108内测版 预计今天测试完毕，申请发布</font></p>
                ''' 
    for location in locations:
        if location["updateoper"]=="去掉":
            reMoveCont=''' <p><span style="font-size:14px;font-family:微软雅黑">%s.</span><span style="font-size:14px;font-family:微软雅黑;color:#FF0000">去掉 </span><span style="font-size:14px;font-family:微软雅黑">%s的%s升级</span></P>''' %(i,location["filename"],location["updatetype"])
            i=i+1        
        elif location["updateoper"]=="新增":
#             updateAddContent="新增"+location["filename"]+"的"+location["updatetype"]+"升级"
            updateAddContent=''' <p><span style="font-size:14px;font-family:微软雅黑">%s.</span><span style="font-size:14px;font-family:微软雅黑;color:#FF0000">新增 </span><span style="font-size:14px;font-family:微软雅黑">%s的</span><span style="font-size:14px;font-family:微软雅黑;color:#FF0000">%s</span><span style="font-size:14px;font-family:微软雅黑">升级</span></P> ''' %(i,location["filename"],location["updatetype"])
            arrList=[]
            contentList=[]
            huoList=[]            
            firstFileName=''
            str=''
            for index in range(len(location["conditions"])):
                arrList.append(location["conditions"][index]['filename'])
                firstFileName=location["conditions"][0]['filename']
                if index>0 and location["conditions"][index]['filename']!=firstFileName:
                    huoList.append('且')
                elif location["conditions"][index]['filename']==firstFileName:
                    huoList.append('或')                    

                if location["conditions"][index]['select']=='between':
                    st='介于['+location["conditions"][index]['ver1']+','+location["conditions"][index]['ver2']+']'
                if location["conditions"][index]['select']=='equal':
                    st="=="+location["conditions"][index]['ver1']
                contentList.append(st)            
            contStr=[]           
            if len(location["conditions"])==1:
                conditionsCont=firstFileName+contentList[0]
            
            elif len(location["conditions"])>1:                
                for i in range(len(location["conditions"])):
                    if i==0:
                        str=contentList[i]
                        contStr.append(str)                       
                    else:                        
                        str=huoList[i]+contentList[i] 
                        contStr.append(str)                      
                connect=''    
                for itcont in  contStr:
                    connect=connect+ itcont                             
                conditionsCont= firstFileName+connect
            qjian=''' <p>&nbsp;&nbsp;<span style="display:block;text-indent:2em;font-size:14px;font-family:微软雅黑">发布区间:%s</span></P> '''%(conditionsCont)
            strOther='''<div><p>&nbsp;&nbsp;<span style="text-indent:2em;font-size:14px;font-family:微软雅黑">其他条件:%s</span></P> '''%(location["othercondition"])
            rate= '''<p>&nbsp;&nbsp;<span style="font-size:14px;font-family:微软雅黑">V3升级比例:</span><span style="font-size:14px;font-family:微软雅黑;color:#FF0000">%s%%</span></P> '''%(location["rate"])        
            updatedailyamount='''<p>&nbsp;&nbsp;<span style="font-size:14px;font-family:微软雅黑">预计可以升级的量级:每日</span><span style="font-size:14px;font-family:微软雅黑;font-weight:bold">%sw</span></P> '''%(location["updatedailyamount"])
            fileSize='''<p>&nbsp;&nbsp;<span style="font-size:14px;font-family:微软雅黑">文件大小:</span><span style="font-size:14px;font-family:微软雅黑;font-weight:bold">%sM</span></p>'''%location["size"]
            magnitude='''<p>&nbsp;&nbsp;<span style="font-size:14px;font-family:微软雅黑">发布区间增量级:</span><span style="font-size:14px;font-family:微软雅黑;font-weight:bold">%s</span></P></div>'''%location["magnitude"]            
            htmlCont=htmlCont+updateAddContent+'\n'+qjian+'\n'+strOther+'\n'+ rate+'\n'+updatedailyamount+'\n'+fileSize+'\n'+magnitude
            i=i+1
    print content1+upDetail+reMoveCont+htmlCont+"</html>"
    mymail.sendMailPic('xiayanxia@360.cn', 'xiayanxia@360.cn', '123123123123', (content1+upDetail+reMoveCont+htmlCont+"</html>").decode('utf-8').encode('gb2312'))
#             detailConts.append(htmlCont)
#         detailConts.append(reMoveCont)

        
        
            
#     for ritem in reMoveCont:
#         print ritem
        
         
        
   

    