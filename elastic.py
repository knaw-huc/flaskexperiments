#!/usr/bin/env python3

import requests
import json

# response  = requests.get("http://localhost:5000/endpoint/")
# print(response.text)

endpoint = "http://localhost:9200/favouritesongs/nummer/1" # elastic search

data = '''
{
    "artiest" : "Skrillex",
    "nummer" : "First of the Year",
    "opmerking" : "Metal synths,",
    "inbrenger" : "mp",
    "volgnummer": "9"
}    
'''
# https://www.youtube.com/watch?v=2cXDgFwE13g


dicdata = json.loads(data)
print(type(dicdata), dicdata)

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

# r = requests.post(endpoint, data=json.dumps(dicdata), headers=headers)

r = requests.put(endpoint,data = json.dumps(dicdata), headers=headers)

response = requests.get(endpoint);

print(type(response), response, response.json())

