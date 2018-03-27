import datetime
import os
import sys

from app import app
from flask import Flask, jsonify, request, abort

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

now = datetime.datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M")

#
# General Informations
#

@app.route('/api/v1/', methods=['GET'])
def get_apiversion():

	return jsonify(
	    date		= timeString,
	    explanation = 'Gerneral Information: API Version v1.0',
	    unit		= 'None',
	    data		= '1.0'
	)