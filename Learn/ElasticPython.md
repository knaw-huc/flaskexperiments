# ElasticSearch & Python

## Python for a prettier output for json output obtained from curl

    curl http://localhost:9200/favouritesongs/nummer/1 | python -m json.tool

or 


    curl http://localhost:9200/favouritesongs/nummer/1&pretty=true 

But this is only for ElasticSearch, not other api's.



json.dumps(dict) # converts python structures, dictionary or list to json strings
dicdata = json.loads(data) # json-string to dictionary
