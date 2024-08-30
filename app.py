# app/__init__.py
from flask import Flask, request, render_template
from flask_restx import Api
from flask_migrate import Migrate
from mongoengine import connect, disconnect

from config import Config, authorizations, db, cors
from blueprints.users import api as user_ns
from blueprints.posts import api as post_ns

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
cors.init_app(app)
# Initialize Flask-Migrate
migrate = Migrate(app, db)  # Add this line

def connect_db():
    connect('xi', host='localhost', port=27017)


def disconnect_db():
    disconnect()


connect_db()


api = Api(app, version='1.0', title='Chat API',
          description='A simple Flask API',
          authorizations=authorizations,
          security='Bearer Auth',
           doc='/doc/swagger', 
           prefix='/api')


api.add_namespace(user_ns, path='/users')
api.add_namespace(post_ns, path='/posts')


if __name__ == '__main__':
    app.run(debug=True)
    