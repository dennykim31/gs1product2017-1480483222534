# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
'''
import json
import http.client, urllib.parse
import pprint
conn = http.client.HTTPConnection("211.174.220.74:8080")
headers = {}
conn.request("GET", "/product/8803451227376.json", headers=headers)
res = conn.getresponse()
data = res.read()
decoded_data = data.decode("utf-8")
dict_data = json.loads(decoded_data)
gsdata = dict_data['data']['product']
'''

def GetPeople():
    list = [  {'id'='gs121'},
        {'type'='agri'},
           {'brand'='1'}]
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
