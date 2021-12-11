#try.....except.....处理语句来批量登录5台交换机上面执行show clock 让脚本在SW3-SW4分别因为用户密码不匹配，以及连通性出现故障
#脚本不受的影响继续执行

import paramiko
import time
import getpass
import sys
import socket

from paramiko.client import AutoAddPolicy

username = input('Username: ')
#getpass 输入密码为密文，安全起见
password = getpass.getpass('Password: ')

device_list = sys.agrv[1]
cmd_file = sys.argv[2]

switch_witch_authentication_issue = []
switch_not_reachable = []


#同时不同网段的设备配置EIGRP
with open("03-device-list.txt",mode="r",encoding="utf8") as f:
    for line in f.readlines():
        try:
            ip = line.strip()
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko,AutoAddPolicy())
            ssh_client.connect(hostname=ip,username=username,password=password,look_for_key=False)
            print("Successfully connect to ", ip)
            remote_connection = ssh_client.invoke_shell()
            
            # cmdlist = open(cmd_file,'r')
            # cmdlist.seek(0)
            with open('cmd_file',mode='r',encoding='utf8') as f:
                for line in f.readlines():
                    remote_connection.send(line + "\n")
                time.sleep(2)
                output = remote_connection.recv(65535)
                print(output.decode("acsii"))
        except paramiko.AuthenticationException:       
        #except Exception as e:
            print("User authentication failed for " + ip + ".")
            switch_witch_authentication_issue.append(ip)

        except socket.error:
            print(ip + "is not reachable.")
            switch_not_reachable.append(ip)

            ssh_client.close


print("\nUser authentication failed for below switches:")
for i in switch_witch_authentication_issue:
    print(i)

print("\nBelow switches are not reachable:")
for i in switch_not_reachable:
    print(i)



#代码执行 python3 04-device.py ip_list cmd.txt