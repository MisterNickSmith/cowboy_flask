#python configuratoin file
import os 
class Config(object): 
  SECRET_KEY = "only-I-can-live-forever" 

  basedir = os.path.abspath(os.path.dirname(__file__))

  SQLAlchemy_DATABASE_URI = os.environ.get('DATABASE_URL') or \
'sqlite:///' + os.path.join(basedir, 'app.db')

  SQLAlchemy_TRACK_MODIFICATIONS = False
