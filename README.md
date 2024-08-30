# Flask MongoDB and PostgreSQL App

This is a Flask application template that uses PostgreSQL for relational data and MongoDB for document-based data. The project includes SQLAlchemy and MongoEngine as the ORM/ODM, respectively.

## Features

- Flask
- PostgreSQL with SQLAlchemy
- MongoDB with MongoEngine
- Flask-Migrate for database migrations
- API routes for interacting with MongoDB and PostgreSQL
- Modular structure with blueprints

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8+
- PostgreSQL
- MongoDB
- Virtualenv (optional, but recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/spartan124/flask_boilerplate.git
cd flask_boilerplate
```

### 2. Create a Virtual Environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

```.env
FLASK_DEBUG=True
SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@localhost/xi'
TEST_SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@localhost/testdb'
MONGODB_DB='xi'
MONGODB_HOST='localhost'
MONGODB_PORT= 27017
````

### 5. Initialize Database

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

*Note: You will need to setup postgres on your own and supply the URI. Same goes for MongoDb 

### 6. Run the Application

```bash
flask run
```

### 7. Access the API Docs

<http://127.0.0.1:5000/doc/swagger>
