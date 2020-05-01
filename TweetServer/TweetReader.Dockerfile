FROM python:3-stretch

WORKDIR /app

COPY /TweetServer /app
COPY /tweetreader_pb2.py /app
COPY /tweetreader_pb2_grpc.py /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 50051

CMD ["python", "tweet_reader.py"]
