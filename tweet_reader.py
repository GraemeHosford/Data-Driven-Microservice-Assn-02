from concurrent import futures
import pandas as pd
import grpc
import time

import tweetreader_pb2
import tweetreader_pb2_grpc


tweet_data = None


class TweetReader(tweetreader_pb2_grpc.TweetReaderServicer):
    def getTweets(self, request, context):
        yield tweetreader_pb2.Tweet(target="target1", text="Text1", username="User1")
        yield tweetreader_pb2.Tweet(target="target2", text="Text2", username="User2")


def read_in_tweets():
    global tweet_data
    tweet_data = pd.read_csv("training.1600000.processed.noemoticon.csv", encoding="latin")

    # Giving columns actual names instead of indexes to make using pandas a bit easier
    tweet_data.columns = ["target", "ids", "date", "flag", "user", "text"]


def serve():
    read_in_tweets()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tweetreader_pb2_grpc.add_TweetReaderServicer_to_server(TweetReader(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
