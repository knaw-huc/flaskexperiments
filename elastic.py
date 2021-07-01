#!/usr/bin/env python3

from os import closerange
import requests
import json

# response  = requests.get("http://localhost:5000/endpoint/")
# print(response.text)

endpoint = "http://localhost:9200/favouritesongs/nummer/" # ElasticSearch endpoint

# a json string must first converted to a dictionary
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

dicdata = json.loads(data) # json-string to dictionary
id = dicdata["id"]
unique_endpoint = endpoint + str(id)
print(unique_endpoint)
headers = {'content-type': 'application/json'}

r = requests.put(unique_endpoint,data = json.dumps(dicdata), headers=headers)

''' test if it succesfull updated posted data '''

response = requests.get(unique_endpoint);
# response.json() obtain a dictionary
json_formatted_str = json.dumps(response.json(), indent=4)
print(json_formatted_str)

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

id = datapythonformat["id"]
unique_endpoint = endpoint + str(id)
print(unique_endpoint)

headers = {'content-type': 'application/json'}

r = requests.put(unique_endpoint,data = json.dumps(datapythonformat), headers=headers)
response = requests.get(unique_endpoint);
# response.json() obtain a dictionary
json_formatted_str = json.dumps(response.json(), indent=4)
print(json_formatted_str)


def dump(json):
    return json.dumps(json, indent=4)


# print(type(response.json()))
# d = response.json()
# print(type(d), d, d['_source']['artiest'])
