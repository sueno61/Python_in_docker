FROM python:3.8

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/*

# ENTRYPOINT ["streamlit"]
# CMD ["hello"]
# EXPOSE 8501

WORKDIR /src
