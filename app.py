from flask import Flask, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    if(name is not None):
        name = name[0].capitalize() + name[1:]
    else: 
        name = "R"
    return render_template("index.html", name=name )
    # return jsonpersoon

@app.route('/endpoint/') # trailing slash is essential
def endpoint():
    persons = [{"name": "M", "age": 57, "mood": "heavy"}, {"name": "R", "age": 62, "mood": "light"}]
    jsonpersons = json.dumps(persons)
    return jsonpersons


if __name__ == "__main__":
    app.run(debug=True)