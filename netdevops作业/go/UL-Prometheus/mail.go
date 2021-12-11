package mail

import (
	"fmt"
	"strconv"

	"gopkg.in/gomail.v2"
)

//SendMail ...
func SendMail(mailFrom string, sender string, password string, smpthost string, port string, mailTo []string, subject string, body string) error {
	//定义邮箱服务器连接信息，如果是阿里邮箱 pass填密码，qq邮箱填授权码
	mailConn := map[string]string{
		"mailfrom": mailFrom,
		"user":     sender,
		"pass":     password,
		"host":     smpthost,
		"port":     port,
	}
	intport, _ := strconv.Atoi(mailConn["port"]) //转换端口类型为int

	m := gomail.NewMessage()
	// m.SetHeader("From", "SDWAN ALARM"+"<"+mailConn["user"]+">") //这种方式可以添加别名， 也可以直接用<code>m.SetHeader("From",mailConn["user"])</code> 读者可以自行实验下效果
	m.SetHeader("From", mailConn["mailfrom"]) //这种方式可以添加别名， 也可以直接用<code>m.SetHeader("From",mailConn["user"])</code> 读者可以自行实验下效果
	m.SetHeader("To", mailTo...)              //发送给多个用户
	m.SetHeader("Subject", subject)           //设置邮件主题
	m.SetBody("text/html", body)              //设置邮件正文

	d := gomail.NewDialer(mailConn["host"], intport, mailConn["user"], mailConn["pass"])
	// d.TLSConfig = &tls.Config{InsecureSkipVerify: true}

	err := d.DialAndSend(m)
	if err != nil {
		fmt.Println(err.Error())
	}
	return err

}
