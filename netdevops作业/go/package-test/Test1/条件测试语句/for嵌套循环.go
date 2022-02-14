// 语法

// 以下为 Go 语言嵌套循环的格式：
// for [condition |  ( init; condition; increment ) | Range]
// {
//    for [condition |  ( init; condition; increment ) | Range]
//    {
//       statement(s);
//    }
//    statement(s);
// }


// package main

// import "fmt"

// func main() {
//    /* 定义局部变量 */
//    var i, j int

//    for i=2; i < 100; i++ {
//       for j=2; j <= (i/j); j++ {
//          if(i%j==0) {
//             break; // 如果发现因子，则不是素数
//          }
//       }
//       if(j > (i/j)) {
//          fmt.Printf("%d  是素数\n", i);
//       }
//    }  
// }

// package main 
// import "fmt"
// func main() {
// 	var d int = 4
// 	var f int = 2
// 	c := d%f
// 	fmt.Println(c)

// }


//九九乘法表

package main 

import "fmt"

func main() {
    for m := 1; m < 10; m++ {
    //fmt.Printf("第%d次：\n",m) 
        for n := 1; n <= m; n++ { 
            fmt.Printf("%dx%d=%d ",n,m,m*n)
        }
        fmt.Println("")
    }
}