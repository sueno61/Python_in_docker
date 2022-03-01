FROM python:3.8

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/*

WORKDIR /site

ENV FLASK_ENV=development
ENV FLASK_APP=app

# CMD flask run
CMD bash
