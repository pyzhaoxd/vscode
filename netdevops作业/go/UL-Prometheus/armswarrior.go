/*
 * @Author: Sean
 * @Date: 2021-04-29 09:37:09
 * @LastEditTime: 2021-05-03 18:22:48
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /lake-marionette/bin/puppet/icmpprober/prober.go
 */
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net/url"
	"os"
	"strconv"
	"strings"
	"time"

	"dev.azure.com/unilake/LakeEye/lake-common.git/pkg/utils/shell"
	"dev.azure.com/unilake/LakeEye/lake-common.git/pkg/utils/system"
	"github.com/koding/multiconfig"
)

type config struct {
	Version string    `json:"version"`
	Type    string    `json:"type"`
	Sensors []sensor  `json:"destnations"`
	Bgppeer []bgppeer `json:"bgppeer"`
}

type bgppeer struct {
	VR         string `json:"vr"`
	NeighborIP string `json:"neighbor_ip"`
	Sendto     sendto `json:"sendto"`
}

type sensor struct {
	Name     string `json:"name"`
	Dst      string `json:"dst"`
	Interval int    `json:"interval"`
	Count    int    `json:"count"`
	Times    int    `json:"times"`
	Netns    string `json:"netns"`
	Srcinf   string `json:"srcinf"`
	Sendto   sendto `json:"sendto"`
}

type sendto struct {
	Method   string `json:"method"`
	Fromns   string `json:"fromns"`
	Endpoint string `json:"endpoint"`
}

// type ICMPRes struct {
// 	Host       string  `json:"host"`
// 	Name       string  `json:"name"`
// 	PacketLoss float64 `json:"packetloss"`
// 	MinDelay   float64 `json:"mindelay"`
// 	MaxDelay   float64 `json:"maxdelay"`
// 	AvgDelay   float64 `json:"avgdelay"`
// }

var params = new(config)

// InitParams 初始化业务参数
func initParams() {

	// init configuration here
	var paths = []string{
		"./etc/unilake/lakebots/params.json",
		"/etc/unilake/lakebots/params.json",
		"./params.json",
		"../conf/params.json",
	}
	var configPath string
	for _, p := range paths {
		_, err := os.Stat(p)
		if err == nil {
			configPath = p
		}

	}

	fmt.Println(configPath)
	m := multiconfig.NewWithPath(configPath)
	m.MustLoad(params)

}

func sendRes(res []byte, dest sensor) {
	// fmt.Println(string(res))
	packetLoss := 100.0
	var minDelay float64
	var maxDelay float64
	var avgDelay float64
	lines := strings.Split(string(res), "\n")
	for _, line := range lines {
		fmt.Println(line)
		if len(line) == 0 {
			continue
		}
		// strLine := string(l)
		if strings.Contains(line, "packets transmitted") {
			tmpPacketLoss := line[strings.Index(line, "received,")+10 : strings.Index(line, "% packet")]
			var err error
			packetLoss, err = strconv.ParseFloat(tmpPacketLoss, 64)
			if err != nil {
				continue
			}
		}
		if strings.Contains(line, "min/avg/max/mdev") {
			tmpDelay := line[strings.Index(line, "= ")+2 : strings.Index(line, "ms")-1]
			tmpDelayList := strings.Split(tmpDelay, "/")
			if len(tmpDelayList) != 4 {
				continue
			}
			var err error
			minDelay, err = strconv.ParseFloat(tmpDelayList[0], 64)
			if err != nil {
				continue
			}
			maxDelay, err = strconv.ParseFloat(tmpDelayList[1], 64)
			if err != nil {
				continue
			}
			avgDelay, err = strconv.ParseFloat(tmpDelayList[2], 64)
			if err != nil {
				continue
			}
		}
	}
	if dest.Sendto.Method == "Prom" {
		err := pushICMPMetricFromFile(dest, packetLoss, minDelay, maxDelay, avgDelay, dest.Sendto.Endpoint)
		if err != nil {
			return
		}

	} else {
		saveWebhookFile()
	}
}

