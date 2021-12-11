
import paramiko
import time
import re
from datetime import datetime
import socket
import getpass

from paramiko.client import AutoAddPolicy


username = input("Enter your SSH username: ")
password = getpass.getpass("Enter your SSH password: ")
now = datetime.now()
date = "%s-%s-%s-%s:%s:%s" %(now.year, now.month, now.day,now.hour, now.minute, now.second)
#print(date)

switch_with_tacacs_issue = []
switch_not_reachable = []
total_number_of_up_port = 0 
with open('reachable_ip.txt',mode="r",encoding='utf8') as f:
    number_of_switch = len(f.readlines())
    total_number_of_up_ports = number_of_switch * 48
    for line in f.readlines():
        try:
            ip = line.strip()
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko,AutoAddPolicy())
            ssh_client.connect(hostname=ip,username=username,password=password,look_for_key=False)
            print("Successfully connect to ", ip)
            remote_connection = ssh_client.invoke_shell()
            remote_connection.send('term len 0 \n')
            remote_connection.send('show ip int brief | in up\n')
            time.sleep(1)
            output = remote_connection.recv(65535)
            #print(output.decode('ascii'))

            search_up_port = re.findall(r'GigabitEthernet',output)
            number_of_up_port = len(search_up_port)
            print(ip + " has " + str(number_of_switch) + "ports up.")
            total_number_of_up_port += number_of_switch

        except paramiko.AuthenticationException:
            print("TACACS ISE is not working for" + ip + ".")
            switch_with_tacacs_issue.append(ip)

        except socket.error:
            print(ip + "is not reachable.")
            switch_not_reachable.append(ip)
print("\n")
print("There are totally" + str(total_number_of_up_port) + "ports available in the network.")
print("Port up rate is %.2f%%" %(total_number_of_up_port / float(total_number_of_up_ports) * 100)) 


print("\nTACAS is not working for below switches: ")
for i in switch_with_tacacs_issue:
    print(i)

print("\nBelow switches are not reachable: ")
for i in switch_not_reachable:
    print(i)

with open(date + ".txt",mode="a+",encoding="utf8") as f:
    f.write('As of ' + date,"\n")
    f.write("\n\nThere are totally" + str(total_number_of_up_ports) + "ports available in the network.")
    f.write("\nPort up rate is %.2f%%" %(total_number_of_up_port / float(total_number_of_up_ports) * 100))
    f.write("\n***********************************************************************************\n\n")


    


