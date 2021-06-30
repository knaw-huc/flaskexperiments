
# elasticSearch


## DATA ERIN

Data erin stoppen, 3 personen:
curl <HEADER> <METHOD> <DATA>

https://stackoverflow.com/questions/47544966/content-type-header-application-x-www-form-urlencoded-is-not-supported-on-elas

Die header moet er wel bij. Oude tutorials laten deze weg en dan krijg je foutmeldingen.

```
 curl -H 'Content-Type: application/json'  -XPUT 'http://localhost:9200/personen/figuur/1' -d  ' {
"first_name" : "Jane",
"last_name": "Smith",
"age" : 32,
"about" : "I like to collect rock albums", "interests": [ "music" ]
}'

curl -H'Content-Type:application/json' -PUT 'http://localhost:9200/personen/figuur/7' -d ' 

{
"first_name" : "Maarten",
"last_name": "van der Peet",
"age" : 57,
"about": "I used to like music", "interests": [ "nothing" ]
}'

curl -H'Content-Type:application/json' -XPUT 'http://localhost:9200/personen/figuur/2' -d ' 
{
"email":"john@smith.com",
"first_name":"John",
"last_name":"Smith",
"info":{
"bio":"Unknown",
"age":50,
"interests":["flowers","birds"]
},
"join_date":"1940/05/10"
}'
```



## ZOEKEN

Op id, index/type/id in de url
```
curl -H 'Content-Type: application/json'  -XGET 'http://localhost:9200/personen/figuur/7'
```


XGET hoeft niet en voor het ophalen ook Content-Type niet meegeven, zelfs GET hoeft niet (default)
```
curl 'http://localhost:9200/personen/figuur/7'
```

### Algemeen zoeken

    curl -XGET 'http://localhost:9200/personen/figuur/_search'

### Specifiek zoeken
```
curl -X GET "localhost:9200/personen/figuur/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": { }
  },
  "fields": [
    "first_name"
  ]
}
'


curl -X GET -H 'Content-Type: application/json' http://localhost:9200/personen/figuur/_search?pretty -d '{
      "query" : {
        "match" : { "first_name": "Maarten" }
    }
}'

curl -X GET -H 'Content-Type: application/json' http://localhost:9200/personen/figuur/_search?pretty -d '{
      "query" : {
        "match" : { "info":{
"bio":"Unknown"}
    }
}'


curl -XGET "http://localhost:9200/personen/figuur/_search?q=last_name:Peet"
```

## DELETE

curl -XDELETE 'http://localhost:9200/personen/figuur/1'



