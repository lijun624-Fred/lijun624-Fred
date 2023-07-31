import os
import json
import pandas as pd

df = pd.read_csv ("_exportglobalusers0713.csv")
user_list = []

def add_display_name():
    cmd_list_guestusers = "az ad user list --filter \"userType eq 'guest'\" --output json"
    result = os.popen(cmd_list_guestusers)
    guestuser_json = result.read()
    guestusers = json.loads(guestuser_json)
    for user in guestusers:
        if str(user['displayName']).find(".") == -1:
            ntname = str(user['displayName']).lower() + "@bosch.com"
            if df['ntname'].str.contains(ntname).any():
                display_name = df.loc [df['ntname'] == ntname, 'email'].item()
                cmd_list_guestusers = "az ad user update --id " + user['id'] + " --display-name " + str(display_name).split("@")[0]
                os.system(cmd_list_guestusers)
                user_list.append(cmd_list_guestusers)
            else:
                print(ntname)

# get the vm token to authenticate to get the secret from key vault, use the secret to login as sp
def get_secret():
    cmd_get_token = "curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.cn' -H Metadata:true"
    token_return = os.popen(cmd_get_token)
    token_json = json.loads(token_return.read())
    cmd_get_secret = "curl 'https://sharezone-keyvault.vault.azure.cn/secrets/useradmin?api-version=2016-10-01' -H \"Authorization: Bearer " + token_json['access_token'] + "\""
    secret_return = os.popen(cmd_get_secret)
    secret_json = json.loads(secret_return.read())
    cmd_login = "az login --service-principal -u 9b4542ab-95f9-4469-9443-2493a31d57f7 -p=" + secret_json['value'] + " --tenant 6a596574-1518-4214-840e-216bb42592e7"
    os.system(cmd_login)

if __name__ == "__main__":
    get_secret()
    add_display_name()
    s = ", ".join(str(x) for x in user_list)
    cmd_sendmail = "echo " + s + "|mail -s \"User rename notification\" fred.li@cn.bosch.com"
    os.system(cmd_sendmail)