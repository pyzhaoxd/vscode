import telnetlib

host = "192.168.1.1"
user = "cisco"
pasword = "cisco"

# 输入的值和命令必要加b 字节流，写入encode(acsii) 输出需要decode('acsii')
tn = telentlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('acsii') + b"\n")


tn.write(b"config t\n")
tn.write(b"intface loopback 1\n")
tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"write\n")


#打印输出结果
print(tn.read_all().decode.('ascii'))