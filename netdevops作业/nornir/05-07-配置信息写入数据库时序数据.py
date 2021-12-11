from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir.core.task import Result, Task
import logging
from elasticsearch import Elasticsearch,helpers
from datetime import datetime
import time

def get_interfaces(task):
    cmd = None
    if task.host.platform in ['ios','cisco_ios']:
        cmd = 'show interface'
        result = task.run(netmiko_send_command, command_string=cmd, use_timing=True,use_textfsm=True,severity_level = logging.DEBUG )
        if not result.failed:
            return Result(host=task.host,result=result.result,severity_level = logging.INFO )
        else:
            return Result(host=task.host,result=None, failed=True, severity_level = logging.WARNING )
    else:
        raise Exception('Not supported platform')

def get_and_post_interfaces(task,index='interfaces'):
    intfs_result = get_interfaces(task=task)
    if not intfs_result.failed:
        data = intfs_result.result
        for i in data:
            i['nos_ip'] = task.host.hostname
        return info_2_cmdb(index,data)
    else:
        return '失败'


def info_2_cmdb(index_name, data):
    es = Elasticsearch(["http://192.168.137.130:9200"])
    es.indices.create(index=index_name, ignore=400)
    actions = []
    for i in data:
        i['@timestamp'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+0800")
        action  = {
            '_index':index_name,
            '_source': i
        }
        actions.append(action)

        
    resp = helpers.bulk(es, actions)
    return str(resp)




# dev = nr.filter(role='spine')
if __name__ == '__main__':
    """
       结果的打印是嵌套的，默认的log是打印所有info
       可以适当的调整级别，部分调整为debug级别，想打印的调整为info级别
       最终打印结果的时候打印的是info级别即可

    """
    nr = InitNornir(
        config_file="nornir_end.yaml"
    )
    while True:
        results = nr.run(task=get_and_post_interfaces)
        print_result(results,severity_level = logging.INFO)
        time.sleep(5)
