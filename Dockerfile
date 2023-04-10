FROM python:3.11

ENV HOME /root
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
