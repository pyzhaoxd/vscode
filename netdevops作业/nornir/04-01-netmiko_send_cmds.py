from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir.core.plugins.inventory import InventoryPluginRegister

nr = InitNornir(
    config_file="nornir_end.yaml"
)


def show_cmds(task):
    # cmds = task.host.data['cmds']
    cmds = ['show version']
    outputs = []
    for cmd in cmds:
        result = task.run(netmiko_send_command, command_string=cmd)
        output = result.result
        outputs.append(output)
    return outputs

# dev = nr.filter(role='spine')
results = nr.run(task=show_cmds)
print_result(results)
