
//bool符号[ == != => <= ]
var aVar = 10
aVar == 5  // false
aVar == 10 // true
aVar != 5  // true
aVar != 10 // false


//布尔值可以和 &&（AND）和 ||（OR）操作符结合
//因为&&的优先级比||高（&& 对应逻辑乘法，|| 对应逻辑加法，乘法比加法优先级要高），所以下面的布尔表达式可以不加小括号

if 'a' <= c && c <= 'z' ||'A' <= c && c <= 'Z' ||'0' <= c && c <= '9'


//如果需要经常做类似的转换，可以将转换的代码封装成一个函数，如下所示
// 如果b为真，btoi返回1；如果为假，btoi返回0

package main
func btoi(b bool) int {
    if b {
        return 1
    }
    return 0

	
}
//代码解读btoi是函数体，(b bool)是函数参数b和参数的类型 int是参数的返回类型 {}里面的是函数体

// Go语言中不允许将整型强制转换为布尔型，代码如下：
var n bool
fmt.Println(int(n) * 2)
