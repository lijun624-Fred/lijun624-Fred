import os
import json
import pandas as pd

cmd_applist = "az ad app list --all --output json --query '[].appId'"
# replace '--show-mine' with '--all' for production use

df_user = pd.read_csv ("pocusers.csv")

def assign_app_owners():
    app_list = os.popen(cmd_applist).read()
    app_json = json.loads(app_list)
    for app_id in app_json:
        cmd_appowner = "az ad app owner list --id " + app_id + " --query '[].userPrincipalName'"
        app_owner = os.popen(cmd_appowner).read()
        owner_json = json.loads(app_owner)
        for owner_name in owner_json:
            # get the NT name of the owner
            # az ad user show --id "NT name" --query "id" --output tsv
            # az ad app owner add --id 00000000-0000-0000-0000-000000000000 --owner-object-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
            user_name = str(owner_name).split("@")[0].lower()
            if df_user['displayName'].str.contains(user_name).any():
                # print(owner_name,app_id)
                # ntname = df_user.loc [df_user['displayName'] == user_name, 'mail'].item()
                user_id = df_user.loc [df_user['displayName'] == user_name, 'id'].item()
                cmd_assign_owner = "az ad app owner add --id " + app_id + " --owner-object-id " + user_id
                # os.system(cmd_assign_owner)
                print(cmd_assign_owner)

if __name__ == "__main__":
    assign_app_owners()