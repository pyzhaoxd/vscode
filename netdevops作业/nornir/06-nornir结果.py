from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
if __name__ == '__main__':

    nr = InitNornir(
        config_file="nornir_end.yaml", dry_run=True
    )

    results = nr.run(
        task=napalm_get, getters=["interfaces"]
    )
    print_result(results)
    mac_list = []
    # 迭代所有的网络设备及其结果，这个results是一个类似字典的数据结构，key是host value是每个设备的执行结果
    for host, rs in results.items():
        ## 对每台网络设备的结果进行获取，每台网络设备的结果是一个类似列表的数据结构，可以直接用索引取对应的结果
        # 取到的结果是一个Result结构，包含了是否失败，主机信息，错误信息，我们返回的真正的数据（result中），
        # 所以要再点一下result才能拿到真正的每个task返回的data
        for intf, intf_obj in rs[0].result['interfaces'].items():
            print(intf_obj)
        try:
            mac_list.extend([intf_obj.get('mac_address')  for intf,intf_obj in rs[0].result['interfaces'].items()])
        except Exception as e :
            print(e)
    print(mac_list)