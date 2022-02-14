// Go 语言的 continue 语句 有点像 break 语句。但是 continue 不是跳出循环，而是跳过当前循环执行下一次循环语句。

// for 循环中，执行 continue 语句会触发 for 增量语句的执行。

// 在多重循环中，可以用标号 label 标出想 continue 的循环。

// package main

// import "fmt"

// func main() {
//    /* 定义局部变量 */
//    var a int = 10

//    /* for 循环 */
//    for a < 20 {
//       if a == 15 {
//          /* 跳过此次循环 */
//          a = a + 1;
//          continue;
//       }
//       fmt.Printf("a 的值为 : %d\n", a);
//       a++;    
//    }  
// }

//以下实例有多重循环，演示了使用标记和不使用标记的区别：

package main

import "fmt"

func main() {

    // 不使用标记
    fmt.Println("---- continue ---- ")
    for i := 1; i <= 3; i++ {
        fmt.Printf("i: %d\n", i)
            for i2 := 11; i2 <= 13; i2++ {
                fmt.Printf("i2: %d\n", i2)
                continue
            }
    }

    // 使用标记
    fmt.Println("---- continue label ----")
    re:
        for i := 1; i <= 3; i++ {
            fmt.Printf("i: %d\n", i)
                for i2 := 11; i2 <= 13; i2++ {
                    fmt.Printf("i2: %d\n", i2)
                    continue re
                }
        }
}