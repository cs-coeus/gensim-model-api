# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN echo 'deb http://deb.debian.org/debian testing main' >> /etc/apt/sources.list \
    && apt-get update && apt-get install -y --no-install-recommends -o APT::Immediate-Configure=false gcc g++

WORKDIR /app

COPY requirements.txt requirements.txt
COPY .env .env
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install pyemd

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]