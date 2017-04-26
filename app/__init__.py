from flask import Flask
from flask_mongoengine import MongoEngine

flaskApp = Flask(__name__)
flaskApp.config.from_object("config")

db = MongoEngine(flaskApp)

from app import views, models