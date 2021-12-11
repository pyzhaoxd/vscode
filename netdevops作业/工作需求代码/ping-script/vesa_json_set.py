#!/usr/bin/env python
#coding: utf-8
import sys
import json

# # 加载json文件
path1 = r'jsontest1.json'
with open(path1, 'rb') as f:
    try:
        data = json.load(f)
    except:
        pass
        print("please check the jsonfile")


def flat(data,command="set"):

    if isinstance(data,dict):
        for key,values in data.items():

            if key in ['vni','tvi','ptvi','data']:
                key=""
            elif key=='interfaces:interfaces':
                command = command + ' ' + 'interfaces'

            elif key in ['name','id']:
                command=command+' '+str(values)
                command=command.strip()
                values=""

            elif key=='addr':
                command = command + ' ' + 'address'
                command = command + ' ' + values
                print("%s" %(command))
                continue


            elif key in ['address','enable']:
                command = command.strip()
            elif key == 'description':
                print('%s %s "%s"'%(command,key,values))
                continue


            elif key in ['type','priority','preempt-mode','fast-interval','virtual-address','warmup-interval',
                         'remote-address','vlan-id','mode','paired-interface']:
                print("%s %s %s" %(command,key,values))
                continue

            else:
                command=command+' '+str(key)
                command=command.strip()

            flat(values,command)
    elif isinstance(data,list):
        for listitem in data:

            flat(listitem,command)
    else:

        command=command+' '+str(data)
        command=command.strip()
        command=command.replace('True','enable true')
        print(command)


flat(data)