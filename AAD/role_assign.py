import os
import json
import pandas as pd

query_scope = "\"[?principalType=='User'&&principalName!='admin@boschcn.partner.onmschina.cn'].{principalName:principalName, roleDefinitionName:roleDefinitionName, scope:scope}\""
old_domain = "boschcn.partner.onmschina.cn"
new_domain = "_bosch.com#EXT#@boschcn.partner.onmschina.cn"
df = pd.read_csv ("ntaccounts.csv")

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
                user_name = role_dic['principalName'].split ("@")[0]  #fred.li
                ntname = df.loc [df['email'] == user_name, 'ntname'].item() #ilf2szh@bosch.com
                new_upn = ntname.split ("@")[0] + new_domain #ilf2szh_bosch.com#EXT#@boschcn.partner.onmschina.cn
                cmd_assign = "az role assignment create --assignee " + new_upn + " --role " + role_dic['roleDefinitionName'] + " --scope " + role_dic['scope']
                print(cmd_assign)

if __name__ == "__main__":
    get_role_assignment()
