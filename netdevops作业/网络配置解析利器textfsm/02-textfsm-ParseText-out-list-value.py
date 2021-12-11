from re import template
from textfsm import TextFSM


output = '''
N7K# show vlan

VLAN    NAME                           Status                     Ports
----------------------------------------------------------------------------------------
1       default                        active                     Eth1/1,Eth1/2,Eth1/3
                                                                  Eth1/4

2       VLAN002                        active                     Po100,Eth1/49,Eth1/50
3       VLAN003                        active                     Po100,Eth1/49,Eth1/50
4       VLAN004                        active                     Po100,Eth1/49,Eth1/50
5       VLAN005                        active                     Po100,Eth1/49,Eth1/50
6       VLAN006                        active                     Po100,Eth1/49,Eth1/50
7       VLAN007                        active                     Po100,Eth1/49,Eth1/50
8       VLAN008                        active                     Po100,Eth1/49,Eth1/50
9       VLAN009                        active                     Po100,Eth1/49,Eth1/50
10      VLAN0010                       active                     Po100,Eth1/49,Eth1/50
11      VLAN0011                       inactive                   Po100,Eth1/49,Eth1/50

'''


with open('02-textfsm-template.textfsm',mode='r',encoding='utf8') as f:
    template = TextFSM(f)

#查看格式数据输出
#print(template.ParseText(output))


#配合for 循环迭代输出，最后配合if 输出 Status为inactive的VLAN

out = template.ParseText(output)

for i in out:
    print(i)
