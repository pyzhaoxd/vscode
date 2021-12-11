from napalm import get_network_driver


#常用的Getter类的API有： get_facts() get_config() get_interfaces() get_bgp_config() get_bgp_interfaces()


driver = get_network_driver('ios')
SW1 = driver('192.168.1.1','cisco','cisco')
SW1.open()

output = SW1.get_arp_table()
output = SW1.get_config()
print(output)



#将输出内容转换为JSON



from napalm import get_network_driver
import json

driver = get_network_driver('ios')
SW1 = driver('192.168.1.1','cisco','cisco')
SW1.open()

output = SW1.get_arp_table()
print(json.dumps(output,indent=2))

