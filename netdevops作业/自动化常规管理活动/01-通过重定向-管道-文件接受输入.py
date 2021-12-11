#通过重定向接收输入
import sys

class Readirection:
    def __init__(self,in_obj,out_obj):
        self.input = in_obj
        self.ouput = out_obj
    
    
    def read_line(self):
        res = self.input.readline()
        self.ouput.write(res)
        return res

if __name__ == "__main__":
    a = input("Enter a string: ")
    b = input("Enter another string: ")
    if  not sys.stdin.isatty():
        sys.stdin = Readirection(in_obj=sys.stdin,out_obj=sys.stdout)
        print(sys.stdin.read_line())
    #print("Enter string are: ",repr(a),'and',repr(b))


#sys.stdin.isatty() 判断是否有输入
#测试代码
'''import sys
print(sys.stdin.isatty())

python3 script.py #返回Ture

echo 111 | python3 script.py #返回False
'''


#通过管道输入
import sys
for n in sys.stdin:
    print(int(n.strip() // 2))


# echo 15 | python3 srcipt.py



#通过文件接收输入
# sample.txt:
# Hello world
# Hello Python

i = open('sample.txt','r')
o = open('osample_output.txt','w')

a = i.read()
o.write(a)


#代码执行
#python3 srcipt.py
#查看sample_output.txt文件内容