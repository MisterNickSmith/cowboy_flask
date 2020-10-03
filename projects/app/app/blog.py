from flask import Flask 
import os 
from Flask-Squlalchemy import SQLAlchemy
from flask_blogging import SQLAStorage, BloggingEngine
from app import config 

db = SQlAlchemy(app) 
storage = SQLAStorage(db=db) 
db.create_all()



