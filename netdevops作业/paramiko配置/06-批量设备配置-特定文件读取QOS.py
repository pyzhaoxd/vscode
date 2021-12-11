
# 不同型号的网络设备，配置命令不同，实现运行脚本的时候指定配置的网络设备文件和配置内容文件
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
with open(device_list,mode="r",encoding="utf8") as f:
    for line in f.readlines():
        try:
            ip = line.strip()
            ssh_client = paramiko.SSHClient()
            
            ssh_client.connect(hostname=ip,username=username,password=password,look_for_key=False)
            ssh_client.connect
            print("Successfully connect to ", ip)
            remote_connection = ssh_client.invoke_shell()
            with open(cmd_file,mode='r',encoding='utf8') as h:
                for line in h.readlines():
                    remote_connection.send(line + "\n")
                    time.sleep(1)
                    output = remote_connection.recv(65535)
                    print(output.decode('ascii'))
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