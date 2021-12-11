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

with open('02-show-vlan.log',mode='r',encoding='utf8') as f:
    dev_text = f.read()

template = TextFSM(open('02-textfsm-template.textfsm'))
vlan_info = template.ParseTextToDicts(dev_text)

print(vlan_info)


