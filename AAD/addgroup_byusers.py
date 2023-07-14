import os
import json
import pandas as pd
import assign_role_by_user

def addgroup_byusers():
    cmd_group_list = "az ad group list"
    result = os.popen(cmd_group_list)
    group_result = result.read()
    group_dic = json.loads(group_result)
    for group in group_dic:
        print(group['displayName'])

        #add ' in case the group name contains blank
        cmd_group_list = "az ad group member list --group '" + group['displayName'] + "'"
        member_output = os.popen(cmd_group_list).read()
        member_dic = json.loads(member_output)
        for member in list(member_dic):

            #in case the member type is not user
            if member['@odata.type'] == "#microsoft.graph.user":
                upn = str(member['userPrincipalName']).split ("@")[0].lower()
            else:
                continue
            if assign_role_by_user.df_user['displayName'].str.contains(upn).any():
                user_id = assign_role_by_user.df_user.loc [assign_role_by_user.df_user['displayName'] == upn, 'id'].item()
                cmd_add_membership = "az ad group member add --group '" + group['displayName'] + "' --member-id " + user_id
                # print(cmd_add_membership)
                os.system(cmd_add_membership)

if __name__ == "__main__":
    addgroup_byusers()