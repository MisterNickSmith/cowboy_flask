from flask import Flask 
import os 
from flask_sqlalchemy import SQLAlchemy
from flask_blogging import SQLAStorage, BloggingEngine
import config 
from datetime import datetime
from views import app

db = SQLAlchemy(app)

class Note(db.Model):
   date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, primary_key=True) 
   post= db.Column(db.Text, nullable=False) 

   def __repr__(self): 
    return f"Note('{self.date}')"
   


