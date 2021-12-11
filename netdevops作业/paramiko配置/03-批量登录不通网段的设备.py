import paramiko
import time
import getpass

from paramiko.client import AutoAddPolicy

username = input('Username: ')
#getpass 输入密码为密文，安全起见
password = getpass.getpass('Password: ')

#同时不同网段的设备配置EIGRP
with open("03-device-list.txt",mode="r",encoding="utf8") as f:
    for line in f.readlines():
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko,AutoAddPolicy())
        ssh_client.connect(hostname=ip,username=username,password=password,look_for_key=False)
        print("Successfully connect to ", ip)
        remote_connection = ssh_client.invoke_shell()
        remote_connection.send("Configure terminal \n")
        remote_connection.send("route eigrp 1 \n")
        remote_connection.send("end \n")
        remote_connection.send("write \n")
        time.sleep(1)
        output = remote_connection.recv(65535)
        print(output.decode("acsii"))
    ssh_client.close
