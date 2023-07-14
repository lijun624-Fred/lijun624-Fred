import os
import json
import pandas as pd

#Note: must add the display name for the nt accounts before run this script

df_vaults = pd.read_csv ("Azurevaults.csv")
df_cn = pd.read_csv ("_exportcnusers0710.csv")
list_policies = ["certificates", "keys", "secrets", "storage"]

def list_key_vault():
    for i in range(len(df_vaults.index)):
        #swith to the target subscription
        cmd_acc_set = "az account set --subscription " + df_vaults.loc[i]['SUBSCRIPTION']
        account = os.popen(cmd_acc_set)
        account.read()

        #read the access policy
        cmd_show_vault = "az keyvault show --name " + df_vaults.loc[i]['NAME'] + " --query properties.accessPolicies"
        result_policy = os.popen(cmd_show_vault)
        policy_json = result_policy.read()
        policy_list = json.loads(policy_json)

        #list the policies in a key vault
        for policy in policy_list:
            cmd_user_show = "az ad user show --id " + policy['objectId']
            result_user = os.popen(cmd_user_show)
            user_return = result_user.read()            
            if len(user_return) > 0:
                json_user = json.loads(user_return)

                #find the user display name
                user_name = str(json_user['userPrincipalName']).split ("@")[0].lower()
                if df_cn['displayName'].str.contains(user_name).any():
                    object_id = df_cn.loc [df_cn['displayName'] == user_name, 'id'].item()
                    #generate the vault permissions cmd
                    for vault in list_policies:
                        vault_policy = " "
                        if policy['permissions'][vault]:
                            for vault_action in policy['permissions'][vault]: 
                                vault_policy = vault_policy + " " + vault_action
                            if vault != "storage": vault_name = vault.rstrip("s")
                            cmd_key_policy = "az keyvault set-policy --name " + df_vaults.loc[i]['NAME'] + " --object-id " + object_id + " --" + vault_name + "-permissions" + vault_policy
                            ##############print or execute##############
                            #  print(cmd_key_policy)  
                            os.system(cmd_key_policy)    
                else:
                    print(user_name + " has no NT account")

if __name__ == "__main__":
    list_key_vault()