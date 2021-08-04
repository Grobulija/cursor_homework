# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
import requests
from config import Config

app = Flask(__name__)


def qsmake(q, cnt, mode, lon, lan, type, lat, units):
    return {"q": q, "cnt": cnt, "mode": mode, "lon": lon, "type": type, "lat": lat,
            "units": units}


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    weather = []
    cities = request.form.get("cities")
    cities = cities.replace(" ", "")
    cities_req = cities.split(",")
    for city in cities_req:

        querystring = qsmake(city, "1", "null", "", "link, accurate", "", "metric")

        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST
        }

        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            try:
                weather.append(data['list'][0])
            except(IndexError,):
                return Response(status=404)

        else:
            return Response(status=404)
    return render_template("weather.html", weather=weather)


@app.route('/search_by_ll', methods=['POST'])
def search_weather_by_ll():
    weather = []
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    querystring = qsmake("", "1", "null", lon, "link, accurate", lat, "metric")

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    data = response.json()

    if response.status_code == 200:
        weather.append(data['list'][0])
        return render_template("weather.html", weather=weather)
    return Response(status=404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
