def test1(facrot):
    def test2(number):
        return number * facrot
    return test2

double = test1(3)
print(double(5))

# 案例一
def fa(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

print(fa(5))

#案例二：
def fa2(n):
    if n == 1:
        return n
    else:
        return n * fa2(n-1)

def power(x,n):
    result = 1
    for i in range(n):
        result *= x
    return result

#等同于
print(list(map(str,range(10))))
print([str(i) for i in range(10)]) 


#等同于
def func(x):
    return x.isalnum()

seq  = ["foo","x41","?1","****"]
print(list(filter(func,seq)))

print([x for x in seq if x.isalnum()])


#lambda表达式
print(list(filter(lambda x: x.isalnum(),seq)))

number = [1,2,3,4]
from functools import reduce
print(reduce(lambda x,y: x+y, number))

print(sum(number))
