FROM python:3.7.1

WORKDIR /regex_locator

COPY ./requirements.txt .

RUN pip install -r requirements.txt

VOLUME ["/regex_locator"]

