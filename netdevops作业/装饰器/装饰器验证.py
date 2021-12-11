#coding=utf-8
#version:python3.7
#Tools:Pycharm 2017.3.2
__date__ = '2019/5/1 15:47'
__author__ = 'ZhaoXiaoDong'



# 代码改造不使用装饰器
# def set_func(func):
#     def call_func():
#         print("这是权限验证")
#         func()
#     return call_func
#
#
# def test1():
#     print("---test1---")
#
# ret = set_func(test1)
# ret()



# 以上代码调用ret()可以实现，但是用户原有项目都调用的是test()，难道让用户去修改
# 调用方式么，显然是不可取的

# 以下代码为装饰的功能及方案

def set_func(func):
    def call_func():
        print("这是权限验证")
        func()
    return call_func


def test1():
    print("---test1---")

test1 = set_func(test1)
test1()


#能够在原来功能代码不修改的时候，进行功能添加，注意是先执行装饰器里面的代码
# def set_func(func):
#     def call_func():
#         print("这是权限验证")
#         func()
#     return call_func
#
# @set_func  #等价于test1 = set_func(test1)
# def test1():
#     print("---test1---")
#
# test1()
