package main

import (
    "net/http"
)


func main() {
    http.Handle("/", http.FileServer(http.Dir("/")))
    http.ListenAndServe(":8080", nil)
}


// 下面是代码说明：
// 第 1 行，标记当前文件为 main 包，main 包也是 Go 程序的入口包。
// 第 3~5 行，导入 net/http 包，这个包的作用是 HTTP 的基础封装和访问。
// 第 7 行，程序执行的入口函数 main()。
// 第 8 行，使用 http.FileServer 文件服务器将当前目录作为根目录（/目录）的处理器，访问根目录，就会进入当前目录。
// 第 9 行，默认的 HTTP 服务侦听在本机 8080 端口。

// 把这个源码保存为 main.go（Go语言的源文件后缀就是.go），安装Go语言的开发包（后续我们会讲解如何安装），在命令行输入如下命令：
// $ go run main.go

// 在浏览器里输入http://127.0.0.1:8080即可浏览文件，这些文件正是当前目录在HTTP服务器上的映射目录。