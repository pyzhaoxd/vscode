from netmiko import ConnectHandler

#netmiko 是paramiko的升级版，支持更多的网络设备厂商，并且会自动保持配置，输出回显自动刷新所有内容，不用考虑输入间隔太快导致失败问题

SW2 = {
    'device_type': 'cisco_ios'
    'ip': '192.168.1.1'
    'username': 'cisco'
    'password': 'cisco'
}


connect = ConnectHandler(**SW2)
print("Successfully connected to " + SW2['ip'])
config_commands = ['int loopback 1','ip address 1.1.1.1 255.255.255.0']
output = connect.send_config_set(config_commands)
print(output)

result = connect.send_command('show run int loopback 1')
print(result)