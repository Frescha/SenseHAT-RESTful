import datetime
import os
import sys

from app import app
from flask import Flask, jsonify, request, abort
from sense_hat import SenseHat

sense = SenseHat()

#
# Environmental sensors
#

@app.route('/api/v1/humidity', methods=['GET'])
@require_appkey
def get_humidity():
	humidity = sense.get_humidity()
	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Humidity',
	    unit = 'mbar',
	    data		= humidity
	)

@app.route('/api/v1/temperatur_from_humidity', methods=['GET'])
@app.route('/api/v1/temperatur', methods=['GET'])
@require_appkey
def get_temperaturs():
	temp = sense.get_temperature()
	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Gets the current temperature in degrees Celsius from the humidity sensor.',
	    unit		= 'Celsius',
	    data		= temp
	)

@app.route('/api/v1/temperatur_from_pressure', methods=['GET'])
@require_appkey
def get_temperaturs_from_pressure():
	temp = sense.get_temperature_from_pressure()
	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Gets the current temperature in degrees Celsius from the pressure sensor.',
	    unit		= 'Celsius',
	    data		= temp
	)

@app.route('/api/v1/barometric_pressure', methods=['GET'])
@require_appkey
def get_pressures():
	pressure = sense.get_pressure()
	return jsonify(
	    date		= timeString,
	    explanation = 'Environmental sensor: Pressure; The current pressure in Millibars.',
	    unit		= 'bar',
	    data		= pressure
	)
