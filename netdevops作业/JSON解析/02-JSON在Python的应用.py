import json

#json主要有四个模块
# json.dump
# 将Python对象序列化为Json格式的数据流并写入文件类型的对象中

# json.dumps
# 将Python对象序列化为Json格式的字符串

# json.load
# 从文件类型的对象中读取Json格式的数据并反序列化成Python对象

# json.loads
# 将包含Json格式数据的字符串反序列化成Python对象


# JSON类型	Python类型
# {}	        dict
# []	        list
# "string"	    str
# 1234.56	    int或float
# true/false	True/False
# null	        None


#测试dumps() 
a = json.dumps('parry')
print(type(a))

b = {"c":0,"b":0,"a":0}
c = json.dumps(b,sort_keys=True)
print(c)
print(type(c))

print(type({"c":0,"b":0,"a":0}))
print(type(json.dumps([1,2,3])))
#通过以上的测试说明dumps转换JOSN格式后，都是字符串类型

#测试loads()

json_list = '[1,2,3]'
print(type(json_list))
python_list = json.loads(json_list)
print(type(python_list),python_list)

json_dictionary = '{"Vendor":"cisco","Model":"2960"}'
python_dict = json.loads(json_dictionary)
print(type(python_dict),python_dict)


#测试dump()
#读取json文件
a ={
    "sites":[
        {"name":"360","url": "www.360.com"},
        {"name":"google", "url": "www.google.com"},
        {"name":"baidu","url":"www.baidu.com"},
    ]}

b ={
    
        "name":"360","url": "www.360.com",
        "name":"google", "url": "www.google.com",
        "name":"baidu","url":"www.baidu.com",
    }


序列化到文件中
with open('test.json', 'w',encoding='utf8') as fp:
    json.dump(a, fp, indent=4)

# # 反序列化文件中的内容
with open('test.json', 'r',encoding='utf8') as fp:
    c = json.load(fp)
    print(c)
