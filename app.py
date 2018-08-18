# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from flask import make_response,Response
import json
from time import time
from os import system
app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/api/take',methods=['GET'])
def api_take():
    timestamp=int(time())
    pic_file_name = "static/images/{0}.jpg".format(timestamp)
    system("fswebcam {0}".format(pic_file_name))
    return "ok"

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=9000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
