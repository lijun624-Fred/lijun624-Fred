import os
import json
import role_assign

def group_copy_membership():
    with open('grouplist.txt', 'r') as groups:
        while True:
            groupname = groups.readline()
            if not groupname:
                break
            groupname = groupname.strip('\n')
            cmd_group_list = "az ad group member list --group " + groupname + " |grep userPrincipalName|awk '{print $2}'"
            memberlist = os.popen(cmd_group_list).read()
            nt_memberlist = memberlist.split('\n')
            if nt_memberlist[-1] == '': nt_memberlist.pop()  #remove the empty element in the end
            for member in nt_memberlist:
                mail_name = member.split("@")[0].replace('"', '').lower()
                if role_assign.df['email'].str.contains(mail_name).any():
                    ntname = role_assign.df.loc [role_assign.df['email'] == mail_name, 'ntname'].item() #ilf2szh@bosch.com
                    new_upn = ntname.split ("@")[0] + role_assign.new_domain #ilf2szh_bosch.com#EXT#@boschcn.partner.onmschina.cn
                    cmd_objectid = "az ad user show --id " + new_upn + " --output json --query {id:id}"
                    result = os.popen(cmd_objectid)
                    objectid_json = result.read()
                    user_object_id = json.loads(objectid_json)
                    cmd_add_membership = "az ad group member add --group " + groupname + " --member-id " + user_object_id['id']
                    print(cmd_add_membership)
                else:
                    print(mail_name)    #the user doesn't exist

if __name__ == "__main__":
    group_copy_membership()
