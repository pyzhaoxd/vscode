from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config,netmiko_save_config
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir.core.task import Result, Task
import logging
from nornir_jinja2.plugins.tasks import template_file 




def set_interfaces(task,interfaces):
    result = task.run(task=template_file,template='ios_interfaces.j2',path='templates',interfaces=interfaces)
    config = result.result
    config_result = task.run(task=netmiko_send_config,config_commands = config.splitlines())
    save_config = task.run(task=netmiko_save_config)
    return save_config



# dev = nr.filter(role='spine')
# https://www.gingerdoc.com/nornir-%E5%A4%84%E7%90%86%E5%99%A8
# 配置的处理可以使用处理器，按需打印或者编写信息到指定log中等等 平台集成
if __name__ == '__main__':
    
    """
       结果的打印是嵌套的，默认的log是打印所有info
       可以适当的调整级别，部分调整为debug级别，想打印的调整为info级别
       最终打印结果的时候打印的是info级别即可

    """
    nr = InitNornir(
        config_file="nornir_end.yaml"
    )
    
    # 实际使用中可以根据设备ip与每个端口的所属设备IP比较进行筛选 
    intfs = [{
        'name':'eth0/0',
        'description': 'config by the nornir jinja2 20210605'
    }]
    results = nr.run(task=set_interfaces,interfaces=intfs)
    print_result(results,severity_level = logging.INFO)
