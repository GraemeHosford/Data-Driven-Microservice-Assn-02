from concurrent import futures
import pandas as pd
import grpc


def read_in_tweets():
    tweet_data = pd.read_csv("training.1600000.processed.noemoticon.csv", encoding="latin")

    # Giving columns actual names instead of indexes to make using pandas a bit easier
    tweet_data.columns = ["target", "ids", "date", "flag", "user", "text"]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("{::}:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    read_in_tweets()
