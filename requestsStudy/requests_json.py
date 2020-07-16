#json本身是一种轻量的数据交换格式，易于阅读和编写
#使用json函数首先需要导入json库
import json 
#json.dumps():将python对象编码成字符串，即将字典,列表等转换成字符串
#jsons.loads():将已编码好的json字符串解码为python对象
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
#print(type(data)) #<class 'list'>
jsons = json.dumps(data)
#print(jsons)  #[{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]
#print(type(jsons))  #<class 'str'>

#使用参数让json数据格式化输出
json_default = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
#print(json_default)
'''
json_default最终结果显示：
[
    {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5
    }
]
'''

#json.loads() 解码，将字符串解码成python数据类型
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
print(text)  #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}