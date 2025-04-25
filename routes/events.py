from flask import Flask, request, jsonify, Blueprint
# from database import databaseConnection
import psycopg2

events_bp = Blueprint("events_bp", __name__)