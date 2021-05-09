#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:17:44 2021

@author: master
"""

from flask import Flask, request, jsonify
import re
import os
from datetime import datetime
import json

def logging(message, req, code, path, ip):
    now = datetime.now()
    d = now.strftime("%d/%m/%Y:%H:%M:%S")
    log = {"time":d, "ip":ip, "request":req, "path":path, "return":message, "status_code":code}
    if os.path.exists('logs/app.log'):
        with open('logs/app.log', 'a') as f:
            f.write(json.dumps(log) + "\n")
    else:
        with open('logs/app.log', 'w') as f:
            f.write(json.dumps(log) + "\n")
            
app = Flask(__name__)

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    name_list = [m.group(0) for m in matches]
    return " ".join(name_list)

@app.route('/helloworld', methods=['GET'])
def helloword():
    param = request.args.get('name')
    if param == None:
        name = "Stranger"
        path = request.full_path
        ip = request.remote_addr
        logging(f"Hello {name}",request.method, 200, path, ip)
        return f"Hello {name}\n"
    name = camel_case_split(param)
    path = request.full_path
    ip = request.remote_addr
    logging(f"Hello {name}", request.method, 200, path, ip)
    return f"Hello {name}\n", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
