#!/usr/bin/python3

import func_vdip
import func_api_path
import pprint
import requests
import sys
import readline
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import json
import urllib3

urllib3.disable_warnings()


reqOrg = requests.get(
    url=func_vdip.func_ctg_vd_ip() + func_api_path.get_org(),
    headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
    auth=HTTPBasicAuth(func_vdip.func_ctg_vd_username(), func_vdip.func_ctg_vd_pwd()),
    verify=False
)

reqOrgDict = json.loads(reqOrg.text)
# print(json.dumps(reqOrgDict, indent=4, sort_keys=True))

transformDictName = {}
transformDictID = {}
for x in reqOrgDict["organizations"]:
    transformDictName[x["name"]] = x["globalOrgId"]
    transformDictID[x["globalOrgId"]] = x["name"]
# print(json.dumps(transformDictName, indent=4, sort_keys=True))
# print(json.dumps(transformDictID, indent=4, sort_keys=True))


orgVar = input("Please input orgName or orgID:")
if orgVar.isdigit():
    orgVarIsID = orgVar
    print(orgVar, "org name is:", transformDictID[orgVarIsID])
else:
    if "Customer" not in orgVar:
        print("You entered something wrong!")
        sys.exit()
    else:
        orgVarIsOrgName = orgVar
        print(orgVar, "ID is:", transformDictName[orgVarIsOrgName])
