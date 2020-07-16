import unittest
#导入需要测试类
#通过os可以调用系统命令
import os
'''
os.name()判断系统类型。 Linux和unix系统会返回posix,windows系统会返回nt
print(os.name)  #posix
os.system() 执行系统命令的模块，返回命令执行的状态码，开启一个子shell执行命令
os.getcwd():返回当前绝对路径，返回类型为str
'''
case_path = os.getcwd()+'/unittestCaseStudy/'
print(case_path)  # /Users/panwumei/Documents/2020软件测试基础学习/python接口自动化测试/unittestCase/

'''
unittest.defaultTestLoader.discover() 中discover()可以自动识别测试用例
discover(start_dir,pattern='test*.py',top_level_dir= None)
start_dir 要测试的模块名或测试用例目录，
pattern='test*.py'表示用例文件名的匹配原则。此处匹配以“test”开头的.py 类型的文件，* 表示任意多个字符
top_level_dir= None 测试模块的顶层目录，如果没有顶层目录，默认为None
'''
discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
unittest.TextTestRunner().run(discover)