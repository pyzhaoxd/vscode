//Go语言的基本类型有：
bool
string
int、int8、int16、int32、int64
uint、uint8、uint16、uint32、uint64、uintptr
byte // uint8 的别名
rune // int32 的别名 代表一个 Unicode 码
float32、float64
complex64、complex128// 声明变量的一般形式是使用 var 关键字

=============================================================================================================
// 其中，var 是声明变量的关键字，name 是变量名，type 是变量的类型。
var name type
//指定变量类型，如果没有初始化，则变量默认为零值。
//零值就是变量没有做初始化时系统默认设置的值
第一种，指定变量类型，如果没有初始化，则变量默认为零值。
package main
import "fmt"
func main() {

    // 声明一个变量并初始化
    var a = "RUNOOB"
    fmt.Println(a)

    // 没有初始化就为零值
    var b int
    fmt.Println(b)

    // bool 零值为 false
    var c bool
    fmt.Println(c)
}
===========================================================================================================
//数值类型（包括complex64/128）为 0
//布尔类型为 false
//字符串为 ""（空字符串）
//以下几种类型为 nil：

var a *int
var a []int
var a map[string] int
var a chan int
var a func(string) int
var a error // error 是接口

package main
import "fmt"
func main() {
    var i int
    var f float64
    var b bool
    var s string
    fmt.Printf("%v %v %v %q\n", i, f, b, s)
}
=============================================================================================================
//多变量声明
var a,b *int

//测试代码
package main

import "fmt"

func main(){
	var a string = "Zhaoxd"
	fmt.Println(a)

	var b,c int = 1,2
	fmt.Println(b,c)
}

第二种，根据值自行判定变量类型
var v_name = value
package main
import "fmt"
func main() {
    var d = true
    fmt.Println(d)
}


第三种，如果变量已经使用 var 声明过了，再使用 := 声明变量，就产生编译错误，格式：
package main
import "fmt"
func main() {
    f := "Runoob" // var f string = "Runoob"

    fmt.Println(f)
}
=============================================================================================================
// 变量初始化的标准格式
var 变量名 类型 = 表达式
var hp int = 100
=============================================================================================================
//简短格式
//除 var 关键字外，还可使用更加简短的变量定义和初始化语法。
名字 := 表达式
// 短变量声明并初始化
hp := 100
=============================================================================================================
//需要注意的是，简短模式（short variable declaration）有以下限制： n  
//定义变量，同时显式初始化。
//不能提供数据类型。
//只能用在函数内部。
//和 var 形式声明语句一样，简短变量声明语句也可以用来声明和初始化一组变量：
i, j := 0, 1

//下面通过一段代码来演示简短格式变量声明的基本样式。
package mian 

import "fmt"

func main() {
   x :=100
   a,s :=1,"abc"
   fmt.Println(x)
   fmt.Println(a,s)
}
//因为简洁和灵活的特点，简短变量声明被广泛用于大部分的局部变量的声明和初始化。
//var 形式的声明语句往往是用于需要显式指定变量类型地方，或者因为变量稍后会被重新赋值而初始值无关紧要的地方。
=============================================================================================================
// 编译器推导类型的格式
var hp = 100
var attack = 40
var defence = 20
var damageRate float32 = 0.17
var damage = float32(attack-defence) * damageRate
fmt.Println(damage)
当一个变量被声明之后，系统自动赋予它该类型的零值：int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil 等。所有的内存在 Go 中都是经过初始化的。
变量的命名规则遵循骆驼命名法，即首个单词小写，每个新单词的首字母大写，例如：numShips 和 startDate 。
变量的声明有几种形式，通过下面几节进行整理归纳。
==============================================================================================================
//批量格式-多变量声明
//觉得每行都用 var 声明变量比较烦琐？没关系，还有一种为懒人提供的定义变量的方法
//这种因式分解关键字的写法一般用于声明全局变量
var (
    a int
    b string
    c []float32
    d func() bool
    e struct {
        x int
    }
)

package main
var x, y int //非全局变量
var (  // 这种因式分解关键字的写法一般用于声明全局变量
    a int
    b bool
)
var c, d int = 1, 2
var e, f = 123, "hello"

//这种不带声明格式的只能在函数体中出现
//g, h := 123, "hello"
func main(){
    g, h := 123, "hello"
    println(x, y, a, b, c, d, e, f, g, h)
}
===============================================================================================================
//短变量声明的形式在开发中的例子较多，比如：
net.Dial 提供按指定协议和地址发起网络连接，这个函数有两个返回值，一个是连接对象（conn），一个是错误对象（err）。如果是标准格式将会变成：
var conn net.Conn
var err error
conn, err = net.Dial("tcp", "127.0.0.1:8080")


注意：在多个短变量声明和赋值中，至少有一个新声明的变量出现在左值中，即便其他变量名可能是重复声明的，编译器也不会报错，代码如下：
纯文本复制
conn, err := net.Dial("tcp", "127.0.0.1:8080")
conn2, err := net.Dial("tcp", "127.0.0.1:8080")

//变量的生命周期
/*
变量的生命周期指的是在程序运行期间变量有效存在的时间间隔。
变量的生命周期与变量的作用域有着不可分割的联系：
全局变量：它的生命周期和整个程序的运行周期是一致的；
局部变量：它的生命周期则是动态的，从创建这个变量的声明语句开始，到这个变量不再被引用为止；
形式参数和函数返回值：它们都属于局部变量，在函数被调用的时候创建，函数调用结束后被销毁
*/


注意事项
//如果你声明了一个局部变量却没有在相同的代码块中使用它，同样会得到编译错误，例如下面这个例子当中的变量 a：
//尝试编译这段代码将得到错误 a declared and not used。
package main
import "fmt"
func main() {
   var a string = "abc"
   fmt.Println("hello, world")
}

//但是全局变量是允许声明但不使用的。 同一类型的多个变量可以声明在同一行，如：
var a, b, c int
var a, b int
var c string
a, b, c = 5, 7, "abc"
//上面这行假设了变量 a，b 和 c 都已经被声明，否则的话应该这样使用：
a, b, c := 5, 7, "abc"
如果你想要交换两个变量的值，则可以简单地使用 a, b = b, a，两个变量的类型必须是相同。
package main
import (
    "fmt"
)
func main (){
	var a int = 100
	var b int = 200
	b, a = a, b
	fmt.Println(a, b)			
}

匿名变量不占用内存空间，不会分配内存。匿名变量与匿名变量之间也不会因为多次声明而无法使用。
// func 函数名 (参数列表) (返回值列表){
//     函数体
// }
//Go语言匿名变量
func GetData() (int,int) {
    return 100, 200
}
func main(){
    a, _ := GetData()
    _, b := GetData()
    fmt.Println(a, b)
}

// 第 28 行只需要获取第一个返回值，所以将第二个返回值的变量设为下画线（匿名变量）。
// 第 29 行将第一个返回值的变量设为匿名变量。
//匿名变量不占用内存空间，不会分配内存。匿名变量与匿名变量之间也不会因为多次声明而无法使用。