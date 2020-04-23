FROM ubuntu:latest
RUN apt-get update
RUN apt-get install python3-pip -y
RUN apt-get install mysql-server -y
RUN apt-get install libmysqlclient-dev -y
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
CMD ["python3", "backend.py" ]
