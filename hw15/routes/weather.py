from flask import Flask, render_template, request, jsonify, Response
import requests
from app import app
from config import Config


@app.route('/weather', methods=['GET'])
def weather():
    return render_template("homepage.html")


def qsmake(q, cnt, mode, lon, lan, type, lat, units):
    return {"q": q, "cnt": cnt, "mode": mode, "lon": lon, "type": type, "lat": lat,
            "units": units}


def make_response(querystring):
    url = Config.WEATHER_API_URL

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    return requests.request("GET", url, headers=headers, params=querystring)


def good_response(response):
    data = response.json()
    weather = data['list'][0]
    return render_template("weather.html", weather=weather)


def bad_response():
    return Response(status=404)


@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get("city")
    querystring = qsmake(city, "1", "null", "", "link, accurate", "", "metric")

    response = make_response(querystring)
    if response.status_code == 200:
        return good_response(response)

    return bad_response()
