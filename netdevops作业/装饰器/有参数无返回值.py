#coding=utf-8
#version:python3.7
#Tools:Pycharm 2017.3.2
__date__ = '2019/5/1 22:06'
__author__ = 'ZhaoXiaoDong'


def set_func(func):
    def call_func(a):
        print("这是权限验证")
        func(a)
    return call_func

@set_func  #等价于test1 = set_func(test1)

def test1(num):  #此处说的是函数test不许要传递实参，并且函数本身没有返回值
    print("---test1---%d" % num)

test1(100)