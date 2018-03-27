import datetime
import os
import sys

from app import app
from flask import Flask, jsonify, request, abort
from sense_hat import SenseHat

sense = SenseHat()

#
# Matrix
#	