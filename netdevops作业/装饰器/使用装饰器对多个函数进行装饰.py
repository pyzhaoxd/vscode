#coding=utf-8
#version:python3.7
#Tools:Pycharm 2017.3.2
__date__ = '2019/5/1 22:52'
__author__ = 'ZhaoXiaoDong'

def set_func(func):
    print("开始装饰了")  #用来验证在没有调用函数前装饰器已经开始了
    def call_func(a):
        print("这是权限验证")
        func(a)
    return call_func

@set_func  #等价于test1 = set_func(test1)
def test1(num):
    print("---test1---%d" % num)
@set_func
def test2(num):
    print("---test2---%d" % num)

test1(100)
test2(200)
