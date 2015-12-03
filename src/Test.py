# -*- coding:utf-8 -*-
'''
Created on 2015年11月26日

@author: Administrator
'''
import ConfigParser
import json
import re
from fileinput import filename

config = ConfigParser.ConfigParser()
config.read('360se.ini')

#测试用数据
nData='''[{"filename":"360cse_8.5.0.120.exe","updatetype":"全量","updateoper":"去掉"},
{"filename":"8.5.0.118到8.5.0.122","updatetype":"增量","updateoper":"新增","rate":"100",
    "othercondition":"win7","conditions":[{"filename":"360chrome.exe","select":"equal","ver1":"8.5.0.118","ver2":""}],
    "size":"8","updatedailyamount":"56","magnitude":"dfd d "},
{"filename":"8.5.0.122","updatetype":"全量","updateoper":"新增","rate":"100",
    "othercondition":"","conditions":[{"filename":"360chrome.exe","select":"between","ver1":"8.0.0.100","ver2":"8.5.0.114"},
{"filename":"360chrome.exe","select":"between","ver1":"7.0.0.100","ver2":"7.2.0.100"}],
    "size":"5","updatedailyamount":"70","magnitude":"erer"}]'''

def get_real_file_info(filename, browsertype=0):
    '''
    #发布申请邮件中填写的文件名称不规范，可能有5种形式
    #这里要把这5种形式转换成实际对应的文件名和版本并返回
    #1. 360cse_8.5.0.120.exe：直接返回
    #2. 8.5.0.118到8.5.0.122：
        #browsertype为0，返回se8.5.0.118_8.5.0.122.7z。
        #browsertype为1，返回chrome8.5.0.118_8.5.0.122.7z
    #3. 8.5.0.122：
        #browsertype为0，返回360se8.5.0.122.exe。
        #browsertype为1，返回360cse_8.5.0.120.exe     
    #4. 360se.exe_1.0.0.1：返回下划线前面的内容 
    #5. 
    #browsertype == 0，说明是se
    #browsertype == 1，说明是360chrome
    返回值：(文件名，版本号)，如(360cse_8.5.0.120.exe, 8.5.0.120)
    '''
    if filename.endswith('.exe'): 
        #处理形式：360se8.5.0.122.exe或360cse_8.5.0.120.exe
        return filename, filename[-13:-4]
    elif filename.find('.7z') != -1:
        #处理形式：se7.1.1.630_7.1.1.636.7z
        return filename, filename[-12:-3]
    elif filename.find('_') != -1 and not filename.endswith('.7z'):
        #处理形式：360se.exe_1.0.0.1
        temp = filename.split('_')
        return temp[0], temp[1]
    elif filename.find('到') != -1:
        #处理形式：8.5.0.118到8.5.0.122
        if browsertype == 0: #se
            return 'se' + filename[:9] + '_' + filename[-9:] + '.7z', filename[-9:] 
        elif browsertype == 1: #360Chrome
            return 'chrome' + filename[:9] + '_' + filename[-9:] + '.7z', filename[-9:]
    elif re.match(r'\d.\d.\d.\d\d\d', filename):
        #处理形式：8.5.0.120
        if browsertype == 0: #se
            return '360se' + filename + '.exe', filename
        elif browsertype == 1: #360Chrome
            return '360cse_' + filename + '.exe' , filename
    else:
        return '' , ''  

