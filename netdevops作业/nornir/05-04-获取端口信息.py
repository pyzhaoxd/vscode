from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir.core.task import Result, Task
import logging

def get_interfaces(task):
    # 最外侧的结果 索引号最小
    cmd = None
    if task.host.platform in ['ios','cisco_ios']:
        cmd = 'show interface'
        result = task.run(netmiko_send_command, command_string=cmd, use_timing=True,use_textfsm=True,severity_level = logging.DEBUG )
        if not result.failed:
            return Result(host=task.host,result=result.result,severity_level = logging.DEBUG )
        else:
            return Result(host=task.host,result=None, failed=True, severity_level = logging.WARNING )
    else:
        raise Exception('Not supported platform')


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

    results = nr.run(task=get_interfaces)
    print_result(results,severity_level = logging.INFO)
