import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json



if __name__ == '__main__':
    '''
    requests模块直接调用方法
    status_code是状态码 int类型的
    text 是返回的文本 字符串类型的
    json()是一个函数，会将text loads 转成python对象
    content是二进制的返回对象，处理一些图片的时候可以用到
    '''

    regs = requests.get(
        url = 'https://10.1.1.2:9182/vnms/appliance/filter/Customer5013?offset=0&limit=25',
        headers={'Accept':'application/json','Content-Type':'application/json'},
        auth=HTTPBasicAuth(username='zhaoxd',password='Zhaoxd@4321'),
        verify=False
    )

    reqdevDict = json.loads(regs.text)
    print(reqdevDict)
    # print(json.dumps(reqdevDict, indent=4, sort_keys=True))


    ransformDictName = []
    transformDictID = []
    for x in reqdevDict["appliances"]:
      
        ransformDictName[x["packageName"]] = x["memory"]
        transformDictID[x["memory"]] = x["packageName"]

        out = x['packageName']
        ransformDictName.append(out)
        out1 =x['memoy']
        transformDictID.append(out1)

    print(ransformDictName)
    print(transformDictID)