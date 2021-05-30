FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python python3-pip
COPY requirements.txt /opt/
COPY app.py /opt/
RUN pip install -r requirements.txt
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
