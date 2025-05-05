from flask import Flask
from flask_cors import CORS
import psycopg2
from routes import health_bp, events_bp, subscriptions_bp, users_bp
from database import databaseConnection
from dotenv import find_dotenv, load_dotenv
import sys, os
# from flask_migratepg import MigratePg


app = Flask(__name__)
 
#  database migrations
app.config.from_mapping(
    MIGRATIONS_PATH=os.path.abspath('database/migrations'),
    PSYCOPG_CONNINFO=os.getenv("DATABASE_URL")
)
# migrate
MigratePg(app)

# enable cors
CORS(app)

# load .env variables
if not load_dotenv(find_dotenv()):
    print("Error loading variables from dotenv")
else:
    print(".env file loaded successfully!") 
    

     
# routes/endpoints
app.register_blueprint(health_bp)

# run in debug mode for now
if __name__ == '__main__': 
    app.run(debug=True)
    