def check_update_info(updateinfo, browsertype=0):
    '''
    #updateinfo：str类型，从数据库中取出的，余俊填写的升级信息，json串
    #返回值：str类型，记录了ini与发布申请不一致的地方，每个错误信息一行
    '''
    err_msg = ''
    #解析出升级细节
    infos=json.loads(updateinfo) 
     
    #依次处理细节
    for info in infos: 
        #实际传入的filename可能有多种形式，解析成实际的文件名
        filename, filever = get_real_file_info(info['filename'], browsertype)  
        
        if info["updateoper"]==u"去掉": 
            if  filename in config.sections(): 
                #发布申请中删除的节点在ini中仍然存在，报错
                err_msg = err_msg + '\n发布申请中删除了' + filename + '，但是ini中出现了该文件节点'
        if info["updateoper"]==u"新增" or info["updateoper"]==u"修改" :
            if filename not in config.sections(): 
                #发布申请中修改或是新增的节点在ini中不存在，报错
                err_msg = err_msg + '\n发布申请中新增（或修改）了' + filename + '，但是ini中没有该文件节点'
            else:
                check = ''
                try:
                    check = config.get(filename, 'check')
                except ConfigParser.NoOptionError:     
                    err_msg = err_msg + '\n发布申请中新增（或修改）了' + filename + '，但是ini中该文件节点找不到check字段'
                                     
                #验证其它条件
                otherconditions = info['othercondition'] #{"os":"no","skipwb":0,"gentle":0}
                #1. 验证gentle配置
                gentle = 0
                try:
                    gentle = config.getint(filename, 'gentle')
                except ConfigParser.NoOptionError:
                    pass
                if not otherconditions['gentle'] == gentle:
                    err_msg = err_msg + '\n' + filename + '发布申请中gentle配置为' + otherconditions['gentle'] + \
                        '，ini中配置为' + gentle

                #2. 验证skipwb配置
                skipwb = 0
                try:
                    gentle = config.getint(filename, 'skipwb')
                except ConfigParser.NoOptionError:
                    pass
                if not otherconditions['skipwb'] == gentle:
                    err_msg = err_msg + '\n' + filename + '发布申请中skipwb配置为' + otherconditions['skipwb'] + \
                        '，ini中配置为' + skipwb

                #3. 验证系统要求
                
                    
                #验证升级比率
                rate = info['rate'] #(%trate%>"1000")             
                if rate == '100':
                    #如果升级比率是100%，ini对应section的check字段中不应该有trate字符
                    if check.find('trate') != -1:
                        err_msg = err_msg + '\nini中' + filename + '文件中的升级比率与发布申请中不一致'
                else:
                    #如果升级比率不是100%，ini中应该可以找到对应的升级比率字符串
                    if check.find('(%trate%>"' + rate + '"') == -1:
                        err_msg = err_msg + '\nini中' + filename + '文件中的升级比率与发布申请中不一致' 
                
                #验证升级区间
                conditions = info['conditions']
                for condition in conditions:
                    select = condition['select']
                    condition_filename = condition['filename']
                    if select == 'between':
                        condition_str = '(%fver_' + condition_filename + \
                            '%>="'  + condition['ver1'] + \
                            '")&&(%fver_' + condition_filename + \
                            '%<="'  + condition['ver2']  + \
                            '")'
                        if check.find(condition_str) == -1:
                            err_msg = err_msg + '\nini中缺失发布申请中的升级信息，发布申请中的信息为：' +  condition
                    elif select == 'equal':
                        condition_str = '(%fver_' + condition_filename + \
                            '%=="'  + condition['ver1'] + \
                            '")'
                        if check.find(condition_str) == -1:
                            err_msg = err_msg + '\nini中缺失发布申请中的升级信息，发布申请中的信息为：' +  condition
                    elif select == 'greater':
                        condition_str = '(%fver_' + condition_filename + \
                            '%>="'  + condition['ver1'] + \
                            '")' 
                        if check.find(condition_str) == -1:
                            err_msg = err_msg + '\nini中缺失发布申请中的升级信息，发布申请中的信息为：' +  condition               
                    elif select == 'less':
                        condition_str = '(%fver_' + condition_filename + \
                            '%<="'  + condition['ver1'] + \
                            '")'                                  
                        if check.find(condition_str) == -1:
                            err_msg = err_msg + '\nini中缺失发布申请中的升级信息，发布申请中的信息为：' +  condition      
     
    return err_msg
                                        
def check_update_info_details(filename, apply_info, browsertype=0):
    '''
    比对指定升级细节的信息。用luohao ini中配置的信息与yujun页面提交的信息进行对比
    filename：str类型，升级文件名，对应ini中的一个section
    apply_info：dict类型，根据余俊填写的内容，解析出的一个升级细节。
    browsertype：int类型，浏览器类型，0:se，1:360chrome
    #返回值：str类型，记录了ini与发布申请不一致的地方，每个错误信息一行
    '''
    err_msg = ''
    #从ini中解析升级内容
    ini_config_info = {
                       'ver':config.get(filename, 'ver'),
                       'check':config.get(filename, 'check'),
                       'md5':config.get(filename, 'md5'),
                       'url':config.get(filename, 'URL')
                       }
    
    #1. 比对版本信息
    expect_filename, expect_ver = get_real_file_info(apply_info['filename'], browsertype)
    if ini_config_info['ver'] != expect_ver:
        err_msg = err_msg + '\n' + filename + '文件，发布申请中版本号是：' + expect_ver + \
            '，实际ini中版本号是：' + ini_config_info['ver']
    #2. 比对check信息
    #验证余俊填写的信息都能ini中找到
    apply_info['rate']
    
    #验证ini中内容都能在余俊填写的信息中找到
             
