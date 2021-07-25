from flask import Flask, url_for,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/123")
def numbers():
    return "<p>A number</p>"


@app.route("/<val1>/<val2>")
def custom_input(val1, val2):
    return "<p>val1: {}, val2: {}</p>".format(escape(val1),escape(val2))


@app.route("/sum/<val1>/<val2>")
def sum_two_values(val1, val2):
    try:
        val1 = int(val1)
        val2 = int(val2)
        return "<p>{} + {} = {}</p>".format(escape(val1),escape(val2), escape(int(val1)+int(val2)))
    except ValueError as e:
        return "Error: one value was not an integer"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

def form():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method

#with app.test_request_context():
#    print(url_for('static', filename='style.css'))
#    print(url_for('hello_world'))
#    print(url_for('custom_input', val1= 'hello', val2 = 'world'))
#    print(url_for('numbers', next='/'))
#    print(url_for('profile', username='John Doe'))
