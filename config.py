import os
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = "PUPM_WROKORDER_DB"
app.config['MONGO_URI'] = "mongodb://localhost:27017/PUMP_WORKORDER_DB"
mongo = PyMongo(app)
