from flask import Flask

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
@app.route('/home') 

def home(): 
  return "Hello World!" 

if __name__ == "__main__":
    app.run()


