#python configuratoin file
import os 
class Config(object): 
  SECRET_KEY = "only-I-can-live-forever" 

  basedir = os.pasth.abspath(os.path.dirname(__file__))

  SQLAlchemy_DATABASE_URI = os.environ.get('DATABASE_URL')

  SQLAlchemy_TRACK_MODIFICATIONS = False
