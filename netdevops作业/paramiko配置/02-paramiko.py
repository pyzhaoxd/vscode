import paramiko
import time
import getpass

from paramiko.client import AutoAddPolicy

username = input('Username: ')
#getpass 输入密码为密文，安全起见
password = getpass.getpass('Password: ')

#同时为5台设备做配置 vlan10 -vlan20
for i in range(11,16):
    ip = "192.168.1." + str(i)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko,AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password,look_for_key=False)
    print("Successfully connect to ", ip)
    command = ssh_client.invoke_shell()
    command.send("Configure terminal \n")
    for n in range (10,21):
        print("Creating VLAN " + str(n))
        command.send("vlan" + str(n) + "\n")
        command.send("name Python_VLAN" + str(n) + "\n")
        time.sleep(1)

    
    command.send("end\n")
    command.send("wr mem\n")
    time.sleep(2)
    output = command.recv(65535)
    print(output.decode("acsii"))

ssh_client.close


