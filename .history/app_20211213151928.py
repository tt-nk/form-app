import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://form.db'
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
    user_info = "Username:"
    pass_info = "Password:"

    return render_template('index.html', user=user_info, pass_info=pass_info)


@app.route('/main/')
def main():
    return render_template('index.html')


@app.route('/next/')
def next():
    pass


if __name__ == '__main__':
    app.run(debug='True')

    db.create_all()
