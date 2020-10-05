from flask import Flask 
import datetime
import os 

from sqlalchemy import create_engine , Column, Table, String, DateTime, Text, MetaData
from flask_blogging import SQLAStorage, BloggingEngine
import config 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from views import app


engine = create_engine('sqlite:///vault.db')

meta= MetaData()


# create a session object using sessionmaker method to add config with engine
Session = sessionmaker(bind=engine)

#creation of a session
session = Session()

#base class from which all other classes are derived
Base = declarative_base()

Note = Table( 
      'note', meta,
 
    Column('date', DateTime, nullable=False, primary_key=True),
    Column('title', String, nullable=False),
    Column('post', Text, nullable=False) ,
)
   






   


