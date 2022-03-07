FROM python:3.9

RUN apt-get update \
&& apt-get install -y sudo wget vim fonts-ipaexfont unzip

# Japanese Localization
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime


# google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
apt-get update && \
apt-get install -y google-chrome-stable

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
# wget http://dl.google.com/linux/deb/pool/main/g/google-chrome-unstable/google-chrome-unstable_93.0.4577.18-1_amd64.deb && \
# apt-get install -y -f ./google-chrome-unstable_93.0.4577.18-1_amd64.deb


# ChromeDriver
ADD https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_linux64.zip /opt/chrome/

# ADD https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip /opt/chrome/

RUN cd /opt/chrome/ && \
unzip chromedriver_linux64.zip


COPY requirements.txt .
RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/*


RUN apt-get clean && apt clean && rm -rf /var/lib/apt/lists/*


ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome

WORKDIR /work

CMD bash
