import os
import pandas as pd

df_user = pd.read_csv ("pocusers.csv")
df_role = pd.read_csv ("role_list_0712.csv")

def assign_role_by_user():
    for i in range(len(df_user.index)):
        user_name = df_user.loc[i]['displayName']
        print(user_name)
        
        #find the matchd index            
        match_index = df_role.loc [df_role['name'] == user_name].index
        for index_num in list(match_index):
            upn = str(df_user.loc[i]['mail']).split ("@")[0].lower() + "_bosch.com#EXT#@boschcn.partner.onmschina.cn"
            scope = df_role.loc[index_num]['scope']
            role = df_role.loc[index_num]['role']
            cmd_assign = "az role assignment create --assignee " + upn + " --role '" + role + "' --scope " + scope
            os.system(cmd_assign)

if __name__ == "__main__":
    assign_role_by_user()
