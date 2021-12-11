import requests
from requests.auth import HTTPBasicAuth
import json
import sys
import time


if __name__ == '__main__':
    '''
    requests模块直接调用方法
    status_code是状态码 int类型的
    text 是返回的文本 字符串类型的
    json()是一个函数，会将text loads 转成python对象
    content是二进制的返回对象，处理一些图片的时候可以用到
    '''

    regs = requests.get(
        url = 'https://10.1.1.2:9182/vnms/appliance/appliance?offset=0&limit=300',
        headers={'Accept':'application/json','Content-Type':'application/json'},
        auth=HTTPBasicAuth(username='zhaoxd',password='Zhaoxd@4321'),
        verify=False
    )

    reqdevDict = json.loads(regs.text)
    # print(reqdevDict)
    output = json.dumps(reqdevDict, indent=4, sort_keys=True)
    #print(output)



    with open('appliances.json','w') as f:
        f.write(output)

    ransformDictName = []
    transformDictIp = []
    for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:
        out = x['name']
        ransformDictName.append(out)
        out1 =x['ipAddress']
        transformDictIp.append(out1)

    # print(ransformDictName)
    # print(transformDictIp)

    a = zip(ransformDictName,transformDictIp)
    for i in a:
        print(i)
        # b = 'sdwan_ipaddress-' +  time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) + '.txt'
        # with open(b,mode='w') as j:
        #     yield i
        #     j.write(i[0] +'\t' + i[1])

    
  


   
       

     