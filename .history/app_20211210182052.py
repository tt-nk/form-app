from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


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
