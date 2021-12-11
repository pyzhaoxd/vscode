// package main
// import (
//     "fmt"
// )
// func main() {
//     var cat int = 1
//     var str string = "banana"
//     fmt.Printf("%p %p", &cat, &str)
// }

//Go语言允许你控制特定集合的数据结构、分配的数量以及内存访问模式，这对于构建运行良好的系统是非常重要的
// 第 6 行，声明整型变量 cat。
// 第 7 行，声明字符串变量 str。
// 第 8 行，使用 fmt.Printf 的动词%p打印 cat 和 str 变量的内存地址，指针的值是带有0x十六进制前缀的一组数据。

//提示：变量、指针和地址三者的关系是，每个变量都拥有地址，指针的值就是地址。

//从指针获取指针指向的值


//当使用&操作符对普通变量进行取地址操作并得到变量的指针后，可以对指针使用*操作符，也就是指针取值，代码如下。

// 取地址操作符&和取值操作符*是一对互补操作符，&取出地址，*根据地址取出地址指向的值。

// 变量、指针地址、指针变量、取地址、取值的相互关系和特性如下：
// 对变量进行取地址操作使用&操作符，可以获得这个变量的指针变量。
// 指针变量的值是指针地址。
// 对指针变量进行取值操作使用*操作符，可以获得指针变量指向的原变量的值。
// package main
// import (
//     "fmt"
// )
// func main() {
//     // 准备一个字符串类型
//     var house = "Malibu Point 10880, 90265"
//     // 对字符串取地址, ptr类型为*string
//     ptr := &house
//     // 打印ptr的类型
//     fmt.Printf("ptr type: %T\n", ptr)
//     // 打印ptr的指针地址
//     fmt.Printf("address: %p\n", ptr)
//     // 对指针进行取值操作
//     value := *ptr
//     // 取值后的类型
//     fmt.Printf("value type: %T\n", value)
//     // 指针取值后就是指向变量的值
//     fmt.Printf("value: %s\n", value)
// }

// 使用指针修改值
// 通过指针不仅可以取值，也可以修改值


// package main
// import "fmt"
// // 交换函数
// func swap(a, b *int) {
//     // 取a指针的值, 赋给临时变量t
//     t := *a
//     // 取b指针的值, 赋给a指针指向的变量
//     *a = *b
//     // 将a指针的值赋给b指针指向的变量
//     *b = t
// }
// func main() {
// // 准备两个变量, 赋值1和2
//     x, y := 1, 2
//     // 交换变量值
//     swap(&x, &y)
//     // 输出变量值
//     fmt.Println(x, y)
// }

//*操作符作为右值时，意义是取指针的值，作为左值时，也就是放在赋值操作符的左边时，表示 a 指针指向的变量。其实归纳起来，*操作符的根本意义就是操作指针指向的变量。当操作在右值时，就是取指向变量的值，当操作在左值时，就是将值设置给指向的变量


//如果在 swap() 函数中交换操作的是指针值，会发生什么情况？可以参考下面代码

// package main
// import "fmt"
// func swap(a, b *int) {
//     b, a = a, b
// }
// func main() {
//     x, y := 1, 2
//     swap(&x, &y)
//     fmt.Println(x, y)
// }

//运行结果：
//1 2
//结果表明，交换是不成功的。上面代码中的 swap() 函数交换的是 a 和 b 的地址，在交换完毕后，a 和 b 的变量值确实被交换。但和 a、b 关联的两个变量并没有实际关联。这就像写有两座房子的卡片放在桌上一字摊开，交换两座房子的卡片后并不会对两座房子有任何影响。


// package main

// // 导入系统包
// import (
//     "flag"
//     "fmt"
// )
// // 定义命令行参数
// var mode = flag.String("mode", "", "process mode")
// func main() {
//     // 解析命令行参数
//     flag.Parse()

//     // 输出命令行参数
//     fmt.Println(*mode)
// }


// 将这段代码命名为 main.go，然后使用如下命令行运行：
// go run main.go --mode=fast

// 命令行输出结果如下：
// fast

// 代码说明如下：
// 第 10 行，通过 flag.String，定义一个 mode 变量，这个变量的类型是 *string。后面 3 个参数分别如下：
// 参数名称：在命令行输入参数时，使用这个名称。
// 参数值的默认值：与 flag 所使用的函数创建变量类型对应，String 对应字符串、Int 对应整型、Bool 对应布尔型等。
// 参数说明：使用 -help 时，会出现在说明中。
// 第 15 行，解析命令行参数，并将结果写入到变量 mode 中。
// 第 18 行，打印 mode 指针所指向的变量。





//创建指针的另一种方法——new() 函数

package main

import "fmt"

func main() {
	str := new(string)
	*str = "go lanager"
	fmt.Println(*str)
}