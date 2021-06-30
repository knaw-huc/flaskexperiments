from flask import Flask,request, make_response, flash, render_template, redirect
from flask_cors import CORS
from flask.json import jsonify

from flask.helpers import url_for

import json

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = './static/uploads/'
app.secret_key = 'secreet' # for flash() session
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 # max: 1MB, 10s ogg = 125MB, mp4 = 233MB, webm = 48MB


@app.route('/')
@app.route('/<name>')
def index(name=None):
    if(name is not None):
        name = name[0].capitalize() + name[1:]
    else: 
        name = "R"
    return render_template("index.html", name=name )
    # return jsonpersoon



@app.route('/data', methods=['GET']) # need the method if immediately after unslashed route
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    name = request.args.get('name')
    return name
    # print(user)

@app.route('/endpoint/') # trailing slash is essential
def endpoint():
    status = "OK"
    bashcmd = "fmpeg converted"
    returnvalue = 0
    returnvalues = [{"storestatus" : status}, {"mp4conv" : {"bashcmd" : bashcmd, "return" : returnvalue}}]
    return json.dumps(returnvalues), {'Content-Type': 'Application/json; charset=utf-8'}

    # return json.dumps(returnvalues)

@app.route('/createquestion/')
def createquestion():
    return render_template("audioquestion.html", a=1)


@app.route('/submit/', methods = ['POST', 'GET']) # start slash and end slash essential
def submit():
    id = None
    dictOfWords = []
    if request.method == 'POST' and 'id' in request.form:
        id = request.form['id']
        words = request.form['words']
        wordslist = words.split(',')

        for idx, val in enumerate(wordslist):
            print(idx)
            phrase = {"id" : idx + 1, "phrase": val}
            dictOfWords.insert(len(dictOfWords), phrase)
            
        app.logger.info(dictOfWords)


        # jason = jsonify(dictOfWords)
        jason = json.dumps(dictOfWords,indent=4)
        # https://docs.python.org/3/library/json.html

        # return jason # for test


    elif request.method == 'GET' and 'id' in request.args: # for easy test
        id = request.args['id']
    
    flash('prrr... ' + words)

    if id is None:
        return "nothing subsmithed"
    else:    
        return redirect(url_for('createquestion'))
        
        # return 'form subsmithed, you can collect your .lsq with id: ' + id + 'file on '
        r = make_response(render_template("limesurvey_choosewords.lsq", id=id, dictOfWords=jason))
        r.headers.set('Content-Type', 'text/xml; charset=utf-8')
        r.headers.set('Content-Disposition', 'attachment; filename="limesurveyquestion.lsq"')
        # return render_template("limesurvey_choosewords.lsq", id=id)
        return r

 
    return redirect(url_for('uploadwordlist'))

@app.route('/upload/',  methods = ['GET'])
def upload():
    return render_template("upload.html", a=1)

 

@app.route('/processupload/',  methods = ['POST'])
def processupload():
    # app.logger.info(request.files) 
  
    uploaded_file = request.files['file']
    

    if uploaded_file.filename != '':
        safename = app.config['UPLOAD_FOLDER'] + uploaded_file.filename
        # safename = uploaded_file.filename

        uploaded_file.save(safename)
        flash(uploaded_file.filename + ' succesfull stored')

    return redirect(url_for('upload'))




@app.route('/getphrases/')
def getphrases():
    file = open('static/testjsons/quiz.json', 'r');
    content = file.read()
    return content, {'Content-Type': 'Application/json; charset=utf-8'}


if __name__ == "__main__":
    app.run(debug=True)
    