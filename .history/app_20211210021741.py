from flask import Flask, render_template

app = Flask(__name__)


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
