FROM python:3.8

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/*

WORKDIR /site

ENV FLASK_RUN_PORT=5001
ENV FLASK_ENV=development

ENV FLASK_APP=app

# CMD flask run --host=0.0.0.0 
# CMD bash
