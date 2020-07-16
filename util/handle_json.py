#处理json文件
#encoding=utf-8
#在base->base_request.py中mock数据，达到当相关字段加密时，接口测试能正常进行
import json
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

#读取json数据
def read_json(file_name =None):
    if file_name ==None:
        file_path = base_path+'/config/user_data.json'
    else:
        file_path = base_path+file_name
    with open(file_path,encoding='utf-8') as f:
        data = json.load(f)
    return data

#根据键值对关系获取相应的值
def get_value(key,file_name=None):
    data = read_json(file_name)
    return data.get(key)

#写入新值
def write_value(data,path): 
    data_value = json.dumps(data)  #将传入的data,字典类型转化为json类型
    with open(path,'w') as f:
        f.write(data_value)
