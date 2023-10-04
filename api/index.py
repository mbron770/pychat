from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from database import db
from flask_restful import Api, Resource
import os

DB_URL = os.environ.get('DB_URL')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/api')
def hello():
    return "<p>Hello, World!</p>"

@app.route('/api/create-pets-table')
def create_table():
    
    # try:
    #     return jsonify(message="Your string goes here"), 200
    # except Exception as error:
    #     return jsonify(message="Your string goes here"), 500
    return jsonify(m=DB_URL)


if __name__ == '__main__':
    app.run(debug = True)

