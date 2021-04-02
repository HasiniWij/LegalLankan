#!flask/bin/python
from flask import Flask
from flaskrun import flaskrun
from flask import render_template

application = Flask(__name__)


@application.route('/', methods=['GET'])
@application.route('/hello/')
@application.route('/hello/<name>')
def hello(name=None):
    # return '{"Output":"Hello World"}'
    return render_template('hello.html', name=name)


@application.route('/', methods=['POST'])
def post():
    return '{"Output":"Hello World"}'

if __name__ == '__main__':
    flaskrun(application)
