import datetime
import os
import sys

from app import app
from flask import Flask, jsonify, request, abort
from sense_hat import SenseHat

sense = SenseHat()

#
# IMU Sensor
#				

@app.route('/api/v1/orientation_radians/', methods=['GET'])
@require_appkey
def get_orientation_radians():
	orientation_rad = sense.get_orientation_radians()
	return jsonify(
	    date		= timeString,
	    pitch		= "{pitch}".format(**orientation_rad),
	    roll		= "{roll}".format(**orientation_rad),
	    yaw			= "{yaw}".format(**orientation_rad),
	    explanation = 'IMU sensor: Gets the current orientation in radians using the aircraft principal axes of pitch, roll and yaw.',
	    data		= "p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad)
	)

@app.route('/api/v1/orientation_degrees/', methods=['GET'])
@app.route('/api/v1/orientation/', methods=['GET'])
@require_appkey
def get_orientation_degrees():
	orientation = sense.get_orientation_degrees()
	return jsonify(
	    date		= timeString,
	    pitch		= "{pitch}".format(**orientation),
	    roll		= "{roll}".format(**orientation),
	    yaw			= "{yaw}".format(**orientation),
	    explanation = 'IMU sensor: Gets the current orientation in degrees using the aircraft principal axes of pitch, roll and yaw.',
	    data		= "p: {pitch}, r: {roll}, y: {yaw}".format(**orientation)
	)

@app.route('/api/v1/compass/', methods=['GET'])
@require_appkey
def get_compass():
	north = sense.get_compass()
	return jsonify(
	    date		= timeString,
	    explanation = 'IMU sensor: The direction of North.',
	    data		= north
	)

@app.route('/api/v1/compass_raw/', methods=['GET'])
@require_appkey
def get_compass_raw():
	raw = sense.get_compass_raw()
	return jsonify(
	    date		= timeString,
	    x			= "{x}".format(**raw),
	    y			= "{y}".format(**raw),
	    z			= "{z}".format(**raw),
	    explanation = 'IMU sensor: Gets the raw x, y and z axis magnetometer data.',
	    data		= "x: {x}, y: {y}, z: {z}".format(**raw)
	)

@app.route('/api/v1/gyroscope/', methods=['GET'])
@require_appkey
def get_gyroscope():
	gyro_only = sense.get_gyroscope()
	return jsonify(
	    date		= timeString,
	    pitch		= "{pitch}".format(**gyro_only),
	    roll		= "{roll}".format(**gyro_only),
	    yaw			= "{yaw}".format(**gyro_only),
	    explanation = 'IMU sensor: Calls set_imu_config to disable the magnetometer and accelerometer then gets the current orientation from the gyroscope only.',
	    data		= "p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only)
	)

@app.route('/api/v1/gyroscope_raw/', methods=['GET'])
@require_appkey
def get_gyroscope_raw():
	raw = sense.get_gyroscope_raw()
	return jsonify(
	    date		= timeString,
	    x			= "{x}".format(**raw),
	    y			= "{y}".format(**raw),
	    z			= "{z}".format(**raw),
	    explanation = 'IMU sensor: Gets the raw x, y and z axis gyroscope data.',
	    data		= "x: {x}, y: {y}, z: {z}".format(**raw)
	)

@app.route('/api/v1/accelerometer/', methods=['GET'])
@require_appkey
def get_accelerometer():
	accel_only = sense.get_accelerometer()
	return jsonify(
	    date		= timeString,
	    pitch		= "{pitch}".format(**accel_only),
	    roll		= "{roll}".format(**accel_only),
	    yaw			= "{yaw}".format(**accel_only),
	    explanation = 'IMU sensor: Calls set_imu_config to disable the magnetometer and gyroscope then gets the current orientation from the accelerometer only.',
	    data		= "p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only)
	)

@app.route('/api/v1/accelerometer_raw/', methods=['GET'])
@require_appkey
def get_accelerometer_raw():
	raw = sense.get_accelerometer_raw()
	return jsonify(
	    date		= timeString,
	    x			= "{x}".format(**raw),
	    y			= "{y}".format(**raw),
	    z			= "{z}".format(**raw),
	    explanation = 'Gets the raw x, y and z axis accelerometer data.',
	    data		= "x: {x}, y: {y}, z: {z}".format(**raw)
	)