1.准备工作
sudo apt install python3
sudo apt install python3-venv

2.配置python虚拟环境
cd /
cd pyats-test
python3 -m venv .
source bin/activate
pip install 'ipyats[full]'

3.产生testbed yaml文件
cd pyats-test
mkdir codes
cd codes
pyats create testbed interactive --output testbed.yaml文件(手动交互式输入，比如设备ip，用户名，密码，enable密码，设备hostname...)


4.查看testbed yaml文件

在当前目录output testbed.yaml 生成的文件是json格式（可以通过python转为为字典，进行函数语法进行操作）
cat testbed.yaml
[devices:
    nx-osv-1:
        type: 'router'
        os: 'nxos'
        platform: n9kv
        alias: 'uut'
        credentials:
            default:
                username: admin
                password: admin
        connections:
            cli:
                protocol: ssh
                ip: "172.25.192.90"


    csr1000v-1:
        type: 'router'
        os: 'iosxe'
        platform: asr1k
        alias: 'helper'
        credentials:
            default:
                username: cisco
                password: cisco
        connections:
            cli:
                protocol: ssh
                ip: "172.25.192.90"]
关键字段「hostname alias os platform type ip protocol port...」

5.校验testbed yaml
pyats validate testbed testbed.yaml

6.进入pyats python shell
pyats shell --testbed-file testbed.yaml
等价与
>>> from pyats.topology.loader import loader
>>> testbed = load('testbed.yaml')

>>> r1 = testbed.devices['CSR1']
>>> r1.connect()


7.进行交互式输出并打印
>>> parsed = r1.parse('show version')
>>> from pprint import pprint
>>> pprint(parsed)


8. 分析命令清单
https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers


9.CLI解析命令并输出到文件
注意snapshot1是一个目录，目录里面包含原始配置输出和分析后的配置
pyats parsee "show version" "show ip interface brief" --testbed-file testbed.yaml  -- output snapshot1

10.CLI解析命令-指定设备
pyats parsee "show version" "show ip interface brief" --testbed-file testbed.yaml --devices CSR1 -- output snapshot1


11.Learn Device feature

>>>learned=r1.learn('ospf') [支持all-不推荐]
>>>learned_dict=learned.to_dict()
>>>learned_dict


12.CLI Learn Device
pyats learn ospf interface --testbed-file testbed.yaml --devices CSR1 --output r1-ospf-interface


13.Compare Network States
pyats parsee "show version" "show ip interface brief" --testbed-file testbed.yaml --devices CSR1 -- output snapshot1
pyats parsee "show version" "show ip interface brief" --testbed-file testbed.yaml --devices CSR1 -- output snapshot2
pyats diff snapshot1 snapshot2

14.对比排除指定字段信息，比如bgp的time时间
pyats diff snapshot1 snapshot2 --exclude "updated" "time"


15.配置设备
>>> r1=testbed.devices['CSR1']
>>>r1.connect()
>>>from genie.conf.base import interface
>>>iosxe_interface=interface(devices=r1,name='GigabitEthernet1')
>>>iosxe_interface.ipv4='1.1.1.1'
>>>iosxe_interface.enabled=True
>>>from pprint import pprint
>>>pprint(iosxe_interface._to_dict())
>>>pprint(iosxe_interface.build_config(apply=False))  只做展示
>>>iosxe_interface.build_config()应用配置


16.Netmikoi使用pyATS 
对输手动保持的数据，进行数据格式化输出
安装支持(注意在python venv)pip install pyats_genie_command_parse
form pyats_genie_command_parse import GenieCommandParse
from netmiko_0_client import netmiko_show_cred
from pprint import pprint

raw_result = netmiko_show_cred('1.1.1.1','admin','cisco123','show ip interface brief')
print(raw_result)

parse_obj = GenieCommandParse(nos='ios')
data = parse_obj.parse_string(show_command='show ip interface brief',
                            show_output_data=raw_result)

pprint(data)


17.Netmikoi使用pyATS格式化解析输出
pip3 install pyats
pip3 install genie
from netmiko import Netmiko

def netmiko_show_cred_use_genie(host,username,password,cmd,enabled='Cisco123',ssh=True):
    devices_info = {
                    'host':host,
                    'username':username,
                    'password':password,
                    'device_type': 'cisco_ios' if ssh else 'cisco_ios_telnet',
                    'secret':enable
    }
    try:
        net_connect = Netmiko(**devices_info)
        return net_connect.send_command(cmd,
                                        use_textfsm=True,
                                        use_genie=True)
    except Exception as e:
        print(f'connection error ip: {host} error:{str(e)}')
        return

if __name__ == '__main__':
    from pprint import pprint
    parse_result = netmiko_show_cred_use_genie('192.168.1.1',
                                                'admin',
                                                'cisco123'
                                                'show ip interface brief',        
                                                )

    pprint(parse_result)
