from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
if __name__ == '__main__':

    nr = InitNornir(
        config_file="nornir_complex_inventory.yaml", dry_run=True
    )

    results = nr.run(
        task=napalm_get, getters=["facts"]
    )
    print_result(results)