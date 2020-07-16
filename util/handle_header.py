#处理头文件
import os
import sys
sys.path.append(os.getcwd())

from util.handle_json import read_json

def get_header():
    data = read_json('/config/header.json')
    return data