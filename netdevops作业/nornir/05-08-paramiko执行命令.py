from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.plugins.inventory import InventoryPluginRegister
from nornir_paramiko.plugins.tasks import paramiko_command

def show_cmds(task, cmds=None):
    # cmds = task.host.data['cmds']
    # loop_delay_default = 0.2
    # exec_timeout = 60*3
    # max_loops = int(int(exec_timeout)/loop_delay_default)
    cmds = ['show interface']
    cmds = cmds if cmds else (
        task.host.data['cmds'] if task.host.data.get('cmds') else [])
    outputs = []
    for cmd in cmds:
        result = task.run(paramiko_command,command=cmd)
        output = result.result
        outputs.append(output)
    return outputs[0]


# dev = nr.filter(role='spine')
if __name__ == '__main__':
    nr = InitNornir(
        config_file="nornir_end.yaml"
    )
    dev = nr.filter(role='spine')
    results = dev.run(task=show_cmds)
    print_result(results)
