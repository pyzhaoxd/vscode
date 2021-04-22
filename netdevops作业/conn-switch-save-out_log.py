from netmiko import ConnectHandler


if __name__ == "__main__":
    net_conn = ConnectHandler(device_type = 'cisco_ios',
                              host ='192.168.0.250',
                              username ='admin',
                              password ='cisco',
                              port ='22',
                              secret ='cisco',

                              )

    output = net_conn.send_command('show ip interface  brief')
    net_conn.disconnect()

    with open('isco_show_int_br.log', mode='w',encoding='utf8') as f:
        f.write(output)