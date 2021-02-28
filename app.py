from flask import Flask, render_template, url_for
from user import User

app = Flask(__name__)

users = []

@app.route('/')
@app.route('/index')
def index():
    title = 'Test Title'
    user = User('George', 'Spanos')
    return render_template('index.html', title=title, user=user)


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000)
