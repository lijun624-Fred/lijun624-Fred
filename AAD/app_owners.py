import os
import json

cmd_applist = "az ad app list --show-mine --output json --query '[].appId'"

# replace '--show-mine' with '--all' for production use

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
            print(owner_name,app_id)

if __name__ == "__main__":
    assign_app_owners()