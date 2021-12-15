import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20))


@app.route('/')
def index():
    return render_template('signup.html')


@app.route('/menber')
def index():
    return render_template('menber.html')


@app.route('/login')
def index():
    return render_template('login.html')


@app.route('/logout')
def index():
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(debug='True')
