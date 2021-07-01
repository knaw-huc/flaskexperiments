#!/usr/bin/env python3

import requests
import json

# response  = requests.get("http://localhost:5000/endpoint/")
# print(response.text)

endpoint = "http://localhost:9200/favouritesongs/nummer/" # elastic search

data = '''
{
    "id": 1,
    "artiest" : "Skrillex",
    "nummer" : "First of the Year",
    "opmerking" : "Metal synths,",
    "inbrenger" : "mp",
    "volgnummer": 9,
    "url": "https://www.youtube.com/watch?v=2cXDgFwE13g"
}    
'''

# https://www.youtube.com/watch?v=2cXDgFwE13g


datapythonformat = {
    "id" : 2,
    "artiest" : "The Boswell Sisters",
    "nummer" : "Crazy People",
    "jaar" : 1932,
    "opmerking" : "Voorloper Andrew Sisters",
    "inbrenger" : "mp",
    "volgnummer": 13,
    "url": "https://www.youtube.com/watch?v=R-O5U4uuPF8"
}




dicdata = json.loads(data) # json-string to dictionary
print(dicdata)
id = dicdata["id"]
endpoint += str(id)

# json.dumps(dict) converts python structures, dictionary or list to json

headers = {'content-type': 'application/json'}


r = requests.put(endpoint,data = json.dumps(dicdata), headers=headers)

response = requests.get(endpoint);

# print(type(response), response, response.json())

print(response.json())
