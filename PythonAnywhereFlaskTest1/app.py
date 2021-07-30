from flask import Flask, url_for,render_template, Blueprint
from markupsafe import escape

app = Flask(__name__)

bp = Blueprint("app1", __name__)

@bp.route('/')
def hello_testing():
    return "<p>Hello, testing!</p>"

@bp.route('/hello/')
def hello_world():
    return "<p>Hello, World!</p>"

@bp.route("/123/")
def numbers():
    return "<p>A number</p>"

@bp.route("/<val1>/<val2>")
def custom_input(val1, val2):
    return "<p>val1: {}, val2: {}</p>".format(escape(val1),escape(val2))


@bp.route("/sum/<val1>/<val2>")
def sum_two_values(val1, val2):
    try:
        val1 = int(val1)
        val2 = int(val2)
        return "<p>{} + {} = {}</p>".format(escape(val1),escape(val2), escape(int(val1)+int(val2)))
    except ValueError as e:
        return "Error: one value was not an integer"

@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'



@bp.route('/hello/<name>')
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


if __name__ == '__main__':
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(bp)
    app.run()
