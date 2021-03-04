import flask
import Chkcourse
import Login
import goCourse

from flask import Flask, request, Response
from flask_cors import CORS
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = False
CORS(app)

@app.route('/', methods=['GET'])

def home():
    name = request.values.get('name')
    uid = request.values.get('uid')
    pwd = request.values.get('pwd')
    couid = request.values.get('couid')
    gogo = request.values.get('gogo')
    if name != None:
        return Response(Chkcourse.findcourse('', name),mimetype='application/json')
    elif couid != None and gogo == '1':
        return Response(goCourse.gogoCourse(couid,uid,pwd),mimetype='application/json')
    elif uid != None and pwd != None:
        return Response(Login.login(uid,pwd),mimetype='application/json')
    return "Please USE API"

app.run(host= '0.0.0.0',port= '5002',ssl_context=('cert.pem', 'privkey.pem'))
