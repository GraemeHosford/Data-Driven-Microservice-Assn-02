FROM python:3-stretch

WORKDIR /app

COPY /TweetClient /app
COPY /tweetreader_pb2.py /app
COPY /tweetreader_pb2_grpc.py /app
COPY /wait-for-it.sh /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "tweet_analytics_client.py"]
