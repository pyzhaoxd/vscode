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
        url = 'https://163.53.91.71:9182/vnms/organization/orgs',
        headers={'Accept':'application/json','Content-Type':'application/json'},
        auth=HTTPBasicAuth(username='zhaoxd',password='Zhaoxd@4321'),
        verify=False
    )

    reqOrgDict = json.loads(regs.text)
    #print(json.dumps(reqOrgDict, indent=4, sort_keys=True))


    ransformDictName = []
    transformDictID = []
    for x in reqOrgDict["organizations"]:
        # ransformDictName[x["name"]] = x["globalOrgId"]
        # transformDictID[x["globalOrgId"]] = x["name"]

        out = x['name']
        ransformDictName.append(out)
        out1 =x['globalOrgId']
        transformDictID.append(out1)

    print(ransformDictName)
    print(transformDictID)