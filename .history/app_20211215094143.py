import os
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


class LoginForm(FlaskForm):

    validators = [InputRequired(), Length(
        min=8, max=16, message='8文字以上16文字以内で入力して下さい。')]
    username = StringField('Username', validators)
    password = PasswordField('Password')
    submit = SubmitField('Login')


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/')
def index():
    return render_template('top.html')


@app.route('/main')
# @login_required
def main():
    return render_template('main')


@app.route('/login', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host="localhost", debug=True)
