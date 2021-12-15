import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

"""login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20))"""


class LoginForm(FlaskForm):
    validators = [InputRequired()]
    username = StringField('ユーザー名', validators)
    password = PasswordField('パスワード')


@app.route('/signup', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
