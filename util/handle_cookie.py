#处理cookie
#encoding=utf-8
#1.获取cookie 2.写入cookie 

#获取cookie，处理逻辑
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

from util.handle_json import read_json,write_value

#获取所有的cookie
def get_cookie():
    data = read_json('/config/cookie.json')
    return data

#获取特定key的cookie
def get_cookie_value(cookie_key):
    data1 = get_cookie()
    return data1[cookie_key]

#写入cookie
path = base_path+'/config/cookie.json'
def write_cookie(data,cookie_key):
    data2 = get_cookie()
    data2[cookie_key] = data #获取特定key的cookie,并赋值
    write_value(data2,path)  #将新的cookie重新写入到cookie.json

# if __name__ == "__main__":
#     #print(get_cookie_value('app'))
#     data = {'sex':11}
#     print(write_cookie(data,'web'))   #将此写入到cookie.json中
       

