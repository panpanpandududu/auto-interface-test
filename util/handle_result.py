#处理case的数据获取及验证
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

#导入json数据模块
import json 

#导入处理json的方法
from util.handle_json import get_value

#导入校验json格式的库deepdiff
from deepdiff import DeepDiff


#定义一个获取message的方法
def handle_result(url,code):
    # 获取到json数据：给get_value()传url,file_name值
    data = get_value(url,'/config/code_message.json')
    #判断接口文件是否存在，不存在返回none
    if data!=None:
        for i in data:
            message = i.get(str(code))  
            if message:  #若接口文件存在且message也存在，返回message
                return message
    return None

def get_result_json(url,status):
    #获取需要对比的json数据
    data = get_value(url,"/config/result.json")
    if data !=None:  #若能获取到值
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None   #如果获取不到data,返回none


def handle_result_json(dict1,dict2):
    #校验json格式，用deepdiff
    """ 
    #1.忽略顺序或重复项列出差异
    t1 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
    t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 3, 2, 3]}}
    print(DeepDiff(t1,t2,ignore_order=True))  #{}

    #2.从比较中排除对象树的一部分，如token、uuid等容易变化的数：exclude_paths:后面跟不验证的key
    dict1 = {"for life": "vegan", "ingredients": ["no meat", "no eggs", "no dairy"]}
    dict2 = {"for life": "vegan", "ingredients": ["veggies", "tofu", "soy sauce"]}
    print(DeepDiff(dict1,dict2,exclude_paths={"root['ingredients']"}))  #{}
    """
    #isinstance(object, classinfo) 判断一个对象是否是已知类型
    #print(isinstance(1,str))   #判断1是不是字符串类型， false

    #只有dict1，dict2都是字典时，才可进行格式校验
    if isinstance(dict1,dict) and isinstance(dict2,dict):  
        cmp_dict = DeepDiff(dict1,dict2).to_dict()  #将验证结果转换成字典格式
        #print(cmp_dict)
        if cmp_dict.get('dictionary_item_added'):
           return False
        else:
           return True
    return False
         
    

    