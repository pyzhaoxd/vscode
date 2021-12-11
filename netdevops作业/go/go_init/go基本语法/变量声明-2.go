// 声明变量的一般形式是使用 var 关键字

var name type
// 其中，var 是声明变量的关键字，name 是变量名，type 是变量的类型。


例子：var a,b *int

Go语言的基本类型有：
bool
string
int、int8、int16、int32、int64
uint、uint8、uint16、uint32、uint64、uintptr
byte // uint8 的别名
rune // int32 的别名 代表一个 Unicode 码
float32、float64
complex64、complex128// 声明变量的一般形式是使用 var 关键字

var name type
// 其中，var 是声明变量的关键字，name 是变量名，type 是变量的类型。


例子：var a,b *int

Go语言的基本类型有：
bool
string
int、int8、int16、int32、int64
uint、uint8、uint16、uint32、uint64、uintptr
byte // uint8 的别名
rune // int32 的别名 代表一个 Unicode 码
float32、float64
complex64、complex128
当一个变量被声明之后，系统自动赋予它该类型的零值：int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil 等。所有的内存在 Go 中都是经过初始化的。
变量的命名规则遵循骆驼命名法，即首个单词小写，每个新单词的首字母大写，例如：numShips 和 startDate 。
变量的声明有几种形式，通过下面几节进行整理归纳。

标准格式
Go语言的变量声明的标准格式为：
var 变量名 变量类型
变量声明以关键字 var 开头，后置变量类型，行尾无须分号。

批量格式
觉得每行都用 var 声明变量比较烦琐？没关系，还有一种为懒人提供的定义变量的方法


var (
    a int
    b string
    c []float32
    d func() bool
    e struct {
        x int
    }
)


简短格式
除 var 关键字外，还可使用更加简短的变量定义和初始化语法。
名字 := 表达式

需要注意的是，简短模式（short variable declaration）有以下限制： n  
定义变量，同时显式初始化。
不能提供数据类型。
只能用在函数内部。


和 var 形式声明语句一样，简短变量声明语句也可以用来声明和初始化一组变量：
i, j := 0, 1

下面通过一段代码来演示简短格式变量声明的基本样式。
package mian 

import "fmt"

func main() {
   x :=100
   a,s :=1,"abc"
   fmt.Println(x)
   fmt.Println(a,s)
}
因为简洁和灵活的特点，简短变量声明被广泛用于大部分的局部变量的声明和初始化。var 形式的声明语句往往是用于需要显式指定变量类型地方，或者因为变量稍后会被重新赋值而初始值无关紧要的地方。

