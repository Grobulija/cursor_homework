# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
import json
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api
import requests
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get("city")
    querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                   "units": "metric"}

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        weather = data['list'][0]
        return render_template("weather.html", weather=weather)

    return Response(status=404)


api = Api(app)

todos = {}


class Todo(Resource):

    def get(self, todo_id):
        try:
            with open('data/todo_' + str(todo_id) + '.json', 'r') as read_file:
                data = json.load(read_file)
            read_file.close()
        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        todos[todo_id] = request.json.get('text')
        data = {todo_id: todos[todo_id]}
        with open('data/todo_' + str(todo_id) + '.json', 'w') as write_file:
            json.dump(data, write_file)
        write_file.close()
        return data

    def delete(self, todo_id):
        del todos[todo_id]
        return Response(todos, status=204)


class TodoList(Resource):

    def get(self):
        return todos

    def post(self):
        todos[request.json.get('todo_id', None)] = request.json.get('text', "")
        return todos


class Weather(Resource):

    def get(self):
        url = Config.WEATHER_API_URL

        cities = request.args.get('city')
        querystring = {"q": cities}

        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.text
            return data

        return Response(status=404)


api.add_resource(Weather, '/weather')
api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
