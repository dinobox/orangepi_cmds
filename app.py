# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from flask import make_response,Response
import json
from time import time
from os import system

from pyA20.gpio import gpio
from pyA20.gpio import port as pin
gpio.init()
#设置 PA7 为输出
gpio.setcfg(pin.PA7, gpio.OUTPUT)

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

@app.route('/api/power/pa7/on',methods=['GET'])
def api_power_pa7_on():
    gpio.output(pin.PA7, gpio.HIGH)
    return "ok"


@app.route('/api/power/pa7/off',methods=['GET'])
def api_power_pa7_off():
    gpio.output(pin.PA7, gpio.LOW)
    return "ok"

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=9000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
