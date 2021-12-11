#coding=utf-8
#version:python3.7
#Tools:Pycharm 2017.3.2
__date__ = '2019/5/4 22:05'
__author__ = 'ZhaoXiaoDong'

# def set_func(func):
#     def call_func(*args,**kwargs):
#         print("这是权限验证")
#         func(*args,**kwargs)
#     return call_func
#
# @set_func  #开启装饰后func()没有变量接受，返回值为NONE
# def test1(num,*args, **kwargs):
#     print("---test1---%d" % num)
#     print("---test1---" ,args)
#     print("---test1---",kwargs)
#     return "ok" #不使用装饰器打印的返回值
#
# ret = test1(100)
# print(ret)


def set_func(func):
    def call_func(*args,**kwargs):
        print("这是权限验证")
        return func(*args,**kwargs)
    return call_func

@set_func  #开启装饰后func()没有变量接受，返回值为NONE,通过 return func(*args,**kwargs)解决
def test1(num,*args, **kwargs):
    print("---test1---%d" % num)
    print("---test1---" ,args)
    print("---test1---",kwargs)
    return "ok"

ret = test1(100)
print(ret)
