# luistersessie

```
curl -H 'Content-Type:application/json' -XPUT 'http://localhost:9200/luistersessies/nummer/1' -d ' 
{
    "artiest" : "Dua Lupa",
    "nummer" : "Don'\''t start now",
    "opmerking" : "= neo disco",
    "inbrenger" : "mp",
    "volgnummer": "14",

    "luistersessie": {
        "datum" : "2020-04-12",
        "thema" : "Escapisme",
        "deelnemers" : ["mp", "cs", "jn", "wo"],
        "opmerking" : ["escapisme", "zoomsessie"],
        "youtubelink" : "https://www.youtube.com/playlist?list=PLcwvEHzWCITjAEoewh7FnMj2MCnzlRMtU"

    }
}'


curl -X GET -H 'Content-Type: application/json' http://localhost:9200/luistersessies/nummer/_search?pretty -d '{
      "query" : {
        "match" : { "artiest": "Dua" }
    }
}'


curl -H 'Content-Type:application/json' -XGET 'http://localhost:9200/luistersessies/nummer/1'
of
curl  'http://localhost:9200/luistersessies/nummer/1'


krijg je alles:
curl  'http://localhost:9200/luistersessies/nummer/_search'

query lite:
curl  'http://localhost:9200/luistersessies/nummer/_search?q=arties=vic'

```

## Opmerkingen

De single quote in "Don't" verreist nogal een belachelijke manier van escapen, in de shell, om het in Elastic Search te krijgen.
https://stackoverflow.com/questions/32122586/curl-escape-single-quote

Zoeken naar Du werkt niet... Per woord geindexeeerd?

Is die herhaling wenselijk bij noSQL? Elke nummer is een 'document' luistersessie info. Of is een hele luistersessie document.

```
curl -H 'Content-Type:application/json' -XPUT 'http://localhost:9200/luistersessies/nummer/2' -d ' 
{
    "artiest" : ["Vic Fontaine", "James Darren"],
    "nummer" : "It'\''s only a paper moon",
    "opmerking" : ["recursief escapisme", "DS9 S07E10"],
    "inbrenger" : "mp",
    "volgnummer": 6,

    "luistersessie": {
        "datum" : "2020-04-12",
        "thema" : "Escapisme",
        "deelnemers" : ["mp", "cs", "jn", "wo"],
        "opmerking" : ["escapisme", "zoomsessie"],
        "youtubelink" : "https://www.youtube.com/playlist?list=PLcwvEHzWCITjAEoewh7FnMj2MCnzlRMtU"

    }
}'


```