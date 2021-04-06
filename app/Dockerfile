FROM ubuntu:18.04

WORKDIR /usr/app

RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update

RUN apt install python3.6
RUN apt install -y python3-pip
RUN python3 -m pip install wheel
RUN python3 -m pip install scikit-build
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install cmake


RUN python3 -m pip install opencv-contrib-python
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install x11-xserver-utils -y
RUN python3 -m pip install pymysql
RUN python3 -m pip install Flask
#RUN xhost +
COPY ./ ./
CMD ["python3","test.py"]


