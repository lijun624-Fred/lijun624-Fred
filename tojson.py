#!/usr/bin/python3
 
import json
# import pandas as pd

with open('template.json', mode='r') as f:
 
    # 将 JSON 对象转换为 Python 字典
    data2 = json.load(f)
    # print (data2)

    # print (data2['resources'][0]['properties']['virtualNetworkPeerings'])
    for peer in data2['resources'][0]['properties']['virtualNetworkPeerings']:
        print(peer['name'])
        print(peer['properties']['remoteAddressSpace']['addressPrefixes'][0])
    # data_flat = [dict(id=x["id"], **x["properties"]) for x in data2]
    # df = pd.DataFrame(data_flat)
    # print(df)