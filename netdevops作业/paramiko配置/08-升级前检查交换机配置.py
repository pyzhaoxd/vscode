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
            remote_connection.send('show inventory | in PID: WS\n')
            time.sleep(0.5)
            remote_connection.send('show flash: | in c2960\n')
            time.sleep(0.5)
            remote_connection.send('show boot | in BOOT path\n')
            time.sleep(0.5)
            output = remote_connection.recv(65535)
            #print(output.decode('ascii'))
            remote_connection.send('write mem\n')
            switch_mode = re.search(r'WS-C2960\w?-\w{4,5}-L',output)
            ios_version = re.search(r'c2960\w?-\w{8,10}\d?-mz.\d{3}-\d{1,2}.\w{2,4}(.bin)?',output)
            boot_system = re.search(r'flash:.+mz.\d{3}-\d{1,2}\.\w{2,4}\.bin',output)
            if switch_mode.group() == "WS-C2960-24PC-L" and ios_version.group() == "c2960-lanbasek9-mz.122-55.SE12.bin" and boot_system.group() == "flash:/c2960-lanbasek9-mz.122-55.SE12.bin":
                switch_upgraded.append(ip)
            elif switch_mode.group() == "WS-C2960S-F24PS-L" and ios_version.group() == "c2960s-universalk9-mz.150-2.SE11.bin" and boot_system.group() == "flash:/c2960s-universalk9-mz.150-2.SE11.bin":
                switch_upgraded.append(ip)
            elif switch_mode.group() == "WS-C2960X-24PS-L" and ios_version.group() == "c2960x-universalk9-mz.152-2.e8.bin" and boot_system.group() == "flash:/c2960x-universalk9-mz.152-2.e8.bin":
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

    