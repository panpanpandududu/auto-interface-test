import requests
import unittest

#测试类,继承unittest.TestCase:所有测试用例类继承的基本类
class Test01(unittest.TestCase):
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

    #控制某个case是否执行，可以用skipIf()来判断
    host = 'http://www.imooc.com'
    @unittest.skipIf(host =='http://www.imooc.com','这个case不执行')
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
        print("case03")
        flg1 = "ll"
        flg2 = 'lalala'
        self.assertIn(flg1,flg2,msg = 'flg1不在flg2里面')

if __name__ == "__main__":
    unittest.main()
    # #更改测试用例顺序，用测试套件TestSuite
    # #步骤：1.构建测试套件
    # suite = unittest.TestSuite()
    # #更改测试用例顺序
    # tests = [Test01('test_02'),Test01('test_03'),Test01('test_01')]
    # #将tests添加进测试
    # #单个用addTest(),多个用addTests()
    # suite.addTests(tests)
    # #2.执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)





