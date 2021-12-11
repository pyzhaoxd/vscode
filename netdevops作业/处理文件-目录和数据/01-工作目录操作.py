import os

#获取当前目录
ospath = os.getcwd()
print(ospath)


#更改目录
# os.chdir(r'C:\Users\64530')
# print(os.getcwd())



#列出文件和目录
ls = os.listdir()
print(ls)


#重命名目录或者文件
# rn = os.rename('a.txt','b.txt')

# rn1 = os.rename('work','work1')


#退出代码
print(os.error(exit,1))


#复制，移动，重命名，删除目录或者文件


#将a文件的内容复制到b文件，如果B文件不存在就自动创建
import shutil
shutil.copy('a.txt','b.txt')


#移动文件
shutil.move(r'C:\Users\64530\PycharmProjects\untitled3\python复习\netdevops作业\处理文件-目录和数据\b.txt', r'C:\Users\64530\\')


#重命名文件
shutil.move('a.txt','c.txt')
os.rename('a.txt','b.txt')


#删除文件
os.remove('a.txt')

#删除目录
os.removedirs('work')
os.rmdir('work')







