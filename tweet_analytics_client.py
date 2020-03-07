# Name: Graeme Hosford
# Student ID: R00147327

import tweetreader_pb2
import tweetreader_pb2_grpc

import grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tweetreader_pb2_grpc.TweetReaderStub(channel)
        response = stub.getTweets(tweetreader_pb2.TweetRequest())

        for item in response:
            print(item.text)


if __name__ == '__main__':
    run()
