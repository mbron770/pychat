from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from http.server import BaseHTTPRequestHandler
from database import db
# from flask_restful import Api, Resource
from flask_cors import CORS
from models import User
import os
# os.system("pip install flask-migrate")

app = Flask(__name__)
CORS(app)
# DB_URL = os.environ.get('DB_URL')
DB_URL="postgresql://default:0kfNebo1Twgp@ep-hidden-rain-16108082.us-east-1.postgres.vercel-storage.com:5432/verceldb"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)

class handler(BaseHTTPRequestHandler):
    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header('Content-type','text/plain')
    #     self.end_headers()
    #     self.wfile.write('Hello, world!'.encode('utf-8'))
    #     return
    
    @app.route("/api/python")
    def hello_world():
        return "<p>Hello, World!</p>"

# @app.route('/api')
# def hello():
#     return "<p>Hello, World!</p>"

# @app.route('/api/test',  methods = ['GET', 'PATCH'])
# def test():
#     if(request.method == 'GET'):
#         all = User.query.all()
#         users = []
#         for user in all:
#             users.append(str(user))
#         return jsonify(users), 200


    if __name__ == '__main__':
        app.run()

