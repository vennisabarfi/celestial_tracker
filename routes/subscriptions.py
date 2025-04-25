from flask import Flask, request, jsonify, Blueprint
# from database import databaseConnection
import psycopg2

subscriptions_bp = Blueprint("subscriptions_bp", __name__)