import paramiko
import time

ip = "192.168.1.1"
username = "cisco"
password = "cisco"


ssh_client = paramiko.SSHClient()
#Paramiko接受未知的公钥，标准配置
ssh_client.set_missing_host_key_policy(paramiko,AutoAddPolicy())
#look_for_key=False关闭SSH免密登录
ssh_client.connect(hostname=ip,username=username,password=password,look_for_key=False)

print("Successfully connected to ", ip)
#唤醒shell
command = ssh_client.invoke_shell()
command = send("configure terminal\n")
command = send("int loop l\n")
command = send("ip address 1.1.1.1 255.255.255.0\n")
command = send("end\n")
command = send("write mem\n")

time.sleep(2)
output = command.recv(65535)
print(output.decode(ascii))

#推出SSH
ssh_client.close