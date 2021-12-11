#通过 pythonping 扫描不通网络中的存活主机并写入保存到指定reachable_ip.txt文件中 172.16.0.x -- 172.16.4.x 两层for嵌套解决
#通过生成的reachable_ip.txt文件，读取文件的地址信息以此登录设备进行show ip int brief | in up 查看哪些端口是up的
#在配合正则表达式（re）模块，在回显内容匹配用户物理端口号Gix/x/x 统计总数 得出每个交换机得物理端口UP数目
#注意show ip int brief | in up中会出现多种接口,比如Ten级联口，interface vlan loopback ,所以在正则表达式中要注意Gix/x/x关键字

#os subprocess pyping  ping 如果目标可达返回0，如果不可达，返回非0
#pythonping 默认对目标ip ping4次，当目标可达返回的是Reply from 110.242.68.4, 9 bytes in 12.03ms 如果不可达返回得是Request timed out

from pythonping import ping
import os
import time


#保持每次运行脚本都及时存储最新得状态，如果当前脚本目录有之前得文件将删除，当脚本重新运行时将自动创建文件
# if os.path.exists("reachable_ip.txt"):
#     os.remove("reachable_ip.txt")


# third_octed = range(5)
# last_octet = range(1,255)


# for ip3 in third_octed:
#     for ip4 in last_octet:
#         ip = "172.16." + str(ip3) + "." + str(ip4)
#         ping_result = ping(ip)
#         with open('reachable_ip.txt',mode='a',encoding='utf8') as f:
#             if 'Reply' in str(ping_result):
#                 f.write(ip + "\n")
#                 print(ip + 'is reachable.')
#             else:
#                 print(ip + " " 'is not reachable.')




ip = "www.baidu.com"
ping_result = ping(ip)
print(type(ping_result)) #返回<class 'pythonping.executor.ResponseList'> 必须将str()才能使用成员运算符in来做判断，反正if 'Reply in str(ping_result):'永远返回False，目标永远不可达
with open('reachable_ip.txt',mode='a',encoding='utf8') as f:
    if 'Reply' in str(ping_result):
        f.write(ip + "\n")
        print(ip +" ",'is reachable'+ time.asctime())
        
    else:
        print(ip + " ",'is not reachable.')


