import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
import sys



if __name__ == '__main__':
    '''
    requests模块直接调用方法
    status_code是状态码 int类型的
    text 是返回的文本 字符串类型的
    json()是一个函数，会将text loads 转成python对象
    content是二进制的返回对象，处理一些图片的时候可以用到
    '''

    regs = requests.get(
        url = 'https://10.1.1.2:9182/vnms/appliance/filter/Customer5015?offset=0&limit=50',
        headers={'Accept':'application/json','Content-Type':'application/json'},
        auth=HTTPBasicAuth(username='zhaoxd',password='Zhaoxd@4321'),
        verify=False
    )

 

    reqdevDict = json.loads(regs.text)
    #print(reqdevDict)
    output = json.dumps(reqdevDict, indent=4, sort_keys=True)
    #print(output)

    with open('Customer.json','w') as f:
        f.write(output)

    ransformDictName = []
    transformDictIp = []
    networkconnect= []
    for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:
        out = x['name']
        ransformDictName.append(out)
        out1 =x['ipAddress']
        transformDictIp.append(out1)
        out2 = x['ping-status']
        networkconnect.append(out2)




    a = zip(ransformDictName,transformDictIp,networkconnect)
    for i in a:
        print(i)
                                                         