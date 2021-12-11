// 变量初始化的标准格式
var 变量名 类型 = 表达式

var hp int = 100


// 编译器推导类型的格式
var hp = 100

var attack = 40
var defence = 20
var damageRate float32 = 0.17
var damage = float32(attack-defence) * damageRate
fmt.Println(damage)

// 短变量声明并初始化
hp := 100


短变量声明的形式在开发中的例子较多，比如：
conn, err := net.Dial("tcp","127.0.0.1:8080")
net.Dial 提供按指定协议和地址发起网络连接，这个函数有两个返回值，一个是连接对象（conn），一个是错误对象（err）。如果是标准格式将会变成：
var conn net.Conn
var err error
conn, err = net.Dial("tcp", "127.0.0.1:8080")


注意：在多个短变量声明和赋值中，至少有一个新声明的变量出现在左值中，即便其他变量名可能是重复声明的，编译器也不会报错，代码如下：
纯文本复制
conn, err := net.Dial("tcp", "127.0.0.1:8080")
conn2, err := net.Dial("tcp", "127.0.0.1:8080")