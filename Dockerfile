FROM python:3.6
RUN apt-get update && apt-get install -y libshout3-dev pkg-config
RUN pip install python-shout soundcloud-lib
COPY streamer.py /streamer.py
CMD python /streamer.py

