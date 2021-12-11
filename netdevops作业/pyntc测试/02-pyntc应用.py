

#获取目标设备借本信息
#对目标进行配置
#获取目标设备的running-config
#对目标设备的running-config进行beif
#重启目标设备


#获取目标设备的基本信息代码实现如下：

import json
from pyntc import ntc_device as NTC

SW1 = NTC(host='192.168.1.1',username='cisco',password='cisco',device_type='cisco_ios_ssh')
SW1.open()
print(json.dumps(SW1.facts, indent=4))
SW1.close()


#对目标设备进行配置
SW1 = NTC(host='192.168.1.1',username='cisco',password='cisco',device_type='cisco_ios_ssh')
SW1.open()
SW1.config('hostname pyntc_sw1')
SW1.config(['route ospf 1','network 0.0.0.0 255.255.255.255 area 0'])
SW1.close()

#获取目标设备的running-config
SW1 = NTC(host='192.168.1.1',username='cisco',password='cisco',device_type='cisco_ios_ssh')
SW1.open()
run = SW1.running_config
print(run)
SW1.close()


#对目标设备的running-config进行备份
SW1 = NTC(host='192.168.1.1',username='cisco',password='cisco',device_type='cisco_ios_ssh')
SW1.open()
SW1.backup_running_config('SW1_config.cfg')
SW1.close()

#对目标设备进行重启
SW1 = NTC(host='192.168.1.1',username='cisco',password='cisco',device_type='cisco_ios_ssh')
SW1.open()
SW1.save()
SW1.reboot(confirm=True)