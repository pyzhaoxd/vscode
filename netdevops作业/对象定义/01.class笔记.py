class Stu:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __len__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self) -> str:
        pass
    
    def __int__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def stu_list(self): #面向对象封装
        if self.name == 'zhaoxd':
            print('input write ok')
        elif self.age == int(18):
            print("input write ok")
        else:
            print("input write error")


# def main():
#     a = Stu()



# if __name__ == "__main__":
#     main()



#继承

class jsj(Stu):
    pass

b = jsj()
print(b.name)


#继承重写

class jsj1(Stu):

    #重写__init__
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


#多态
c =jsj1()
print(c.num2)

d = jsj1()
print(d.num2)