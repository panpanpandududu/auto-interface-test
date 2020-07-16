#处理数据依赖
import os 
import sys
sys.path.append(os.getcwd())

#导入excel模块，获取所依赖的case并执行
from util.handle_excel import excel_data
#jsonpath-rw库:从多层嵌套json中解析所需要的值
from jsonpath_rw import jsonpath,parse
import json


#解析数据（解析Excel对应的前置条件数据）
def split_data(data):  #这个data指的是Excel表格里前置条件里的数据
    '''
    text = '123a456'
    print(text.split('a',1) )    #前一个为分割字符，后一个为分割次数  [123,456]
    '''
    case_id = data.split('>')[0]
    case_data = data.split('>')[1]
    return case_id,case_data

#获取数据依赖所在行的返回结果
def depend_data(data):
    '''
    获取依赖结果集
    '''
    case_id = split_data(data)[0]  #获取依赖case
    row_number = excel_data.get_rows_number(case_id)  #获取依赖case所在行
    data =excel_data.get_cell_value(row_number,14)  #获取依赖case请求后的返回结果
    #print(type(data))  字符串
    return data
    

def get_depend_data(data,rule_str):
    '''
    获取依赖结果集中的特定字段
    ''' 
    # data = {
    #     'status':0,
    #     'data':{
    #         'banner':[
    #             {
    #                 'id':9,
    #                 'type':5,
    #             }
    #         ]
    #     }
    # }
    #解析规则
    # rule_str = 'data.banner[*].id'
    # 把返回回来的字符串data转化为json/dict 类型
    res_data = json.loads(data)
    json_exe = parse(rule_str)
    #从对应json中寻找解析规则
    madle = json_exe.find(res_data)
    return [match.value for match in madle]
    # for match in madle:
    #     return match.value

def get_data(data):
    '''
    依赖数据重构
    '''
    #1.获取依赖数据集
    res = depend_data(data)
    #2.获取解析规则
    rule_data = split_data(data)[1]
    #3.获取结果集中特定字段
    return get_depend_data(res,rule_data)



# if __name__ == "__main__":
    #print(depend_data("imooc_002>data:banner:id"))
    # print(get_depend_data())