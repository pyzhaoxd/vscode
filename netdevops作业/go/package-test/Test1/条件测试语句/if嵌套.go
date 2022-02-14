// if 布尔表达式 1 {
//    /* 在布尔表达式 1 为 true 时执行 */
//    if 布尔表达式 2 {
//       /* 在布尔表达式 2 为 true 时执行 */
//    }
// }


// package main

// import "fmt"

// func main() {
//    /* 定义局部变量 */
//    var a int = 100
//    var b int = 200
 
//    /* 判断条件 */
//    if a == 100 {
//        /* if 条件语句为 true 执行 */
//        if b == 200 {
//           /* if 条件语句为 true 执行 */
//           fmt.Printf("a 的值为 100 ， b 的值为 200\n" );
//        }
//    }
//    fmt.Printf("a 值为 : %d\n", a );
//    fmt.Printf("b 值为 : %d\n", b );
// }


//判断用户密码输入案例：

package main 

import"fmt"

func main(){
    var a int 
    var b int
    fmt.Printf("请输入密码：   \n")
    fmt.Scan(&a)
	//调试语句
	fmt.Printf("a in",a)
    if a == 5211314 {
    fmt.Printf("请再次输入密码：")
    fmt.Scan(&b)
        if b == 5211314 {
            fmt.Printf("密码正确，门锁已打开")
        }else{
            fmt.Printf("非法入侵，已自动报警")
        }
    }else{
        fmt.Printf("非法入侵，已自动报警")
    }
}