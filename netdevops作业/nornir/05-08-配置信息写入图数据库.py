from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir.core.task import Result, Task
import logging
from elasticsearch import Elasticsearch, helpers
from datetime import datetime
import time
# coding:utf-8
from py2neo import Graph, Node, Relationship
from neo4jhelper import create_nodes_and_neighbors





def cdp_info_2_neo4jdb(task):
    if task.host.platform in ['ios', 'cisco_ios']:
        cmd = 'show cdp neighbors'
        result = task.run(netmiko_send_command, command_string=cmd, use_timing=True, use_textfsm=True,
                          severity_level=logging.DEBUG)
        infos = result.result

        for i in infos:
            i['local_interface'] = ''.join(i['local_interface'].split())
            i['neighbor_interface'] = ''.join(i['neighbor_interface'].split()[-2:])

            i['neighbor'] = i['neighbor'].split('.')[0]
        create_nodes_and_neighbors(task.host.name, cdp_or_lldp_infos=infos)
    return 'success'



# create(d1:Device {name:"netdevops01",ip:192.168.137.201})-[neighbor:Neighbor{local_interface:'eth0/0',neighbor_interface:'eth0/0'}]->(d2:Device {name:"netdevops02",ip:192.168.137.202}) return d1,neighbor,d2
if __name__ == '__main__':
    """
       结果的打印是嵌套的，默认的log是打印所有info
       可以适当的调整级别，部分调整为debug级别，想打印的调整为info级别
       最终打印结果的时候打印的是info级别即可

    """
    nr = InitNornir(
        config_file="nornir_end.yaml"
    )
    results = nr.run(task=cdp_info_2_neo4jdb)

    print_result(results, severity_level=logging.DEBUG)
