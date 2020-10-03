from flask import Flask

app = Flask(__name__)
#why imported from app and not flask? 
import app.views


#@app.route('/')
#@app.route('/home') 

#def home(): 
#  return "Hello World!" 




