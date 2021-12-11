# get method
def get_org():
    org_path = "/vnms/organization/orgs"
    return org_path


# get method
def get_appliance_list():
    appliance_list_path = "/vnms/appliance/appliance?offset=0&limit=10000"
    return appliance_list_path


# get method
def get_customer_appliance_list(customer_name):
    customer_appliance_list_path = "/vnms/appliance/filter/" + customer_name + "offset=0&limit=10000"
    return customer_appliance_list_path


# get method
def get_dg_list(customer_name):
    dg_path = "/nextgen/deviceGroup?organization=" + customer_name + "&offset=0&limit=25"
    return dg_path


# post method, need input dg name
def post_dg_template_sync_status():
    dg_template_sync_status_path = "/vnms/template/deviceGroup/deviceStatus"
    return dg_template_sync_status_path


# post method
def post_commit_template(appliance_name):
    commit_template_path = "/vnms/template/applyTemplate/" + appliance_name + "/devices?reboot=false"
    return commit_template_path


# get method
def get_template(template_name):
    get_template_path = "/vnms/sdwan/workflow/templates/template/" + template_name
    return get_template_path


# post method, need input template name
def post_save_template():
    save_template_path = "/vnms/sdwan/workflow/templates/template"
    return save_template_path


# post method
def post_deploy_template(template_name):
    deploy_template_path = "/vnms/sdwan/workflow/templates/template/deploy/" + template_name + "?verifyDiff=true"
    return deploy_template_path


# post method, need input dg information
def post_create_dg():
    create_dg_path = "/nextgen/deviceGroup"
    return create_dg_path


# get method, need input device name
def get_device(device_name):
    get_device_path = "/vnms/sdwan/workflow/devices/device/" + device_name
    return get_device_path


# get method
def get_available_id():
    get_available_id_path = "/vnms/sdwan/global/Branch/availableId/withSerialNumber"
    return get_available_id_path


# post method
def post_get_data(device_name):
    get_data_path = "/vnms/sdwan/workflow/devices/device/template/data/" + device_name
    return get_data_path


# post method, need input
def post_save_device():
    save_device_path = "/vnms/sdwan/workflow/devices/device"
    return save_device_path


# post method, need input
def post_deploy_device(device_name):
    deploy_device_path = "/vnms/sdwan/workflow/devices/device/deploy/" + device_name
    return deploy_device_path

