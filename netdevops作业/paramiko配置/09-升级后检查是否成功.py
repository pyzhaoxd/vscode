from jinja2.utils import pass_environment
import paramiko
import time
import re
import socket
import getpass

from paramiko.client import AutoAddPolicy


username = input("Enter your SSH username: ")
password = getpass.getpass("Enter your SSH password: ")
switch_upgraded = []
switch_not_upgraded = []
switch_with_tacacs_issue = []
switch_not_reachable = []


with open('reachable_ip.txt',mode="r",encoding='utf8') as f:
    for line in f.readlines():
        try:
            ip = line.strip()
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko,AutoAddPolicy())
            ssh_client.connect(hostname=ip,username=username,password=password,look_for_key=False)
            print("Successfully connect to ", ip)
            remote_connection = ssh_client.invoke_shell(width=300)
            remote_connection.send('term len 0 \n')
            remote_connection.send('show version | b SW Version\n')
            time.sleep(0.5)
            output = remote_connection.recv(65535)
            #print(output.decode('ascii')
            ios_version = re.search(r'\d{2}.\d\(\d{1,2}\)\w{2,4}',output)
            if ios_version.group() == '12.2(55)SE12':
                switch_upgraded.append(ip)
            elif ios_version.group() == '15.2(2)E8':
                switch_upgraded.append(ip)
            elif ios_version.group() == '15.0(2)SE11':
                switch_upgraded.append(ip)
            else:
                switch_not_upgraded.append(ip)
        except paramiko.AuthenticationException:
            print("TACACS ISE is not working for" + ip + ".")
            switch_with_tacacs_issue.append(ip)

        except socket.error:
            print(ip + "is not reachable.")
            switch_not_reachable.append(ip)

            ssh_client.close


print("\nTACAS is not working for below switches: ")
for i in switch_with_tacacs_issue:
    print(i)

print("\nBelow switches are not reachable: ")
for i in switch_not_reachable:
    print(i)

print('\nBelow switches IOS version are up-to-date: ')
for i in switch_upgraded:
    print(i)

print('\nBelow switches IOS version are not updated yet: ')
for i in switch_not_upgraded:
    print(i)
