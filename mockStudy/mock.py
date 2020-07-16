from unittest import mock
import requests
import unittest
def add():
    a=1
    b=2
    #设定实际返回值为a+b
    return a+b

def use_mock():
    print(add())

#将mock对象赋予被测函数
add = mock.Mock(return_value = 15)
#调用测试一下mock是否成功
#use_mock()  #结果为15，mock成功

#mock接口测试
#定义一个接口请求函数
url = "http://www.imooc.com/login"
data = {
    "username":"111111",
    "password":"11112"
}
def post_request(url,data):
    res = requests.post(url,data).json()
    return res
 
 #测试类
class testLogin(unittest.TestCase):
    #测试post
    def test_post(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username":"111111"
        }
        #创建一个mock对象，return_value是mock的返回值
        success_res = mock.Mock(return_value = data)
        
        #将mock对象赋予被测函数post_request()
        post_request = success_res

        #调用被测函数
        res = post_request()
        #断言实际结果与预期结果
        self.assertEqual(res,'success_res')

if __name__ == "__main__":
    unittest.main()
