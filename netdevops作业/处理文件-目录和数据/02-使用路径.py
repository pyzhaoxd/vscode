import os

#返回绝对路径，包含文件
a = os.path.abspath('a.txt')
print('绝对路径输入#################',a)


#返回路径，不包含文件
b = os.path.dirname(r'C:\Users\64530\PycharmProjects\untitled3\python复习\netdevops作业\处理文件-目录和数据\a.txt')
print('返回路径不包含文件名：#################',b)



#返回文件不包含路径
c = os.path.basename(r'C:\Users\64530\PycharmProjects\untitled3\python复习\netdevops作业\处理文件-目录和数据\a.txt')
print('返回文件名：#################',c)


#判断文件是否存在，返回BOOL值，True False
d = os.path.exists('a.txt')
print('判断当前目录文件是否存在返回结果：#################',d)


#返回文件大小
e = os.path.getsize('a.txt')
print('返回文件大小，单位是字节：#################',e)


#返回文件创建时
# os.path.getatime
# os.path.getctime
# os.path.getmtime
f = os.path.getctime('a.txt')
print('返回文件创建时间：#################',f)


#检查输入是否是一个文件,BOOL
# os.path.isfile 
# os.path.isabs
# os.path.isdir
# os.path.islink
# os.path.ismount
g = os.path.isfile('a.txt')
print('检查输入是否是一个文件：#################',g)


#执行shell命令
print(list(os.popen('dir')))
#os.system('ls')


#路径拼接
#os.path.join()
Path1 = '/home'
Path2 = '/develop'
Path3 = '/code'

Path10 = Path1 + Path2 + Path3
Path20 = os.path.join(Path10)
print ('Path10 = ',Path10)
print ('Path20 = ',Path20)

#os.path.split()
# 语法：os.path.split('PATH')
# 参数说明：
#     PATH指一个文件的全路径作为参数：
#     如果给出的是一个目录和文件名，则输出路径和文件名
#     如果给出的是一个目录名，则输出路径和为空文件名

h = os.path.split(r'C:\Users\64530\PycharmProjects\untitled3\python复习\netdevops作业\处理文件-目录和数据\a.txt')
print(h)

j  = os.path.split(r'C:\Users\64530\PycharmProjects\untitled3\python复习\netdevops作业\处理文件-目录和数据\\')
print(j)


#分隔符以空格 ，分割2次,并取序列为1的项
sentence="All good things come to those who wait."
print("分隔符以空格 ，分割2次,并取序列为1的项: ",sentence.split(' ',2)[1])
