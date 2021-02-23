from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_pynamodb import PynamoDB

db_mongoengine = MongoEngine()
db_pymongo = PyMongo()
db_pynamodb = PynamoDB()
