from flask import Flask, render_template, url_for

app = Flask(__name__)


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        def __getitem__(self):
            return self

    def initials(self):
        return "{},{}.".format(self.firstname[0], self.lastname[1])


@app.route('/')
@app.route('/index')
def index():
    title = 'Test Title'
    user = User('George', 'Spanos')
    return render_template('index.html', title=title, user=user)


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
