
#Configuration： 配置替换(config.replace)---合并(config.merge)----比对(compare Config)----原子更换(Atomic changes)----回滚(Rollback)

#第一步首先创建一个设备的.cfg配置文件，然后通过load_merge_candidate()函数读取配置文件将命令通过SCP协议发送到目标设备，接着通过commit_config()将这些命令在设备执行，注意需要在设备开启scp Server服务

from napalm import get_network_driver


driver = get_network_driver('ios')
SW1 = driver('192.168.1.1','cisco','cisco')
SW1.open()

SW1.load_merge_candidate(filename='02-napalm_config.cfg')
SW1.confirm_commit()


