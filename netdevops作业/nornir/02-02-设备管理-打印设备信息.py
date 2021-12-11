#!/usr/bin/env python

from nornir import InitNornir

nr = InitNornir(
    config_file="nornir_complex_inventory.yaml"
)
# list hosts

#nr.inventory.hosts.items()返回时一个对象
hosts = nr.inventory.hosts
# print(hosts)
#
# hosts是一个特殊的对象，类似字典的方法，key值是host的字符串，value是一个内置的类host
# for hostname, host_obj in hosts.items():
#     print('hostname, type(hostname):', hostname, type(hostname)) #type(hostname)是str
#     print('host_obj, type(host_obj):', host_obj, type(host_obj))
#     print('host_obj.hostname:', host_obj.hostname)
#     print('host_obj.username:', host_obj.username)
#     print('host_obj.data：', host_obj.data)

# # list groups
# print(nr.inventory.groups)

# # groups类似hosts 是一个特殊的对象
# groups = nr.inventory.groups
# for group_name, group_obj in groups.items():
#     print(group_name, type(group_name))
#     print(group_obj, type(group_obj))
#     print(group_obj.platform)
#     print(group_obj.username)


#defaults 没有item()方法
print(nr.inventory.defaults)




