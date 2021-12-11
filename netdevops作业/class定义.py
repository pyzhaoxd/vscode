
#random随机生成功能
from random import choice
x = choice(["hello",['1','2','3','4','5']])
print(x.count('5'))

#创建一个类
class Person(object):

    def set_name(self,name):
        self.name = name 

    def get_name(self):
        return self.name 

    def greet(self):
        return("hello world! I'm {}.".format(self.name))
        
foo = Person()
bar = Person()
foo.set_name('ok1')
bar.set_name('ok2')
print(foo.greet())
print(bar.greet())

#操作对象本身
print(foo.name)
bar.name = "1234"
print(bar.greet())
print(foo.get_name())


#属性，函数和方法

#如果将属性关联到一个普通的函数，那么这样就没有特殊的self参数了
class Class:
    def method(self):
        return("I have a self")
instance = Class()
print(instance.method())


class Bird:
    song = 'Squaawk!'

    def sing(self):
        return(self.song)

bar = Bird()
print(bar.song)
print(bar.sing())


#让方法和属性成为私有的（不能从外部直接访问--但是也可以通过手段达到直接访问的目的）
class Server:

    def __tomcat(self):
        return("this is tomcat")

    def accesstomcat(self):
        print("the secret message is:")
        return(self.__tomcat())

ser = Server()
#print(ser.__tomcat) 不能直接访问属性，Server类么有这个属性
print(ser.accesstomcat())