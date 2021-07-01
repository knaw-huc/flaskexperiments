#!/usr/bin/env python3

import requests
import json

endpoint = "http://localhost:9200/favouritesongs/nummer/" # ElasticSearch endpoint
headers = {'content-type': 'application/json'}

file = open('data.json', 'r');
content = file.read()
dict = json.loads(content)
# print(dict)

for index in range(len(dict)):
    id = dict[index]["id"]
    # print(index, id)
    dicdata = dict[index]
    unique_endpoint = endpoint + str(id)
    # print(unique_endpoint)
    r = requests.put(unique_endpoint,data = json.dumps(dicdata), headers=headers)


''' show all records '''

response = requests.get("http://localhost:9200/favouritesongs/nummer/_search");
# response.json() obtain a dictionary
json_formatted_str = json.dumps(response.json(), indent=4)
print(json_formatted_str)

'''
Or with curl: curl http://localhost:9200/favouritesongs/nummer/_search?pretty
'''