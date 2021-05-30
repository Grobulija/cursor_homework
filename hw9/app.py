from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

rome = pytz.timezone('Europe/Rome')
format = '%d.%m.%Y %H:%M:%S %Z%z'

@app.route("/")
def main():
    return "Welcome!"


@app.route('/time')
def time():
    time = datetime.now(rome)
    return time.strftime(format)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
