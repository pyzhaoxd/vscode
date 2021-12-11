from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.plugins.inventory import InventoryPluginRegister
import netmiko 

def show_cmds(task, cmds,**kwargs):
    # cmds = task.host.data['cmds']
    # loop_delay_default = 0.2
    # exec_timeout = 60*3
    # max_loops = int(int(exec_timeout)/loop_delay_default)
    outputs = []
    for cmd in cmds:
        result = task.run(netmiko_send_command,
                          command_string=cmd, use_timing=True,**kwargs)
        output = result.result
        outputs.append(output)
    return outputs[0]


# dev = nr.filter(role='spine')
if __name__ == '__main__':
    nr = InitNornir(
        config_file="nornir_end.yaml"
    )
    cmds = ['show ip interface brief']
    results = nr.run(task=show_cmds, cmds=cmds,use_textfsm=True)
    print_result(results)
