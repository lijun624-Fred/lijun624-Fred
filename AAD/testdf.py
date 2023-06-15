import pandas as pd

df1 = pd.read_csv ("ntaccounts.csv")
user_name = 'fred.li'
if df1['email'].str.contains(user_name).any():
    print("yes")
# ntname = df1.loc [df1['email'] == user_name, 'ntname'].item()
# print(ntname.split ("@")[0] + "_bosch.com#EXT#@boschcn.partner.onmschina.cn")