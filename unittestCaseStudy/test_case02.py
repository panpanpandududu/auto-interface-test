import unittest
import sys
'''
导入sys,根据sys.path的路径来搜索module.name(模块名)
import sys  #sys是system缩写
sys.path 输出是一个列表，其中第一项是空串''，代表当前目录，即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）。 
'''
import os
base_path = os.getcwd()
sys.path.append(base_path)  #为下述引入模块base_request提供搜索路径
#引入在Base中封装好的方法
from Base.base_request import request

url = "http://www.imooc.com"
data = {
    "username":"1111",
    "password":"22222"
}
#测试类,继承unittest.TestCase
class Test02(unittest.TestCase):
    # def setUp(self):
    #     print("每个case开始时执行")
    # def tearDown(self):
    #     print("每个case结束时执行")

    @classmethod
    def setUpClass(cls):
        print("在所有case开始时执行，且只有一个")
    @classmethod
    def tearDownClass(cls):
        print("在所有case结束后执行，且只有一个")
    
    def test_01(self):
        print("case01")
        flag = True
        #如果断言正确，则不会提示msg
        self.assertTrue(flag,msg = 'flag为true')
        
    def test_02(self):
        print("case02")
        str1 = 'hahaha'
        str2 = 'llll'
        #如果断言不正确，则提示msg
        self.assertEqual(str1,str2,msg = '字符串不相等')

    def test_03(self):
        res = request.run_main('get',url,data)
        print(res)
        #return res
       

if __name__ == "__main__":
    # unittest.main()
    # #更改测试用例顺序，用测试套件TestSuite
    # #步骤：1.构建测试套件
    suite = unittest.TestSuite()
    # #更改测试用例顺序
    tests = [Test02('test_02'),Test02('test_03'),Test02('test_01')]
    # #将tests添加进测试
    # #单个用addTest(),多个用addTests()
    suite.addTests(tests)
    # #2.执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)





