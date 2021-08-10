# flask_web/app.py
from flask import Flask, render_template
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


api = Api(app)


with app.app_context():
    from routes.todo import *
    from routes.weather import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
