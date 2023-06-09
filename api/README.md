# Kilega Api

The project demonstrate to use of [Flask](https://flask.palletsprojects.com/en/2.2.x/) micro framework for the creation of `Kilega Service API`

## Features
- Use Flask with [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
- Database integration with Flask SQLAlchemy
- Authentication with JWT
- Enviroment Seperation 
- Error handing with Werkzeug
- API documentation with SwaggerUI and Flask-RESTX
- Unit testing 
- Database Migration
## Routes to Implement
| Method | Route | Functionality |Access|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/auth/login/``` | _Login user_|_All users_|
| *GET* | ```/docs/``` | _View API documentation_|_All users_|

## Python Packages
1. [Flask](https://flask.palletsprojects.com/en/2.2.x/)
2. [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
3. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
4. [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
5. [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
6. [Python-decouple](https://pypi.org/project/python-decouple/)
7. [Pytest](https://docs.pytest.org/en/7.2.x/)

## Running the project 
### Requirements
- Python 3.9.5 or higher
- Requirements text file
- Access to GitHub repository
- Linux/MacOs/Windows Operating System (OS)
### Step 1:
Clone the project reposity
```
git clone https://github.com/arcticline-platform/Kilega.git
```
### Step 2:
Change directory to project folder, create a virtual environment and activate it

```
$ cd Kilega/api
$ python -m venv env
$ source env/bin/activate
```

### Step 3:
Install all the required dependencies
```
$ pip install -r requirements.txt
```
Run the project in development
```
$ export FLASK_APP=src/
$ export FLASK_DEBUG=1
$ Flask run
```
----
```
python runserver.py