FROM python:3.6
RUN apt-get update && apt-get install -y libshout3-dev pkg-config
RUN pip install python-shout soundcloud-lib
RUN pip install jq
COPY streamer.py /streamer.py
COPY poolside.py /poolside.py

CMD python -u /streamer.py
