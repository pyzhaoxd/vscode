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
# from py2neo.Schema import  ConstraintValidationFailed
import traceback
from py2neo.matching import NodeMatcher, RelationshipMatcher

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://192.168.137.130:7474', auth=('neo4j', 'admin123!'))
nodes_matcher = NodeMatcher(graph)


#
# graph.delete_all()
# graph.schema.create_uniqueness_constraint('Device', 'name')


def get_or_create_node(label, info, id_filed=None):
    try:

        node = Node(label, **info)
        graph.create(node)
        return node
    except Exception as e:
        if 'ConstraintValidationFailed' in str(e):

            try:
                filter_info = {id_filed: info.get(id_filed)}
                node = nodes_matcher.match(label, **filter_info).first()
                return node
            except Exception as e:
                traceback.print_exc()
                print(e)


def get_or_create_neighbor(devices, local_intf, neighbor_intf):
    try:
        print(local_intf)
        r = Relationship(devices[0], 'Neighbor', devices[1], local_intf=local_intf, neighbor_intf=neighbor_intf)
        graph.create(r)
        return r
    except Exception as e:
        traceback.print_exc()
        print(e)


# ---- netmiko_send_command ** changed : False ----------------------------------- DEBUG
# [ { 'capability': 'R S I',
#     'local_interface': 'Eth 0/0',
#     'neighbor': 'netdevops01.netdevops.com',
#     'neighbor_interface': 'Uni Eth 0/0',
#     'platform': 'Linux'},
#   { 'capability': 'R S I',
#     'local_interface': 'Eth 0/2',
#     'neighbor': 'netdevops01.netdevops.com',
#     'neighbor_interface': 'Uni Eth 0/2',
#     'platform': 'Linux'},
#   { 'capability': 'R S I',
#     'local_interface': 'Eth 0/3',
#     'neighbor': 'netdevops01.netdevops.com',
#     'neighbor_interface': 'Uni Eth 0/3',
#     'platform': 'Linux'}]

def create_nodes_and_neighbors(local_dev, cdp_or_lldp_infos):
    for i in cdp_or_lldp_infos:
        local_dev_node = get_or_create_node('Device', {'name': local_dev}, id_filed='name')
        neighbor_node = get_or_create_node('Device', {'name': i['neighbor']}, id_filed='name')
        get_or_create_neighbor((local_dev_node, neighbor_node), local_intf=i['local_interface'],
                               neighbor_intf=i['neighbor_interface'])

        if __name__ == '__main__':
            pass
            # info = {
            #     'name': 'netdevops02'
            # }
            # node1 = get_or_create_node('Device', info, id_filed='name')
            #
            # info = {
            #     'name': 'netdevops01'
            # }
            # node2 = get_or_create_node('Device', info, id_filed='name')
            # r = get_or_create_neighbor((node1,node2),local_intf='eth0/0',neighbor_intf='eth0/0')
            # print(r)
