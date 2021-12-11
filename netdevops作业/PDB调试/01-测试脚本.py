class Student:
    def __init__(self,std):
        self.count = std

    def print_std(self):
        for i in range(self.count):
            print(i)
        return

if __name__ =="__main__":
    Student(5).print_std()


 #PDF调试方式一共有三种：
 # 第一中在解释中运行
 # 
 # >>> import script_name
 # >>> import pdf
 # >>> pdb.run('srcipt_name.Student(5).print_std()')
 # > 调试输出
 # （pdb）  输入continue 继续运行并输出调试信息 

 

 #第二种方式，在命令行中运行

 #python3 -m pdb srcipt_name.py  注意遇到pdb提示直接输入continue继续调试即可

 #第三种方式，在python脚本中使用
import pdb
class Student:
    def __init__(self,std):
        self.count = std

    def print_std(self):
        for i in range(self.count):
            pdb.set_trace()   #它是一个python函数，可以在任何位置进行调用
            print(i)
        return

if __name__ =="__main__":
    Student(5).print_std()



#调试基本程序崩溃的方法

class Student:
    def __init__(self,std):
        self.count = std

    def go(self):
        for i in range(self.count):
            print(i)
        return

if __name__ =="__main__":
    Student(5).go()


#调试命令
#python3 -m trace --trace srcipt_name.py

