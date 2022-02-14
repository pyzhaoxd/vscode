// 形式参数
// 在定义函数时函数名后面括号中的变量叫做形式参数（简称形参）。形式参数只在函数调用时才会生效，函数调用结束后就会被销毁，在函数未被调用时，函数的形参并不占用实际的存储单元，也没有实际值。

// 形式参数会作为函数的局部变量来使用。


package main
import (
    "fmt"
)
//全局变量 a
var a int = 13
func main() {
    //局部变量 a 和 b
    var a int = 3
    var b int = 4
    fmt.Printf("main() 函数中 a = %d\n", a)
    fmt.Printf("main() 函数中 b = %d\n", b)
    c := sum(a, b)
    fmt.Printf("main() 函数中 c = %d\n", c)
}
func sum(a, b int) (int){
    fmt.Printf("sum() 函数中 a = %d\n", a)
    fmt.Printf("sum() 函数中 b = %d\n", b)
    num := a + b
	fmt.Println("num",num)
    return num
}

