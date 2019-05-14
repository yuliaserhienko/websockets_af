FROM python:3.7

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt