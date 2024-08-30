from datetime import timedelta
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()


db = SQLAlchemy()
cors = CORS()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'port': int(os.getenv('MONGODB_PORT'))
    }
    SECRET_KEY = os.getenv('SECRET_KEY')
    
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_SQLALCHEMY_DATABASE_URI')
    MONGODB_SETTINGS = {
        'db': os.getenv('TEST_MONGODB_DB', 'xitestdb'),
        'host': os.getenv('TEST_MONGODB_HOST', 'localhost'),
        'port': int(os.getenv('TEST_MONGODB_PORT', 27017))
    }

authorizations = {
    "Bearer Auth": {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Add a JWT token to the header with ** Bearer &lt;JWT&gt; token to authorize **'
    }
}