func pushICMPMetricFromFile(dest sensor, packetLoss, minDelay, maxDelay, avgDelay float64, endpoint string) error {
	hostname := system.GetHostname()
	// save to file
	filename := fmt.Sprint(dest.Name, strconv.FormatInt(time.Now().Unix(), 10))
	f, err := os.Create(filename)
	defer f.Close()
	if err != nil {
		fmt.Println(err.Error())
		return err
	}

	w := bufio.NewWriter(f)
	// # TYPE some_metric counter
	lineStr := "# TYPE maxdelay gauge"
	fmt.Fprintln(w, lineStr)
	lineStr = fmt.Sprintf("maxdelay{type=\"icmprobe\",sensorname=\"%s\"} %f", dest.Name, maxDelay)
	fmt.Fprintln(w, lineStr)

	lineStr = "# TYPE mindelay gauge"
	fmt.Fprintln(w, lineStr)
	lineStr = fmt.Sprintf("mindelay{type=\"icmprobe\",sensorname=\"%s\"} %f", dest.Name, minDelay)
	fmt.Fprintln(w, lineStr)

	lineStr = "# TYPE avgdelay gauge"
	fmt.Fprintln(w, lineStr)
	lineStr = fmt.Sprintf("avgdelay{type=\"icmprobe\",sensorname=\"%s\"} %f", dest.Name, avgDelay)
	fmt.Fprintln(w, lineStr)

	lineStr = "# TYPE packetloss gauge"
	fmt.Fprintln(w, lineStr)
	lineStr = fmt.Sprintf("packetloss{type=\"icmprobe\",sensorname=\"%s\"} %f", dest.Name, packetLoss)
	fmt.Fprintln(w, lineStr)
	err = w.Flush()
	if err != nil {
		return err
	}
	//create test policy
	u, _ := url.Parse(endpoint)
	policyCMD := fmt.Sprintf("/bin/echo 'test filter create type=v4 proto=6 dst=0.0.0.1/32 src=%s sport=%s control-app' | nc -C 0 9001 >/dev/null 2>&1", u.Host, u.Port())
	shell.RunCmd(policyCMD)
	pushCMD := fmt.Sprintf("curl --data-binary @%s -u prom:unilakeprom %s/metrics/job/pushgateway_sensors/instance/%s", filename, dest.Sendto.Endpoint, hostname)
	if dest.Sendto.Fromns != "default" {
		pushCMD = fmt.Sprintf("/bin/echo 'versa123' | sudo ip netns exec %s %s", dest.Sendto.Fromns, pushCMD)
	}
	fmt.Println(pushCMD)
	shell.RunCmd(pushCMD)
	os.Remove(filename)
	return nil
}

func pushBGPCheckFromFile(bgpp bgppeer, state, etime float64) error {
	hostname := system.GetHostname()
	// save to file
	filename := fmt.Sprint(bgpp.NeighborIP, strconv.FormatInt(time.Now().Unix(), 10))
	f, err := os.Create(filename)
	defer f.Close()
	if err != nil {
		fmt.Println(err.Error())
		return err
	}

	w := bufio.NewWriter(f)
	// # TYPE some_metric counter
	lineStr := "# TYPE maxdelay gauge"
	fmt.Fprintln(w, lineStr)
	lineStr = fmt.Sprintf("bgpstate{vr=\"%s\",peer=\"%s\"} %f", bgpp.VR, bgpp.NeighborIP, state)
	fmt.Fprintln(w, lineStr)

	lineStr = "# TYPE mindelay gauge"
	fmt.Fprintln(w, lineStr)
	lineStr = fmt.Sprintf("bgp_est_time{vr=\"%s\",peer=\"%s\"} %f", bgpp.VR, bgpp.NeighborIP, etime)
	fmt.Fprintln(w, lineStr)

	err = w.Flush()
	if err != nil {
		return err
	}
	//create test policy
	u, _ := url.Parse(bgpp.Sendto.Endpoint)
	policyCMD := fmt.Sprintf("/bin/echo 'test filter create type=v4 proto=6 dst=0.0.0.1/32 src=%s sport=%s control-app' | nc -C 0 9001 >/dev/null 2>&1", u.Host, u.Port())
	shell.RunCmd(policyCMD)
	pushCMD := fmt.Sprintf("curl --data-binary @%s -u prom:unilakeprom %s/metrics/job/pushgateway_sensors/instance/%s", filename, bgpp.Sendto.Endpoint, hostname)
	if bgpp.Sendto.Fromns != "default" {
		pushCMD = fmt.Sprintf("/bin/echo 'versa123' | sudo ip netns exec %s %s", bgpp.Sendto.Fromns, pushCMD)
	}
	fmt.Println(pushCMD)
	shell.RunCmd(pushCMD)
	os.Remove(filename)
	return nil
}

func saveWebhookFile() {

}