def parse_condition(conditions):
    '''
    将传入的实际升级条件，格式如下
    ((%fver_setup.exe%=="6.3.1.150")||(%fver_setup.exe%=="6.3.1.196")||
    (%fver_setup.exe%=="7.0.0.182"))&&((%fver_ExtYouxi.dll%>"6.2.1.1001")&&(%fver_ExtYouxi.dll%<"6.2.2.1001"))&&(%trate%<="5000")
    解析为一个字典的列表，其中每个字典是一个独立的升级条件，如{"filename":"360chrome.exe","select":"between","ver1":"8.0.0.100","ver2":"8.5.0.114", 'other':'', 'rate':'100%'}
    conditions：传入的实际升级条件，具体内容是ini中check部分的文本
    返回：一个list，里面包含各个升级条件的列表
    '''
    result = []
    #将ini中check条件按照||拆分
    condition_list = conditions.split('||') #根据||对条件进行拆分，获取到一个条件列表
    for condition in condition_list: 
        condition_items = condition.split('&&') #列表中有区间的情况，根据&&继续拆分出原子条件
        
        condition_list = []
        condition_dict = {
            'filename':'', 
            'ver1':'', 
            'ver2':'', 
            'select':'', 
            'rate':'', 
            'other':{
                     'os':'no', 
                     'skipwb':0, 
                     'gentle':0
                     }}
        
        for item in condition_items:
            if item.find('%sysver%'):
                pass
            if item.find('=='): #(%fver_setup.exe%=="7.1.1.630")d
                condition_dict['filename'] = parse_condition_filename(item)
                condition_dict['ver1'] = parse_condition_ver(item)
                condition_dict['ver2'] = ''
                condition_dict['select'] = 'equal'
            elif item.find('>='): #(%fver_setup.exe%>="7.1.1.529")&&(%fver_setup.exe%<="7.1.1.999")
                if condition_dict['ver1'] == '':
                     condition_dict['ver1'] = item[-11:-2]
                else:
                    condition_dict['ver1'], condition_dict['ver2'] = item[-11:-2], condition_dict['ver1']
            elif item.find('<='):
                if condition_dict['ver1'] == '':
                     condition_dict['ver1'] = item[-11:-2]
                else:
                    condition_dict['ver1'], condition_dict['ver2'] = item[-11:-2], condition_dict['ver1']                
            elif item.find('trate'): #(%trate%<="1000")
                condition_dict['rate'] = item.split('"')[1]
            
        result.append(condition_dict)    
    return result
             
   
class CheckConditions():
       
    
    def __init__(self, config_str, type=0):
        self.type = type
        self.config_str = config_str
        
    def parseCheckInfo(self):
        pass
    
    def getCount(self):
        pass
    
    def addCheckCondition(self):
        pass

class CheckConditionItem():
    def __init__(self, filename, ver1, ver2, select, other, rate):
        self.filename = filename
        self.ver1 = ver1
        self.ver2 = ver2
        self.select = select
        self.other = other
        self.rate = rate
    
class CheckConditionItemParser():
    
    parsedConditionItems = []
    parsedFileDict = {}
    condition_item_list = []
    
    def __init__(self, condition_items):
        self.condition_items = condition_items
            
    def parseCondition(self, condition_item_list):
        for condition_item in condition_item_list:
            filename = self.parseConditonItemFileName(condition_item)
            relation = self.getRelationByFileName(filename)
            if relation == 'between':
                pass
            else:
                self.parsedConditionItems.append(CheckConditionItem())
    
    def parseConditonItemFileName(self, condition_item):
        '''
        (%fver_setup.exe%>="7.1.1.528") ===> setup.exe
        '''
        filter_list = ['trate', 'sysver']
        temp_list = condition_item.split('%')
        raw_filename = temp_list[1] #结果形式为：fver_setup.exe
        filename = raw_filename.lstrip('fver_') #结果形式为：setup.exe，去掉"fver_"
        if filename not in filter_list:
            return filename        
    
    def parseConditonItemFileVer(self, condition_item):
        '''
        实例
        (%fver_setup.exe%>="7.1.1.528") ===> 7.1.1.528
        '''
        temp_list = condition_item.split('"')
        return temp_list[1]
    
    def getConditionItemCount(self):
        '''
         (%fver_setup.exe%>="7.1.1.528")&&(%fver_setup.exe%<="8.0.1.999")&&(%fver_sesafe.dll%<"1.2.0.350") ===> 3
        '''
        return len(self.condition_item.split('&&'))
    
    def getConditionItemList(self):  
        '''
        返回按&&分割的，原子条件列表，如[(%fver_setup.exe%>="7.1.1.528"), (%fver_setup.exe%<="8.0.1.999"), (%fver_sesafe.dll%<"1.2.0.350")]
        (%fver_setup.exe%>="7.1.1.528")&&(%fver_setup.exe%<="8.0.1.999")&&(%fver_sesafe.dll%<"1.2.0.350")
        '''
        return self.condition_item.split('&&')

    def getConditionFileList(self):
        '''
        获取一个条件中全部文件名列表，去重
        (%fver_setup.exe%>="7.1.1.528")&&(%fver_setup.exe%<="8.0.1.999")&&(%fver_sesafe.dll%<"1.2.0.350") ===>
        ['setup.exe', 'setup.exe', 'sesafe.dll']
        '''
        for item in self.condition_item.split('&&'):
            filename = self.parseConditonItemFileName(item)
            if filename not in self.conditionItemList:
                self.conditionItemFileList.append(object)
                
    def createDictByFileName(self, filename):
        '''
        根据文件名生成字典，形式如下：
        '''
        myfile_set = set(self.getConditionItemList()) #去重
        for myfile in myfile_set:
                self.parsedFileDict.setdefault(filename, [])

              
if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    #print get_real_file_name('8.5.0.118到8.5.0.122') #se8.5.0.118_8.5.0.122.7z
    #print get_real_file_name('360cse_8.5.0.120.exe', 0)
    #check_update_info(nData)
    #print get_real_file_ver('360cse_8.5.0.120.exe')
    #print parse_condition_filename('((%fver_setup.exe%=="6.3.1.150")')
    #print parse_condition_ver('((%fver_setup.exe%=="6.3.1.150")')
    print check_update_info(nData, 0)
    