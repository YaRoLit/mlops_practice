FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3

RUN apt install -y python3-pip

RUN pip3 install numpy

RUN pip3 install pandas

RUN pip3 install scikit-learn

COPY . /apps

WORKDIR /apps

CMD ["/bin/bash", "pipeline.sh"]
