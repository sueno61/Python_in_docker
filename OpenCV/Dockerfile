FROM ubuntu

RUN apt-get update \
&& apt-get install -y sudo wget vim fonts-ipaexfont

RUN apt update \
&& apt install -y build-essential \
libbz2-dev libdb-dev \
libreadline-dev libffi-dev libgdbm-dev liblzma-dev libncursesw5-dev \
libsqlite3-dev libssl-dev zlib1g-dev uuid-dev

ENV DEBIAN_FRONTEND=noninteractive
RUN apt install -y tk-dev

RUN apt-get clean && apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tar.xz \
&& tar xJf Python-3.8.12.tar.xz \
&& rm -f Python-3.8.12.tar.xz

WORKDIR /tmp/Python-3.8.12
RUN ./configure && make && make install

WORKDIR /usr/local/bin
RUN ln -s python3 python && ln -s pip3 pip

RUN mkdir /work
WORKDIR /work

# install library
RUN pip install --upgrade pip setuptools
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt  && rm -rf /root/.cache/*


# RUN apt-get update && apt-get install libxcb-xinerama0

# execute jupyterlab as a default command
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]
