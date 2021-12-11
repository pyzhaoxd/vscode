from netmiko import ConnectHandler

if __name__ == '__main__':
    '''
    配置三种方式，先写笔者最建议使用的是send_config_set
    传入command的list即可
    连接对象会自动进入config模式
    初学者在使用配置的时候需谨慎，推荐先使用send_command去采集信息，在慢慢掌握之后配置一些风险小的配置，小步慢走
    '''
    net_conn = ConnectHandler(device_type='cisco_ios',
                              host='192.168.199.200',
                              username='cisco',
                              password='cisco',
                              port=22,  # 可选参数, 默认是22端口，可以不写，在模拟环境可能会有端口映射，或者是使用Telnet等可以指定其他端口
                              secret='cisco'  # 选填，, 默认值是''，空字符串,这个是enable的密码
                              )
    net_conn.enable() # 进入特权模式，这个一定要写
    net_conn.config_mode() # 建议写一下，进入config模式
    configs = ['interface fastEthernet 0/0',
                'description configed by netmiko202010150839']
    output = net_conn.send_config_set(config_commands=configs)
    print('send_config_set::',output)
    output = net_conn.save_config()



