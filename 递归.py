def test1(facrot):
    def test2(number):
        return number * facrot
    return test2

double = test1(3)
print(double(5))

# 案例一
