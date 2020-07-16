import requests
import json
#header介绍及运用
header = {
    'Host':'m.imooc.com',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://m.imooc.com/',
    'Accept-Language':'zh-CN,zh;q=0.9',
}
header_url = 'http://www.imooc.com'
#header_res = requests.get(header_url,headers=header,verify=False).json()
#print(header_res)

#header中带加密
#引入hashlib,它提供字符串加密模块
import hashlib 
#实例化md5
md5 = hashlib.md5()
#需加密的字符串
a= 'name = anjing,age=18,sex=male'
#对字符串a进行加密
md5.update(a.encode('utf-8'))
#获取加密后的字符串
res = md5.hexdigest()
#print(res)   #打印出 7b660350c1408acde4dbf44916281052
#再把加密的字符串放到请求里
md5_header = {
    #...
    'token':res,   #名为token的参数传入res,即此参数加密
}
#header_res = requests.get(header_url,headers=header,verify=False).json()


