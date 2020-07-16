#coding = utf-8
#目的：封装所有的requests请求
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

import requests
import json
#获取配置文件
from util.handle_init import handinit
#获取本地json数据 ,目的：mock数据
from util.handle_json import get_value
#写入cookie
from util.handle_cookie import get_cookie,write_cookie
class BaseRequests:
    #定义一个post方法
    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):
        #发送一个post请求
        response = requests.post(url=url,data=data,cookies=cookie,headers=header)
        if get_cookie!=None:
            '''
            get_cookie类似{"is_cookie":"app"}这种形式
            requests只能保持 cookiejar 类型的cookie，
            而我们手动构建的cookie是dict类型的。所以将cookiejar->dict
            '''
            cookie_value = requests.utils.dict_from_cookiejar(response.cookies)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        #返回res出去
        return res
    #定义一个get方法
    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        #发送一个get请求
        response = requests.get(url =url, params=data,cookies=cookie,headers=header)
        if get_cookie !=None:
            cookie_value = requests.utils.dict_from_cookiejar(response.cookies)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res

    #定义一个方法来决定调用什么post还是get
    def run_main(self ,method,url, data,cookie=None,get_cookie=None,header=None):
        #执行方法，传递method，url,data参数
        #print(get_value(url))   #mock数据
        #url是 host+关键URL方式
        base_url = handinit.get_value('server','host')
        if 'http' not in url:
            url = base_url+url
        if method == 'get':
            res = self.send_get(url,data,cookie,get_cookie,header)
        else:
            res = self.send_post(url,data,cookie,get_cookie,header)
        try:
            res = json.loads(res)  #将json字符串转化为字典
        except:
            print('这个结果是一个text')
        return res

#实例化类
request = BaseRequests()
# if __name__ == "__main__":
    # request = BaseRequests()
    # #测试引入的host
    # request.run_main('get','/api3/getbanneradvertver2',"{'username':'11111'}")  



