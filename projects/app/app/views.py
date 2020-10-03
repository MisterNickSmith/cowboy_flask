from flask import Flask
from flask import render_template

app = Flask(__name__)
#why imported from app and not flask? 

@app.route('/')
@app.route('/home') 

bar ={
         "first" : "projects" ,
         "second" : "resume" ,
         "third" : "contact",
       }

def home(): 
  return render_template("base.html", title = "Nick Smith")

@app.projects('/projects')

def projects(): 
  return render_template("projects.html", title = "Projects") 

def contact(): 
  return render_template("contact.html", title = "Contact")







  if __name__ == "__main__":
    app.run(debug=true)



