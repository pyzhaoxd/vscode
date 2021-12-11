/*
 * @Author: Sean
 * @Date: 2021-05-04 11:30:38
 * @LastEditTime: 2021-05-04 14:49:45
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /lake-bot/bin/webhook/alertreceiver/receiver.go
 */

package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"dev.azure.com/unilake/LakeEye/lake-bot.git/pkg/mail"
	"dev.azure.com/unilake/LakeEye/lake-bot.git/pkg/wechat"
	"github.com/gin-gonic/gin"
)

type Alert struct {
	Labels      map[string]string `json:"labels"`
	Annotations map[string]string `json:"annotations"`
	StartsAt    time.Time         `json:"startsAt"`
	EndsAt      time.Time         `json:"endsAt"`
}

type Notification struct {
	Version           string            `json:"version"`
	GroupKey          string            `json:"groupKey"`
	Status            string            `json:"status"`
	Receiver          string            `json:"receiver"`
	GroupLabels       map[string]string `json:"groupLabels"`
	CommonLabels      map[string]string `json:"commonLabels"`
	CommonAnnotations map[string]string `json:"commonAnnotations"`
	ExternalURL       string            `json:"externalURL"`
	Alerts            []Alert           `json:"alerts"`
}

const (
	SENDER   = "cloud-sdwan"
	MAILFROM = "cloud-sdwan@chinatelecomglobal.com"
	// PASS     = "Cs2021!@#$"
	PASS     = "Cs2021!@34"
	SMPTHOST = "mail.chinatelecomglobal.com"
	SMPTPORT = "587"
	// SENDER   = "su0403@sina.com"
	// PASS     = "68bd671713f15d56"
	// SMPTHOST = "smtp.sina.com"
	// SMPTPORT = "587"
)

//lixil alert maillist: Kezhen.yang@lixil.com和dujia.gao@lixil.com
var RECIEVER = []string{"suming@unilake.io", "kevin.yang@unilake.io", "Kezhen.yang@lixil.com", "dujia.gao@lixil.com"}

func main() {
	router := gin.Default()
	router.POST("/webhook", icmpAlertHook)
	router.Run(":9098")
}

func icmpAlertHook(c *gin.Context) {
	var notification Notification

	err := c.BindJSON(&notification)

	jsonstr, _ := json.Marshal(notification)
	fmt.Println(string(jsonstr))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	for _, alert := range notification.Alerts {
		desc := fmt.Sprint(alert.Annotations["summary"], ",", alert.Annotations["description"])
		wechat.SendMSGTemplate("ypDr570y_EiKVTvIwaToflj-3wHjLUFblRT4Rk7hxVo", "Group1", alert.Labels["alertname"], desc, alert.StartsAt.String(), "联系相关人员", notification.ExternalURL)
		// err := mail.SendMail(MAILFROM, SENDER, PASS, SMPTHOST, SMPTPORT, []string{alert.Annotations["mailto"]}, alert.Annotations["summary"], alert.Annotations["description"])
		// go mail.SendMail(MAILFROM, SENDER, PASS, SMPTHOST, SMPTPORT, []string{alert.Annotations["mailto"]}, alert.Annotations["summary"], alert.Annotations["description"])
		go mail.SendMail(MAILFROM, SENDER, PASS, SMPTHOST, SMPTPORT, RECIEVER, alert.Annotations["summary"], alert.Annotations["description"])
		// if err != nil {
		// fmt.Print(err.Error())
		// }
	}
	c.JSON(http.StatusOK, gin.H{"message": " successful receive alert notification message!"})

}
