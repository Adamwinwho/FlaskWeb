from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField("what is your name?",validators=[Required()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    form = NameForm()
    return render_template("index.html",form=form)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html",name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == "__main__":
    app.run(debug=True)
    #manager.run()
