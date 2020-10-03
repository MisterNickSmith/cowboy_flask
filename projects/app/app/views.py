from flask import Flask
from flask import render_template

app = Flask(__name__)
#why imported from app and not flask? 

@app.route('/')
@app.route('/home') 



def home(): 
#  bar = { 'first' : 'projects' ,   'second' : 'resume' ,'third' : 'contact'}
  return render_template("base.html", title = "Nick Smith")
@app.route('/projects')

def projects(): 
  return render_template("projects.html", title = "Projects") 
@app.route('/resume')
def resume(): 
  return render_template("resume.html", title= "Resume")
@app.route('/contact')
def contact(): 
  return render_template("contact.html", title = "Contact")


def styling():
 url_for( 'static', filename="styling.css")







if __name__ == "__main__":
    app.run(debug=true)



