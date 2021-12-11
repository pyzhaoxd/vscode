#JSON的数据结构具有易读的特点，她是由键值对和对象组成，在结构上非常类似Python的字典，如果是一个典型的JSON数据格式
{
    "intf": "Gigabitethernet0/0",
    "status": "up"
}

#与Python的字典一样，JSON的键值对也是由冒号分开，左边是key,右边是value

#JSON与字典不一样的地方如下：
#JSON里的键的数据类型必须为字符串，而在字典字符串，常数，浮点数，或者元组等都能作为键的数据类型
#JSON里键的字符串内容必须使用双引号括起来，不像字典里即可以用单引号又可以用双引号来表示字符串
#JSON里键值对的值又分为两种形式：一种形式是简单的值，包括字符串，整数等 比如上面的Gigabitethernet0/0和up就是一种简单的值，另一种被称为对象，对象内容用大括号{}表示，对象中的键值对用逗号分开，他们是无序的
{"Vendor":"cisco","Model":"2960"}

#当有多组对象存在，将称为JSON阵列（JSON Array）阵列以中括号[]表示，阵列中的元素（即各对象）是有序您的（可以把它整理成列表）
{
    "devices":[
        {"Vendor":"Cisco","Model":"2960"},
        {"Vendor":"H3C","Model":"10510"},
        {"Vendor":"HUAWEI","Model":"ASR190"},
        {"Vendor":"Juniper","Model":"MX80"},
        {"Vendor":"F5","Model":"F123"},
    ]

}
