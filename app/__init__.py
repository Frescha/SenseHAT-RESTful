from flask import Flask

app = Flask(__name__)

from app import routes
from app import imusensors
from app import environmentalsensors
from app import matrix