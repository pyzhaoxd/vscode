// Go 语言中 break 语句用于以下两方面：

//     用于循环语句中跳出循环，并开始执行循环之后的语句。
//     break 在 switch（开关语句）中在执行一条 case 后跳出语句的作用。
//     在多重循环中，可以用标号 label 标出想 break 的循环。
// package main

// import "fmt"

// func main() {
//    /* 定义局部变量 */
//    var a int = 10

//    /* for 循环 */
//    for a < 20 {
//       fmt.Printf("a 的值为 : %d\n", a);
//       a++;
//       if a > 15 {
//          /* 使用 break 语句跳出循环 */
//          break;
//       }
//    }
// }

//以下实例有多重循环，演示了使用标记和不使用标记的区别：

package main

import "fmt"

func main() {

    // 不使用标记
    fmt.Println("---- break ----")
    for i := 1; i <= 3; i++ {
        fmt.Printf("i: %d\n", i)
                for i2 := 11; i2 <= 13; i2++ {
                        fmt.Printf("i2: %d\n", i2)
                        break
                }
        }

    // 使用标记
    fmt.Println("---- break label ----")
    re:
        for i := 1; i <= 3; i++ {
            fmt.Printf("i: %d\n", i)
            for i2 := 11; i2 <= 12; i2++ {
                fmt.Printf("i2: %d\n", i2)
                break re
            }
        }
}