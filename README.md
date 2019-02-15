[![Build Status](https://travis-ci.org/Arrotech/Politico_Api.svg?branch=develop)](https://travis-ci.org/Arrotech/Politico_Api) [![Coverage Status](https://coveralls.io/repos/github/Arrotech/Politico_Api/badge.svg?branch=develop)](https://coveralls.io/github/Arrotech/Politico_Api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/e4c6a7d21481978d93b4/maintainability)](https://codeclimate.com/github/Arrotech/Politico_Api/maintainability)


# Politico API's

This project i am to create a set of API endpoints defined in the API Endpoints Specification
section and use database to store data.


Below are the Endpoints that have been created.

| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| api/v2/auth/signup | Create user| POST |
| api/v2/auth/login | Login to account |GET|


**TOOLS TO BE USED IN THE CHALLENGE**
1. Server-Side Framework:[Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library:[Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide:[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework:[PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Endpoints: [PostMan](https://www.getpostman.com/)
6. Testing Framework:[Coverage, a Python Testing Framework](https://coverage.readthedocs.io/en/v4.5.x/)
 
**Other requirements**

		pip install pytest

		pip install coverage

		pip install nose

		pip install flask

		virtualenv

		Postgres

		Psycopg2-binary

**How to run the application**
 1. Make a new directory on your computer
 2. Do a git init in  the folder
 3. Create virtual environment by typing this in the terminal - virtualenv -p python3 venv
 4. `git clone` this  <code>[repo](https://github.com/Arrotech/Politico_Api/)</code>
 4. run `pip install -r requirements.txt` on the terminal to install the dependencies
 6. Export the environmental variable
 7. Then type on the terminal ```flask run``` to start and run the server
 8. Then on [postman](https://www.getpostman.com/), use the above url's


**Author**

     Harun Gachanja Gitundu


**Contributors to the project**

     Abraham Ogol.

     Brian.

     wilson.

     Mark.