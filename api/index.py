from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from database import db
from flask_restful import Api, Resource
import os

DB_URL = os.environ.get('DB_URL')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/create-pets-table')
def create_table():
    
    try:
        return jsonify(message="Your string goes here"), 200
    except Exception as error:
        return jsonify(message="Your string goes here"), 500
    # return "<p>Hello, Worldweewewewewewewew!</p>"




# export DB_URL="postgresql://default:0kfNebo1Twgp@ep-hidden-rain-16108082-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb"
