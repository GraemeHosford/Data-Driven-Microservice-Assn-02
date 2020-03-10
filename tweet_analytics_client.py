# Name: Graeme Hosford
# Student ID: R00147327

from concurrent import futures
import tweetreader_pb2
import tweetreader_pb2_grpc
import tweet_analytics_client_pb2_grpc
import tweet_analytics_client_pb2
import time
import grpc


class TweetAnalyticsClient(tweet_analytics_client_pb2_grpc.TweetAnalyticsClientServicer):
    def getTweets(self, request, context):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = tweetreader_pb2_grpc.TweetReaderStub(channel)
            response = stub.getTweets(tweetreader_pb2.TweetRequest())

            for item in response:
                if "0" in item.target:
                    target = "Negative"
                elif "2" in item.target:
                    target = "Neutral"
                else:
                    target = "Positive"

                yield tweet_analytics_client_pb2.Tweet(target=target, text=item.text, username=item.username)


def run():
    client = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tweet_analytics_client_pb2_grpc.add_TweetAnalyticsClientServicer_to_server(TweetAnalyticsClient(), client)
    client.add_insecure_port("[::]:50052")
    client.start()
    print("Analytics Client Started")
    client.wait_for_termination()


if __name__ == "__main__":
    run()
