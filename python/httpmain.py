import flask
import Chkcourse
import Login
from flask import Flask, request, Response
from flask_cors import CORS
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/', methods=['GET'])

def home():
    name = request.values.get('name')
    uid = request.values.get('uid')
    pwd = request.values.get('pwd')
    if name != None:
        return Response(Chkcourse.findcourse('', name),mimetype='application/json')
    if uid != None and pwd != None:
        return Response(Login.login(uid,pwd),mimetype='application/json')
    return "Please USE API"

app.run(host= '0.0.0.0')
