#!/usr/bin/python3
 
import json
# import pandas as pd

with open('template.json', mode='r') as f:
 
    # 将 JSON 对象转换为 Python 字典
    data2 = json.load(f)

    # print (data2['resources'][0]['properties']['virtualNetworkPeerings'])
    for peer in data2['resources'][0]['properties']['virtualNetworkPeerings']:
        # print(peer['name'])
        # print(peer['properties']['remoteAddressSpace']['addressPrefixes'][0])
        temp_name = peer['properties']['remoteVirtualNetwork']['id'][29:]
        print(temp_name[:-14])
