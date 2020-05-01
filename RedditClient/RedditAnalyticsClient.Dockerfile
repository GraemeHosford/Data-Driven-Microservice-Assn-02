FROM python:3-stretch

WORKDIR /app

COPY /RedditClient /app
COPY /redditreader_pb2.py /app
COPY /redditreader_pb2_grpc.py /app
COPY /wait-for-it.sh /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "reddit_analytics_client.py"]
