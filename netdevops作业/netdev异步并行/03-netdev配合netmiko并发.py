from netmiko import ConnectHandler
import time


with open('ip_list.txt') as f:
    start_time = time.time()
    for ips in f.readlines():
        ip = ips.strip()
        
        SW ={
            'device_type':'cisco_ios',
            'ip':ip,
            'username':'cisco',
            'password':'cisco'
        }

        connect = ConnectHandler(**SW)
        print("Successfully connected to " + SW['ip'])
        config_commands = ['line vty 5 15','logiin local','exit']
        output = connect.send_config_set(config_commands)
        print('Time elapsed: %.2f' %(time.time()-start_time))

#同步方式一台一台登录执行总耗时45s

#通过异步代码如下对比
import asyncio
import netdev
import time




async def task(dev):
    async with netdev.create(**dev) as ios:
        config_commands = ['line vty 5 15','logiin local','exit']
        output = await ios.send_config_set(config_commands)
        print(output)

async def run():
    devices = []
    with open('ip_list.txt') as f:
        for ips in f.readlines():
            ip = ips.strip()
        
            dev ={
            'device_type':'cisco_ios',
            'ip':ip,
            'username':'cisco',
            'password':'cisco'
            }
            devices.append(dev)
        tasks = [task(dev) for dev in devices]
        await  asyncio.wait(tasks)

start_time = time.time()
print(f"程序于{time.strftime('%X')}开始运行\n")
asyncio.run(run())
print(f"\n程序于{time.strftime('%X')}结束运行")