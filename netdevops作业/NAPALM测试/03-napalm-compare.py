from napalm import get_network_driver


driver = get_network_driver('ios')
SW1 = driver('192.168.1.1','cisco','cisco')
SW1.open()

SW1.load_merge_candidate(filename='02-napalm_config.cfg')

differences = SW1.compare_config()
if len(differences) > 0:
    print(differences)
    SW1.commit_config()
else:
    print('NO change needed.')
    SW1.discard_config()


#注意输出结果，如果输出内容前面有+号，表示配置文件和设备里面的对比缺少命令，通过commit_config()将缺少的进行提交。