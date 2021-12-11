# 程序名称arithmetic.py
def add_numbers(x,y):
    return x + y


def sub_numbers(x,y):
    return x - y

def mul_numbers(x,y):
    return x * y

def div_numbers(x,y):
    return (x / y)




#创建测试用例

import unittest
import arithmetic #导入脚本

#测试add_numbers函数
class Test_addition(unittest.TestCase):
    #测试整数
    def test_add_numbers_int(self):
        sum = arithmetic.add_numbers(50,50)
        self.assertEqual(sum, 100)

    #测试符点数
    def test_add_numbers_float(self):
        sum = arithmetic.add_numbers(50.55,78)
        self.assertEqual(sum,128.55)
    
    #测试字符串
    def test_add_numbers_string(self):
        sum = arithmetic.add_numbers('hello','python')
        self.assertEqual(sum,'hellopython')


if __name__ == "__main__":
    unittest.main()

# 在命令执行： python3 im unittest test_addition.py

#测试结果有三种：OK/FAILLED/ERROR

# #unittest模块常用的方法
# assertEqual()和assertNotEqua() 检查是否达到预期
# assertTrue()和assertFalse()检查一个表示式的布尔值
# asserRaises()检查是否触发的特定的异常
# setUp()和tearDown()定义之前和之后执行的指令