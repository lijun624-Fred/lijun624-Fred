import os
import json

query_scope = "\"[?principalType=='User'&&principalName!='admin@boschcn.partner.onmschina.cn'].{principalName:principalName, roleDefinitionName:roleDefinitionName, scope:scope}\""
old_domain = "boschcn.partner.onmschina.cn"
new_domain = "bosch.com"

def get_role_assignment():
    with open('subscriptionlist.txt', 'r') as subscriptions:
       while True:
            sub_id = subscriptions.readline()
            if not sub_id:
                break
            sub_id = sub_id.strip('\n')
            cmd_list = "az role assignment list --all --subscription " + sub_id + " --output json --query " + query_scope
            result = os.popen(cmd_list)
            role_json = result.read()
            role_list = json.loads(role_json)
            for role_dic in role_list:
                user_name = role_dic['principalName']
                ## when contains 'providers', it's resource level assingment, if not its subsciption level assignment
                if role_dic['scope'].find('providers') > 0:   
                    cmd_assign = "az role assignment create --assignee " + user_name.replace(old_domain, new_domain) + " --role " + role_dic['roleDefinitionName'] + " --scope " + role_dic['scope']
                else:
                    cmd_assign = "az role assignment create --assignee " + user_name.replace(old_domain, new_domain) + " --role " + role_dic['roleDefinitionName'] + " --subscription " + role_dic['scope']
                print(cmd_assign)

if __name__ == "__main__":
    get_role_assignment()
