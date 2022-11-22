#!/usr/bin/python3
 
import json

f = open('template.json', mode='r')
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(f)
print (data2)
