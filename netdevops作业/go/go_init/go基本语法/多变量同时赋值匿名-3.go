

package main

import (
    "fmt"
)


// func main (){
// 	var a int = 100
// 	var b int = 200
// 	b, a = a, b
// 	fmt.Println(a, b)
	
			
// }


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
