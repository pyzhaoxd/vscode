// 语法

// Go 语言的 For 循环有 3 种形式，只有其中的一种使用分号。

// 和 C 语言的 for 一样：

// for init; condition; post { }

// 和 C 的 while 一样：

// for condition { }

// 和 C 的 for(;;) 一样：

// for { }

//     init： 一般为赋值表达式，给控制变量赋初值；
//     condition： 关系表达式或逻辑表达式，循环控制条件；
//     post： 一般为赋值表达式，给控制变量增量或减量。

// for语句执行过程如下：

//     1、先对表达式 1 赋初值；

//     2、判别赋值表达式 init 是否满足给定条件，若其值为真，满足循环条件，则执行循环体内语句，然后执行 post，进入第二次循环，再判别 condition；否则判断 condition 的值为假，不满足条件，就终止for循环，执行循环体外语句。

// for 循环的 range 格式可以对 slice、map、数组、字符串等进行迭代循环。格式如下：

// for key, value := range oldMap {
//     newMap[key] = value
// }


// package main

// import "fmt"

// func main() {
// 	sum := 0
// 	for i := 0; i < 10; i++{
// 		sum += i
// 	}
// 	fmt.Println(sum)
// }

// init 和 post 参数是可选的，我们可以直接省略它，类似 While 语句。
// 以下实例在 sum 小于 10 的时候计算 sum 自相加后的值：

// package main

// import "fmt"

// func main() {
//         sum := 1
//         for ; sum <= 10; {
//                 sum += sum
//         }
//         fmt.Println(sum)

//         // 这样写也可以，更像 While 语句形式
//         for sum <= 10{
//                 sum += sum
//         }
//         fmt.Println(sum)
// }

// 无限循环:
// package main

// import "fmt"

// func main() {
//     sum := 0
//     for {
//         sum++ // 无限循环下去
//     }
//     fmt.Println(sum) //无法输出
// }

// For-each range 循环
// 这种格式的循环可以对字符串、数组、切片等进行迭代输出元素。

package main

import "fmt"

func main() {
	strings := []string{"google","baidu","youtube"} //[]表示range的范围
	for i,s := range strings{
		fmt.Println(i,s)
	}

	numbers := [6]int{1,2,3,4,5,6}
	for i,x := range numbers{
		fmt.Printf("第 %d 位 x 的值 = %d\n",i,x)
	}
}