import os
import sys
sys.path.append(os.getcwd())

from ddt import ddt,data
import unittest
from util.handle_excel import excel_data

#数据参数,导入Excel数据
#datas = [[1,2,3],[4,5,6],[7,8,9]]
datas = excel_data.get_excel_data()
#首先在测试类前先声明使用(执行)ddt
@ddt    #@xxx代表执行xxx
class testcase01(unittest.TestCase):
    def setUp(self):
        print('每个case开始时执行')
    def tearDown(self):
        print('每个case结束时执行')

    @data(*datas)  #当数据通过变量的方式传递时，变量前面加*    #将Excel数据接入ddt
    def test_01(self,data1):
                #case编号	作用	是否执行	前置条件	依赖key	url	method	data	cookie操作	header操作	预期结果方式	预期结果	result	数据
        case_id,function,is_run,condition,depend_key,url,method,request_data,cookie,header,execpet_method,execpet,result,result_data =data1
        #casename,casenum,isrun,method,cookie = data1
        print("this is test case",case_id,function,is_run,condition,depend_key,url,method,request_data,cookie,header,execpet_method,execpet,result,result_data)


if __name__ == "__main__":
    unittest.main()
