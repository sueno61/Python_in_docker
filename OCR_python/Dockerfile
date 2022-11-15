FROM python:3.8

RUN apt update && apt install -y \
tesseract-ocr libtesseract-dev tesseract-ocr-jpn 

RUN apt install -y libopencv-dev

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/*

WORKDIR /Projects
