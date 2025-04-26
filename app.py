from flask import Flask
from flask_cors import CORS
import psycopg2
from routes import health_bp, events_bp, subscriptions_bp, users_bp
from database import databaseConnection
# from dotenv import find_dotenv, load_dotenv
import sys, os
# from flask_migratepg import MigratePg


app = Flask(__name__)


# enable cors
CORS(app)


# routes/endpoints
app.register_blueprint(health_bp)

# run in debug mode for now
if __name__ == '__main__': 
    app.run(debug=True)
    

