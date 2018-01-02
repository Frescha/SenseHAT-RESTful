#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, abort
from functools import wraps
from random import randint

import datetime
import os
#import ssl

#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.load_cert_chain('server.crt', 'server.key')

now = datetime.datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M")
config=None

app = Flask(__name__)

if config is None:
	config = os.path.join(app.root_path, '../etc/emulator.cfg')
	app.config.from_pyfile(config)

# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
    	key=app.config['SECRET_APIKEY']
        #with open('api.key', 'r') as apikey:
            #key=apikey.read().replace('\n', '')
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


@app.route('/api/v1/', methods=['GET'])
def get_apiversion():

	return jsonify(
	    date		= timeString,
	    explanation = 'Gerneral Information: API Version v1.0',
	    unit		= 'None',
	    data		= '1.0'
	)

#
# Environmental sensors
#

@app.route('/api/v1/humidity', methods=['GET'])
@require_appkey
def get_humidity():
	
	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Humidity',
	    unit = 'float',
	    data		= randint(0, 35)
	)

@app.route('/api/v1/temperatur_from_humidity', methods=['GET'])
@app.route('/api/v1/temperatur', methods=['GET'])
@require_appkey
def get_temperaturs():
	
	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Gets the current temperature in degrees Celsius from the humidity sensor.',
	    unit		= 'Celsius',
	    data		= randint(0, 35)
	)

@app.route('/api/v1/temperatur_from_pressure', methods=['GET'])
@require_appkey
def get_temperaturs_from_pressure():
	
	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Gets the current temperature in degrees Celsius from the pressure sensor.',
	    unit		= 'Celsius',
	    data		= randint(0, 35)
	)

@app.route('/api/v1/barometric_pressure', methods=['GET'])
@require_appkey
def get_pressures():

	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Pressure; The current pressure in Millibars.',
	    unit		= 'bar',
	    data		= randint(0, 1000)
	)

#
# IMU Sensor
#				

@app.route('/api/v1/gyroscope/', methods=['GET'])
@require_appkey
def get_gyroscope():

	return jsonify(
	    date		= timeString,
	    explanation = 'gyroscope',
	    data		=  randint(0, 9)
	)

@app.route('/api/v1/accelerometer', methods=['GET'])
@require_appkey
def get_accelerometer():

	return jsonify(
	    date		= timeString,
	    explanation = 'Accelerometer',
	    data		= randint(0, 59)
	)


@app.route('/api/v1/magnetometer', methods=['GET'])
@require_appkey
def get_magnetometer():

	return jsonify(
	    date		= timeString,
	    explanation = 'Just a explanation',
	    data		= '16'
	)






# 8x8 LED Matrix

@app.route('/api/v1/ledmatrix/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
	app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])