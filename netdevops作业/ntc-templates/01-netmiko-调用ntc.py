from netmiko import ConnectHandler
import json
from textfsm import TextFSM


dev_info = {
        'device_type': 'cisco_ios',
        'host': '192.168.199.102',  # 用host 和ip均可，系统会自动判断
        'username': 'admin',
        'password': 'admin123!',
        'port': 22,  # 默认是22端口，可以不写，在模拟环境可能会有端口映射，或者是使用Telnet等可以指定其他端口
        'secret': 'admin123！',  # 选填，, 默认值是''，空字符串,这个是enable的密码
    }


#use_textfsm=True 表示调用TextFSM,而TextFSM调用的net-template模板这个步骤在net-templates介绍第6步通过环境变量做好了，indent=2 必须写上
#注意netmiko调用textfsm返回的数据不是字符串，而是列表，所以这里interfaces数据类型为列表。列表里面的数据如JSON阵列一样的json对象，因次可以配置for 和if 来取相应的值
connect = ConnectHandler(**dev_info)
print('Successfully connected to ' + dev_info['ip'])
interfaces = connect.send_command('show ip int brief',use_textfsm=True)
print(json.dumps(interfaces,indent=2))



#以上运行结果将返回一个json格式数据

[
    {
        "intf": "GigabitEthernet0/1",
        "ipaddr":"192.168.1.1",
        "status":"up",
        "proto":"up"
    },

        {
        "intf": "GigabitEthernet0/2",
        "ipaddr":"192.168.1.2",
        "status":"up",
        "proto":"up"
    },

        {
        "intf": "GigabitEthernet0/3",
        "ipaddr":"192.168.1.3",
        "status":"down",
        "proto":"down"
    },

        {
        "intf": "GigabitEthernet0/4",
        "ipaddr":"192.168.1.4",
        "status":"up",
        "proto":"up"
    }
]


#修改之前的脚本 配合for 和if 后去指定数据
#注意netmiko调用textfsm返回的数据不是字符串，而是列表，所以这里interfaces数据类型为列表。列表里面的数据如JSON阵列一样的json对象，因次可以配置for 和if 来取相应的值

SW1 = {
        'device_type': 'cisco_ios',
        'host': '192.168.199.102',  # 用host 和ip均可，系统会自动判断
        'username': 'admin',
        'password': 'admin123!',
        'port': 22,  # 默认是22端口，可以不写，在模拟环境可能会有端口映射，或者是使用Telnet等可以指定其他端口
        'secret': 'admin123！',  # 选填，, 默认值是''，空字符串,这个是enable的密码
    }


#use_textfsm=True 表示调用TextFSM,而TextFSM调用的net-template模板这个步骤在net-templates介绍第6步通过环境变量做好了，indent=2 必须写上
connect = ConnectHandler(**SW1)
print('Successfully connected to ' + SW1['ip'])
interfaces = connect.send_command('show ip int brief',use_textfsm=True)
for interface in interfaces:
    if interface["status"] == 'up':
        print(f'{interface["intf"]} is up!", "ip address":{interface["ipaddr"]}')
