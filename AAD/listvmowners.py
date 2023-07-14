import os
import json

query_scope = "\"[?principalType=='User'&&principalName!='admin@boschcn.partner.onmschina.cn'].{principalName:principalName}\""
old_domain = "boschcn.partner.onmschina.cn"
new_domain = "bosch.com"

def list_vm_owners():
    with open('vmsubs.txt', 'r') as subscriptions:
       while True:
            sub_id = subscriptions.readline()
            if not sub_id:
                break
            sub_id = sub_id.strip('\n')
            cmd_owner_list = "az role assignment list --role owner --scope /subscriptions/" + sub_id + " --output json --query " + query_scope
            result = os.popen(cmd_owner_list)
            owner_json = result.read()
            owner_list = json.loads(owner_json)
            if not owner_list:
                cmd_contributor_list = "az role assignment list --role contributor --scope /subscriptions/" + sub_id + " --output json --query " + query_scope
                result1 = os.popen(cmd_contributor_list)
                contributor_json = result1.read()
                contributor_list = json.loads(contributor_json)
                for contributor_name in contributor_list:
                    print(contributor_name['principalName'])  
            else:               
                for owner_name in owner_list:
                    print(owner_name['principalName'])

if __name__ == "__main__":
    list_vm_owners()