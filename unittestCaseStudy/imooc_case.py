import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from base.base_request import request
import unittest
import json
#mock数据
from unittest import mock
#生成测试报告
import HTMLTestRunner
'''
上述为引入模块
'''
host = 'http://www.imooc.com/'

#定义一个方法来读取本地存储数据，所有的数据包括在一起
def read_jsons():
    with open(base_path+"/config/user_data.json") as f:
        data = json.load(f)
    return data
#定义一个方法根据键值对取出相应的数据
def get_data(key):
    data = read_jsons()
    return data[key]

#测试类
class ImoocCase(unittest.TestCase):
    def test_banner(self):
        url = host+'api3/getbanneradvertver2'
        data = {
            'timestamp':'1561269343481',
            'uid':'7213561',
            'token':'7ad09430cbaf927af642ab843ec374ef',
            'type':'1',
            'marking':'androidbanner',
            'uuid':'41b650ef846688193728ff7381eb6c1c',
            'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY'
        }

        #mock一个对象来返回mock值
        mock_res = mock.Mock(return_value=get_data('/api3/getbanneradvertver2'))
        request.run_main = mock_res
        res = request.run_main('post',url,data)
        self.assertEqual(res['errorCode'],1002)
    
    def beta4(self):
        url = host+'api3/beta4'
        data = {
            'timestamp':'1561269343486',
            'uid':'7213561',
            'token':'66640986fb118dda4334719ac8afbf89',
            'uuid':'41b650ef846688193728ff7381eb6c1c',
            'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY',
        }
        mock_method = mock.Mock(return_value=get_data('/api3/beta4'))
        request.run_main = mock_method
        res = request.run_main('post',url,data)
        self.assertEqual(res['errorCode'],1000)

if __name__ == "__main__":
    #unittest.main()

    #构建测试套件
    suite = unittest.TestSuite()
    #添加测试
    suite.addTest(ImoocCase('test_banner'))
    suite.addTest(ImoocCase('beta4'))
    #创建测试报告输地址
    file_path = base_path+'/report/report.html'
    with open(file_path,'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report,title='这是一个接口测试',description='第一个生成报告')
        runner.run(suite)
    report.close()
