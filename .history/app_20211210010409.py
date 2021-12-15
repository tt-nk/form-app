from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_info = "Username:"
    pass_info = "Password:"

    return render_template('index.html'user_info=user, pass_info=pass_info)


if __name__ == '__main__':
    app.run()
