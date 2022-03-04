
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

    def get():
        applianceName = []
        for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:      
            out1 =x["applianceLocation"]
            applianceName.append(out1)

           

        # for y in reqdevDict1["versanms.sdwan-template-list"]:
        #     applianceName.append(y)

        # templates_name = map(lambda x:x.get('templateName'),applianceName)

            
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

        ping_status= map(lambda x:x.get('ping-status'),applianceName)


        device_groups= []
        device_templates = []
        for x in reqdevDict2["device-group"]:
            out = x['name']
            out3 =x["poststaging-template"]
            device_groups.append(out)
            device_templates.append(out3)

        ping_status = []
        for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]: 
             out1 =x["ping-status"]
             ping_status.append(out1)



     
    
  

        #a = zip(device_name,device_locationId,device_latitude,device_longitude,device_type,device_groups,device_templates)
        a = zip(device_name,device_locationId,device_latitude,device_longitude,device_type,ping_status)
        
        #print(a)
        print("('Device_Name','Device_LocationId','Device_Latitude','Device_Longitude','Device_Type','Device_Groups','evice_templates')")
        for i in a:
            print(i)      

             
    get()
        
        
    
   
    

    #调试模式 >>python run-script.py >c.json
    # for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:      
    #     print(x)


 
    # for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:
    #     # ransformDictName[x["name"]] = x["ipAddress"]
    #     # transformDictIp[x["ipAddress"]] = x["name"]

    #     out = x['name']
    #     appliances_list.append(out)

    # def get_applianceName():
    #     applianceName = []
    #     for x in reqdevDict["versanms.ApplianceStatusResult"]["appliances"]:      
    #         out1 =x["applianceLocation"]['applianceName']
    #         applianceName.append(out1)

    #     for z in applianceName:
    #         print(z)
    # get_applianceName()


    