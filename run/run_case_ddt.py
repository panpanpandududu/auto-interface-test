import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

#导入json库
import json
#获取Excel表格数据
from util.handle_excel import excel_data
#获取requests请求
from base.base_request import request
#获取message值
from util.handle_result import handle_result,handle_result_json,get_result_json
#获取cookie值
from util.handle_cookie import get_cookie,get_cookie_value,write_cookie
#获取header的值
from util.handle_header import get_header
#获取依赖数据
from util.codition_data import get_data
#输出测试报告
import HTMLTestRunner
#unittest测试框架
import unittest
#数据驱动模块
import ddt

#Excel数据
datas = excel_data.get_excel_data()
#print(datas)
@ddt.ddt
class RunCaseDdt(unittest.TestCase):

    @ddt.data(*datas)  #将Excel数据接入ddt
    def test_main_case(self,data):
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            case_id = data[0]
            i = excel_data.get_rows_number(case_id)  #获取行号
            is_run = data[2]
            if is_run == 'yes':
                data1 = json.loads(data[7])
                is_depend = data[3]
                if is_depend:
                    depend_data = get_data(is_depend)
                    data_key = data[4]
                    data1[data_key] = depend_data

                method = data[6]
                url = data[5]
                Excepect_method = data[10]  #预期结果方式，即通过什么判断结果
                Excepect_code = data[11]   #预期结果
                cookie_method = data[8]   #cookie的处理方式
                is_header= data[9]
                
                if cookie_method == 'yes':    #1.是否携带cookie
                    cookie = get_cookie_value('app')
                if cookie_method =='write':  #2.写入cookie
                    '''
                    必须先获取到cookie,再写入
                    '''
                    get_cookie={"is_cookie":"app"}
                if is_header == 'yes':
                    header = get_header()

                #发送requests请求
                res = request.run_main(method,url,data1,cookie,get_cookie=get_cookie,header=header)

                #通过对比请求到的message与预期config_message是否相同，判断case是否通过
                code = res['errorCode']
                message = res['errorDesc']   #获取实际结果
                if Excepect_method == 'mec':
                    config_message = handle_result(url,code)  #获取预期结果
                    '''
                    if message == config_message:
                        excel_data.excel_write_data(i,13,'通过')
                    else: 
                        excel_data.excel_write_data(i,13,'失败')
                        excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(message,config_message)
                        excel_data.excel_write_data(i,13,'通过')
                    except Exception as e:
                        excel_data.excel_write_data(i,13,'失败')
                        raise e
                    finally:
                        excel_data.excel_write_data(i,14,json.dumps(res))
                elif Excepect_method == 'errorcode':
                    '''
                    if Excepect_code == code:
                        excel_data.excel_write_data(i,13,'通过')
                    else:
                        excel_data.excel_write_data(i,13,'失败')
                        excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(Excepect_code,code)
                        excel_data.excel_write_data(i,13,'通过')
                    except Exception as e:
                        excel_data.excel_write_data(i,13,'失败')
                        raise e
                    finally:
                        excel_data.excel_write_data(i,14,json.dumps(res))
                elif Excepect_method == 'json':
                    if code ==1000:
                        status_str = 'success'
                    else:
                        status_str = 'error'
                    excepect_json = get_result_json(url,status_str)
                    result = handle_result_json(res,excepect_json)  #校验json
                    '''
                    if result:  #默认为true
                        excel_data.excel_write_data(i,13,'通过')
                    else:
                        excel_data.excel_write_data(i,13,'失败')
                        excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i,13,'通过')
                    except Exception as e:
                        excel_data.excel_write_data(i,13,'失败')
                        raise e
                    finally:
                        excel_data.excel_write_data(i,14,json.dumps(res))



if __name__ == "__main__":
    # unittest.main()
    #识别测试用例
    case_path = base_path +'/run'
    discover = unittest.defaultTestLoader.discover(case_path,pattern='run_case_*.py')
    #执行测试用例
    #unittest.TextTestRunner(discover)
    #创建测试报告输出地址
    file_path = base_path+'/report/report.html'
    with open(file_path,'wb') as f:
        '''
        调用HTMLTestRunner模块下的HTMLTestRunner类，下面为几个参数
        stream 指定测试报告文件
　　     title 定义测试报告的标题
　　     description 定义测试报告的副标题
        '''
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='慕课网接口测试',description='this is test')
       #执行测试用例，通过HTMLTestRunner的run()方法来运行测试套件中的测试用例
        runner.run(discover)