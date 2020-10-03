from flask import Flask
from flask import render_template, send_from_directory
import os
from flask_blogging import SQLAStorage , BloggingEngine

app = Flask(__name__)
# why imported from app and not flask?

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html", title="Nick Smith")


@app.route("/projects.html")
def projects():
    return render_template("projects.html", title="Projects")


@app.route("/resume.html")
def resume():
    return render_template("resume.html", title="Resume")


@app.route("/contact.html")
def contact():
    return render_template("contact.html", title="Contact")


@app.route("/notes.html")
def notes():
    return render_template("notes.html", title="Notes")


def styling():
    url_for("static", filename="styling.css")


if __name__ == "__main__":
    app.run(debug=true)
