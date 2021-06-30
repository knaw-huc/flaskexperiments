# Learn


## response headers content types

https://stackoverflow.com/questions/11773348/python-flask-how-to-set-content-type

https://stackoverflow.com/questions/29464276/add-response-headers-to-flask-web-app

## File download

https://coding.tools/blog/force-file-download-instead-of-opening-in-browser-using-http-header-and-flask

## Jinja2

https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript


## WEIRD

### Observations  

In JINJA2

        let phrases = {{ dictOfWords|tojson }};

In Flask

becomes:
      let phrases = [{"id": 1, "phrase": "koud"}, {"id": 2, "phrase": "warm"}, {"id": 3, "phrase": "kil"}];

And is converted by LimeSurvey at the importing stage.

But seemingly:
      let phrases = [{ "id": 1, "phrase": "koud" }, { "id": 2, "phrase": "warm" }, { "id": 3, "phrase": "kil" }]; 

## python -m pip vs pip

https://snarky.ca/why-you-should-use-python-m-pip/

Maar alleen 1 keer bij het maken van een virtual env


## Requests from the client

https://docs.python-requests.org/en/master/user/quickstart/

