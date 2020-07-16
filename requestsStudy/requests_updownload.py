#requests上传文件操作
import requests
import json
url = 'https://graph.baidu.com/upload'
#file指的是上传文件的相关参数，可在抓包里抓住
file = {
    # r 是读取人工书写的数据，书写的时候什么样，读取出来就什么样
    # rb 是读取二进制文件，非人工书写的数据如.jpeg这些
    # encoding指定解码方式，python3默认utf-8,python2默认ascii
    # 'image/jpeg'指的是传递类型
    'image':('mao.jpg',open('/Users/panwumei/Documents/2020软件测试基础学习/笔记/python接口自动化测试/requestStudy/mao.jpg','rb'),'image/jpeg'),
}
res = requests.post(url, files=file,verify=False)
print(res.json())

#requests下载文件
download_url = 'http://file.mukewang.com/apk/app/117/imooc7.3.610102001android.apk?version=1588585458'
res = requests.get(download_url).content  #获取下载内容
with open('muke.apk','wb') as f:  #以写入字节方式打开
   f.write(res)   #运行，可下载文件