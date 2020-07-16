#处理配置文件
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

#import configparser   #在python中用来读取ini类型的配置文件

#configparser用法
#引入模块
import configparser 
#实例化一个对象
#config = configparser.ConfigParser() #ConfigParser()是类中的一个方法
#读取文件内容
#config.read(base_path+'/config/sever.ini')  #read里面跟ini路径
#print(config.sections())  #['server', 'bitbucket']
#得到配置文件里的host
#data = config.get('server','host') 
#print(data)   #http://www.imooc.com/


#封装一个获取配置文件的方法
ini_path = base_path+'/config/sever.ini'
class HandInit:
    def load_ini(self,path):
        '''
        读取配置文件
        '''
        cf = configparser.ConfigParser()
        cf.read(path,encoding='utf-8-sig')
        return cf
    
    def  get_value(self,key,value):
        '''
        获取配置文件内容
        '''
        data =self.load_ini(ini_path).get(key,value)
        return data

handinit = HandInit()  #实例化对象

# if __name__ == "__main__":
#     handinit = HandInit()
#     data = handinit.get_value('server','host')
#     print(data)