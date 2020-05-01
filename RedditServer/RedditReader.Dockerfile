FROM python:3-stretch

WORKDIR /app

COPY /RedditServer /app
COPY /redditreader_pb2.py /app
COPY /redditreader_pb2_grpc.py /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 50055

CMD ["python", "reddit-reader.py"]
