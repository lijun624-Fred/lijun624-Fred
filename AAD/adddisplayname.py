import os
import json
import pandas as pd

df = pd.read_csv ("_exportglobalusers.csv")

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
                print(cmd_list_guestusers)
            else:
                print(ntname)

if __name__ == "__main__":
    add_display_name()
