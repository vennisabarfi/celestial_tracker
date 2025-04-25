from flask import Flask
from flask_cors import CORS
import psycopg2
# from dotenv import find_dotenv, load_dotenv
import sys, os
# from flask_migratepg import MigratePg


app = Flask(__name__)


# enable cors
CORS(app)


# run in debug mode for now
if __name__ == '__main__': 
    app.run(debug=True)
    