func checkBgp(bgpp bgppeer) (string, string, error) {
	// echo 'show bgp neighbor brief Customer1132-LAN-VR | display json' | /opt/versa/confd/bin/confd_cli
	var bgpCheckCMD = fmt.Sprint("echo 'show bgp neighbor brief " + bgpp.VR + " | display json' | /opt/versa/confd/bin/confd_cli")
	res := shell.RunCmd(bgpCheckCMD)
	if !res.Ok {
		fmt.Printf("run ping cmd error %s", res.Error)
	}
	/*
		var abc = `{
			  "data": {
			    "routing-module:bgp": {
			      "neighbors": {
			        "brief": [
			          {
			            "routing-instance": "Customer1132-LAN-VR",
			            "neighbor-ip": [
			              {
			                "neighbor-ip": "169.254.1.1",
			                "local-address-type": "ipv4",
			                "local-addr": "0.0.0.0",
			                "local-port": 0,
			                "remote-addr-type": "ipv4",
			                "remote-port": 0,
			                "remote-as-number": "64614",
			                "state": "Established",
			                "total-sent-prefixes": 4,
			                "total-received-prefixes": 9,
			                "established-time": "05:07:04",
			                "total-received-messages": 30349,
			                "total-transmitted-messages": 34905
			              },
			              {
			                "neighbor-ip": "169.254.0.12",
			                "local-address-type": "ipv4",
			                "local-addr": "169.254.0.13",
			                "local-port": 0,
			                "remote-addr-type": "ipv4",
			                "remote-port": 0,
			                "remote-as-number": "64513",
			                "state": "Established",
			                "total-sent-prefixes": 13,
			                "total-received-prefixes": 1,
			                "established-time": "1w0d00h",
			                "total-received-messages": 23701,
			                "total-transmitted-messages": 23302
			              }
			            ]
			          }
			        ]
			      }Error: application protocol error
			[error][2021-09-03 00:07:05]`
	*/
	// lastIndex := strings.LastIndex(string(res.Output), "}")
	output := string(res.Output)
	lastIndex := strings.LastIndex(output, "}")

	firstIndex := strings.Index(output, "\"neighbors\": ")
	bgpInfo := output[firstIndex+13 : lastIndex+1]
	// fmt.Println(bgpInfo)
	var data map[string]interface{}
	err := json.Unmarshal([]byte(bgpInfo), &data)
	if err != nil {
		return "", "", fmt.Errorf("output struct error")
	}
	neighbors, ok := data["brief"].([]interface{})
	if !ok {
		return "", "", fmt.Errorf("output struct error")
	}
	for _, neighbor := range neighbors {
		routingInstanceName, ok := neighbor.(map[string]interface{})["routing-instance"].(string)
		if !ok {
			return "", "", fmt.Errorf("output struct error")
		}
		if routingInstanceName != bgpp.VR {
			continue
		}
		neighborIPs, ok := neighbor.(map[string]interface{})["neighbor-ip"].([]interface{})
		if !ok {
			return "", "", fmt.Errorf("output struct error")
		}
		for _, neighborIP := range neighborIPs {
			ip, ok := neighborIP.(map[string]interface{})["neighbor-ip"].(string)
			if !ok {
				return "", "", fmt.Errorf("output struct error")
			}
			if ip == bgpp.NeighborIP {
				state, ok := neighborIP.(map[string]interface{})["state"].(string)
				if !ok {
					return "", "", fmt.Errorf("output struct error")
				}
				establishedTime, ok := neighborIP.(map[string]interface{})["established-time"].(string)
				if !ok {
					return "", "", fmt.Errorf("output struct error")
				}
				return state, establishedTime, nil
			}
		}
		return "", "", fmt.Errorf("not found neighbor")
	}
	return "", "", fmt.Errorf("not found neighbor")
}

func runProbe(dest sensor) {
	var pingCMD string
	if dest.Netns != "default" {
		pingCMD = fmt.Sprint("/bin/echo 'versa123' | sudo ip netns exec ", dest.Netns, " ping ", dest.Dst, " -c ", dest.Count, " -i ", dest.Interval)
	} else {
		pingCMD = fmt.Sprint("ping ", dest.Dst, " -c ", dest.Count, " -i ", dest.Interval)
	}
	if dest.Srcinf != "" {
		pingCMD = fmt.Sprint(pingCMD, " -I ", dest.Srcinf)
	}
	// //判断node为flexvnf的情况
	// if params.Type == "flexvnf" {
	// 	pingCMD = fmt.Sprint("/bin/echo 'versa123' | sudo ", pingCMD)
	// }
	fmt.Println(pingCMD)
	i := 0
	for {
		res := shell.RunCmd(pingCMD)
		if !res.Ok {
			fmt.Printf("run ping cmd error %s", res.Error)
		}
		sendRes(res.Output, dest)
		fmt.Println(i)
		i++
		if i == dest.Times {
			break
		}
		time.Sleep(1000)
	}
}

func runCheckBgp(bgpp bgppeer) {
	for {
		var floatState, floatEstTime float64

		state, estTime, err := checkBgp(bgpp)
		if err != nil {
			fmt.Println(err)
			time.Sleep(5000)
			continue
		}
		if state == "Established" {
			floatState = 1
		} else {
			floatState = 0
		}

		if !strings.Contains(estTime, ":") {
			floatEstTime = 24 * 60 * 60 // more then 24 hours
		} else {

			shortTime := strings.Split(estTime, ":")
			h, err1 := strconv.Atoi(shortTime[0])
			m, err2 := strconv.Atoi(shortTime[1])
			s, err3 := strconv.Atoi(shortTime[2])
			if err1 != nil || err2 != nil || err3 != nil {
				floatEstTime = -1
			} else {
				floatEstTime = float64(h*60*60 + m*60 + s)
			}

		}

		err = pushBGPCheckFromFile(bgpp, floatState, floatEstTime)
		if err != nil {
			fmt.Println(err)
		}
		time.Sleep(5000)
	}

}

func main() {
	initParams()
	for _, dest := range params.Sensors {
		go runProbe(dest)
	}
	for _, bgp := range params.Bgppeer {
		go runCheckBgp(bgp)
	}
	select {}
}

// func main() {
// 	abc := "05:07:04"
// 	abcspl := strings.Split(abc, ":")
// 	fmt.Println(strconv.Atoi(abcspl[0]))
// 	fmt.Println(strconv.Atoi(abcspl[1]))
// 	fmt.Println(strconv.Atoi(abcspl[2]))
// }
