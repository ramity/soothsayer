FROM debian:stretch

MAINTAINER Lewis Brown "github.com/ramity"

ADD . /var/flask
WORKDIR /var/flask

RUN apt-get update
RUN apt-get upgrade
RUN apt-get dist-upgrade
RUN apt-get autoremove

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN apt-get install -y chromium
RUN apt-get install -y chromedriver

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000
CMD python3 manage.py run -h 0.0.0.0
