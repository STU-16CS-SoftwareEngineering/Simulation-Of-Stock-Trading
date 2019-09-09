# -*- coding: utf-8 -*-


from flask import Flask


import mysql.connector
import time


app = Flask(__name__)


from app import routes
from app import getaction
