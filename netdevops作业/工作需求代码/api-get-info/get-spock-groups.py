from asyncio.windows_events import NULL
from email.mime import application
from re import A
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
#applianceLocation_info 
    regs = requests.get(
        url = 'https://10.1.1.2:9182/vnms/appliance/appliance?offset=0&limit=1000',
        headers={'Accept':'application/json','Content-Type':'application/json'},
        auth=HTTPBasicAuth(username='zhaoxd',password='Zhaoxd@54321'),
        verify=False
    )

    reqdevDict = json.loads(regs.text)
    # print(reqdevDict)
    output = json.dumps(reqdevDict, indent=4, sort_keys=True)
    #print(output)



    with open('appliances.json','w') as f:
        f.write(output)


#Templates
    regs1 = requests.get(
        url = 'https://10.1.1.2:9182/vnms/sdwan/workflow/templates?deep=true&offset=0&limit=20000',
        headers={'Accept':'application/json','Content-Type':'application/json'},
        auth=HTTPBasicAuth(username='zhaoxd',password='Zhaoxd@54321'),
        verify=False
    )


    reqdevDict1 = json.loads(regs1.text)
    #print(reqdevDict)
    output1 = json.dumps(reqdevDict1, indent=4, sort_keys=True)
    #print(output)

    with open('Customer.json','w') as f:
        f.write(output1)



    
#device-groups
    regs2 = requests.get(
        url = 'https://10.1.1.2:9182/nextgen/deviceGroup?organization&offset=0&limit=1000',
        headers={'Accept':'application/json','Content-Type':'application/json'},
        auth=HTTPBasicAuth(username='zhaoxd',password='Zhaoxd@54321'),
        verify=False
    )


    reqdevDict2 = json.loads(regs2.text)
    #print(reqdevDict)
    output2 = json.dumps(reqdevDict2, indent=4, sort_keys=True)
    #print(output2)

    with open('Customer.json','w') as f:
        f.write(output2)
        
        
    
    device_groups= []
    device_templates = []
    for x in reqdevDict2["device-group"]:
        out = x['name']
        out3 =x["poststaging-template"]
        device_groups.append(out)
        device_templates.append(out3)
    
    # for i in device_groups:
    #     print(i)

    # for o in device_templates:
    #     print(o)


    def get_applianceName():
        applianceName = []
        for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:      
            out1 =x["applianceLocation"]['applianceName']
            applianceName.append(out1)

        for z in applianceName:
            print(z)
    get_applianceName()


    def get():
        applianceName = []
        for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:      
            out1 =x["applianceLocation"]
            applianceName.append(out1   
        device_name = map(lambda x:x.get('applianceName'),applianceName)
        # print(list(device_name))
        device_locationId = map(lambda x:x.get('locationId'),applianceName)
        # print(list(device_locationId))
        device_latitude = map(lambda x:x.get('latitude'),applianceName)
        # print(list(device_latitude))
        device_longitude= map(lambda x:x.get('longitude'),applianceName)
        # print(list(device_longitude))
        device_type= map(lambda x:x.get('type'),applianceName)
        #print(list(device_type))
        a = zip(device_name,device_locationId,device_latitude,device_longitude,device_type)
        for i in a:
            print(i)              
    get()