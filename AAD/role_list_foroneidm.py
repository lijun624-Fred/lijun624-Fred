import os
import json

query_scope = "\"[?principalType=='User'&&principalName!='admin@boschcn.partner.onmschina.cn'].{principalName:principalName, roleDefinitionName:roleDefinitionName, scope:scope}\""
old_domain = "boschcn.partner.onmschina.cn"
new_domain = "bosch.com"

def get_role_assignment():
    with open('subscription_fulllist.txt', 'r') as subscriptions:
       while True:
            sub_id = subscriptions.readline()
            if not sub_id:
                break
            sub_id = sub_id.strip('\n')
            cmd_list = "az role assignment list --scope /subscriptions/" + sub_id + " --output json --query " + query_scope
            result = os.popen(cmd_list)
            role_json = result.read()
            role_list = json.loads(role_json)
            # print(role_list)
            for role_dic in role_list:
                user_name = str(role_dic['principalName'])
                sub_id = str(role_dic['scope'])
                access_right = "CN=IDM2BCD_AzCN_" + sub_id.lstrip('/subscriptions/') + "_" + role_dic['roleDefinitionName'] + ",OU=SECURITYGROUPS,OU=Ci-idm2bcd,OU=Applications,DC=de,DC=bosch,DC=com"
                print(user_name, access_right)

if __name__ == "__main__":
    get_role_assignment()
