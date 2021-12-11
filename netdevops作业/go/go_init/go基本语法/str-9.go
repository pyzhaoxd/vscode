// 定义字符串
// 可以使用双引号""来定义字符串，字符串中可以使用转义字符来实现换行、缩进等效果，常用的转义字符包括：
// \n：换行符
// \r：回车符
// \t：tab 键
// \u 或 \U：Unicode 字符
// \\：反斜杠自身

// package main
// import (
//     "fmt"
// )
// func main() {
//     var str = "Hello\nWorld"
//     fmt.Println(str)
// 	fmt.Println(len(str))
// 	fmt.Println(str[0])
// 	fmt.Println(str[5-1])
// 	fmt.Println(str[len(str)-1])
// }

//一般的比较运算符（==、!=、<、<=、>=、>）是通过在内存中按字节比较来实现字符串比较的，因此比较的结果是字符串自然编码的顺序。
//字符串所占的字节长度可以通过函数 len() 来获取，例如 len(str)。

// 字符串的内容（纯字节）可以通过标准索引法来获取，在方括号[ ]内写入索引，索引从 0 开始计数：
// 字符串 str 的第 1 个字节：str[0]
// 第 i 个字节：str[i - 1]
// 最后 1 个字节：str[len(str)-1]

// 需要注意的是，这种转换方案只对纯 ASCII 码的字符串有效。
// 注意：获取字符串中某个字节的地址属于非法行为，例如 &str[i]。

// 字符串拼接符“+”
// 两个字符串 s1 和 s2 可以通过 s := s1 + s2 拼接在一起。将 s2 追加到 s1 尾部并生成一个新的字符串 s。

//str := "Beginning of the string " +"second part of the string"

// package main

// import "fmt"

// func main() {
// 	s := "hel" + "lo,"
// 	s += "world!"
// 	fmt.Println(s) //输出 “hello, world!”
// }

//定义多行字符串
//使用双引号书写字符串的方式是字符串常见表达方式之一，被称为字符串字面量（string literal），这种双引号字面量不能跨行，如果想要在源码中嵌入一个多行字符串时，就必须使用`反引号，代码如下：
//在这种方式下，反引号间换行将被作为字符串中的换行，但是所有的转义字符均无效，文本将会原样输出。
// package main

// import (
// 	"fmt"
// 	"unicode"
// )

// func main() {
// 	const str = `第一行
// 	第二行
// 	第三行
// 	\r\n`

// 	fmt.Println(str)

// }


