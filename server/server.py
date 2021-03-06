#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    return "<h1 style='color:blue'>Hello World!</h1>"


@app.route('/api/v1.0/nettool/<path:type>/<path:keyword>', methods=['GET'])
def get_net_tool(type, keyword):
    # print(request.args.get('summary'))
    # print(request.args.get('charge'))
    print(type + keyword)
    if type == "dig" or type == "whois" or type == "ping" and keyword and "." in keyword:
        value = data_from_type(type, keyword)
        return value
    else:
        abort(400)
    return None


def data_from_type(cmd, kwd):
    cmds = [cmd, kwd]
    if cmd == "ping":
        cmds = [cmd, "-c", "3", kwd]
    # value = subprocess.run(cmds, stdout=subprocess.PIPE).stdout
    print(cmds)
    proc = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    value = ''
    for line in proc.stdout:
        value += line.decode() + '\n'
    print(value)
    return value
