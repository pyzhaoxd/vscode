import sys
import paramiko
import time



ip = "192.168.1.1"
username = "student"
password = "student"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip,username=username,password=password)

print("Successful connection",ip)
ssh_client.invoke_shell()

remote_connection = ssh_client.exec_command('cd /home/admin; mkdir test_server\n')
remote_connection = ssh_client.exec_command('other shell')

print(remote_connection.read())
ssh_client.close



