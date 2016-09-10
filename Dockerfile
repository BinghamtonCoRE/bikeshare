FROM ubuntu:16.04
MAINTAINER Akash Kothawale <akash@decached.com>
RUN apt-get update -y && \
    apt-get -y install \
    build-essential git python3 python3-dev python3-pip nodejs npm nodejs-legacy
RUN npm install -g bower

RUN mkdir /code
WORKDIR /code

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY bower.json .bowerrc ./
RUN bower install --allow-root
COPY ./ ./

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "app:app"]
