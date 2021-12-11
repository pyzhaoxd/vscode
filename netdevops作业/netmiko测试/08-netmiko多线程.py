import threading
import time

# def say_affter(what,delay):
#     print(what)
#     time.sleep(delay)
#     print(what)


# t = threading.Thread(target = say_affter,args=('hello',3))
# t.start()

# 以上代码虽然启动了多线程，也感受不到它和单线程的区别

#测试二，加时间


# def say_affter(what,delay):
#     print(what)
#     time.sleep(delay)
#     print(what)


# t = threading.Thread(target = say_affter,args=('hello',3))
# print(f"程序于{time.strftime('%X')}开始运行")
# t.start()
# print(f"程序于{time.strftime('%X')}结束运行")



#测试三正确的捕捉函数开始和结束时间,需要使用thrading模块的join()方法
#t.join()方法的作用是强制阻塞调用它的线程，知道该线程运行完毕或者终止（类似单线程的同步）
# def say_affter(what,delay):
#     print(what)
#     time.sleep(delay)
#     print(what)


# t = threading.Thread(target = say_affter,args=('hello',3))
# print(f"程序于{time.strftime('%X')}开始运行")
# t.start()
# t.join()
# print(f"程序于{time.strftime('%X')}结束运行")


#测试四，创建多个用户线程并运行

def say_affter(what,delay):
    print(what)
    time.sleep(delay)
    print(what)
print(f"程序于{time.strftime('%X')}开始运行\n")
threads = []

for i in range(1,6):
    t = threading.Thread(target = say_affter,name="线程" + str(i),args=('hello',3))
    print(t.name + '开始执行')
    t.start()
    #t.join() #用于测试单线程执行时间15s
    threads.append(t)
    

for i in threads:
    i.join()
print(f"\n程序于{time.strftime('%X')}结束运行")




#以上代码执行时间总共3秒，如果以单线程来执行5次say_affter(what,delay)函数，需要花费3 x 5 = 15s 



#多线程在netmiko中的应用测试


# import threading
# from queue import Queue
# import time
# from netmiko import ConnectHandler

# threads = []

# def ssh_session(ip,ouput_q):
#     commands = ["line vty 5 15","login loacl","exit"]
#     SW = {'device_type':'cisco_ios','ip':ip,'username':'cisco','password':'cisco'}
#     ssh_session = ConnectHandler(**SW)
#     output = ssh_session.send_config_set(commands)
#     print(output)
# print(f"程序于{time.strftime('%X')}开始运行\n")


# with open('ip_list.txt',mode='r',encoding='utf8') as f:
#     for ips in f.readlines():
#         t = threading.Thread(target=ssh_session,args=(ips.strip(),Queue()))
#         t.start()
#         threads.append(t)


# for i in threads:
#     i.join()

# print(f"\n程序于{time.strftime('%X')}结束运行")
