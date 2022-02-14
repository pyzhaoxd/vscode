// Go 语言的 goto 语句可以无条件地转移到过程中指定的行。
// goto 语句通常与条件语句配合使用。可用来实现条件转移， 构成循环，跳出循环体等功能。

// 但是，在结构化程序设计中一般不主张使用 goto 语句， 以免造成程序流程的混乱，使理解和调试程序都产生困难。
// 语法

// goto 语法格式如下：

// goto label;
// ..
// .
// label: statement;


// 在变量 a 等于 15 的时候跳过本次循环并回到循环的开始语句 LOOP 处：  
// 		+
//   		+
//   		+
// 标记1   代码块1-------------------------
// 		+								 -
// 标记2	代码块2                       -goto标记3
// 		+                                -
// 标记3   代码块3-------------------------

// 实例
package main

import "fmt"

func main() {
   /* 定义局部变量 */
   var a int = 10

   /* 循环 */
   LOOP: for a < 20 {
      if a == 15 {
         /* 跳过迭代 */
         a = a + 1
         goto LOOP
      }
      fmt.Printf("a的值为 : %d\n", a)
      a++    
   }  
}

// package main

// import "fmt"

// func main() {
//    /* 定义局部变量 */
//    var a int = 10

//    /* 循环 */
//    LOOP: for a < 20 {
//       if a == 15 {
//          /* 跳过迭代 */
//          a = a + 1
//          goto LOOP
//       }
//       fmt.Printf("a的值为 : %d\n", a)
//       a++    
//    }  
// }
package main 

import "fmt"

func main() {
    print9x()
    // gotoTag()
}

//嵌套for循环打印九九乘法表
func print9x() {
    for m := 1; m < 10; m++ {
        for n := 1; n <= m; n++ {
      		fmt.Printf("%dx%d=%d ",n,m,m*n)
        }
        fmt.Println("")
    }
}

//for循环配合goto打印九九乘法表
func gotoTag() {
    for m := 1; m < 10; m++ {
    n := 1
    LOOP: if n <= m {
        fmt.Printf("%dx%d=%d ",n,m,m*n)
        n++
        goto LOOP
    } else {
        fmt.Println("")
    }
    n++
	}
}