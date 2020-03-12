# Name: Graeme Hosford
# Student ID: R00147327

import tweetreader_pb2
import tweetreader_pb2_grpc
import time
import redis
import grpc


def run():
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

            try:
                connection = redis.StrictRedis(port=6379)
                data_string = "{} - {} - {}".format(target, item.text, item.username)
                connection.set(item.id, data_string)
                print(item.text)
                time.sleep(1)
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    run()
