FROM ubuntu

RUN apt-get update \
&& apt-get install -y sudo wget vim fonts-ipaexfont \
mecab mecab-ipadic-utf8 libmecab-dev swig

RUN apt update \
&& apt install -y build-essential \
libbz2-dev libdb-dev \
libreadline-dev libffi-dev libgdbm-dev liblzma-dev libncursesw5-dev \
libsqlite3-dev libssl-dev zlib1g-dev uuid-dev

ENV DEBIAN_FRONTEND=noninteractive
RUN apt install -y tk-dev

RUN apt-get clean && apt clean && rm -rf /var/lib/apt/lists/*

## install python3.9
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.9.12/Python-3.9.12.tar.xz \
&& tar xJf Python-3.9.12.tar.xz \
&& rm -f Python-3.9.12.tar.xz

WORKDIR /tmp/Python-3.9.12
RUN ./configure && make && make install

WORKDIR /usr/local/bin
RUN ln -s python3 python && ln -s pip3 pip

RUN mkdir /work
WORKDIR /work

## install Python libraries
RUN pip install --upgrade pip setuptools
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt  && rm -rf /root/.cache/*

## execute jupyterlab as a default command
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]
