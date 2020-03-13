# Name: Graeme Hosford
# Student ID: R00147327

import tweetreader_pb2
import tweetreader_pb2_grpc
import time
import random
import redis
import grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tweetreader_pb2_grpc.TweetReaderStub(channel)
        response = stub.getTweets(tweetreader_pb2.TweetRequest())

        total_words = 0
        prev_least_words = None
        tweet_least_words = ""

        num_positive = 0
        num_negative = 0
        num_neutral = 0

        for item in response:
            tweet_words = len(item.text.split())
            total_words += tweet_words

            if prev_least_words is None or tweet_words < prev_least_words:
                tweet_least_words = item.text
                prev_least_words = tweet_words

            if "0" in item.target:
                num_negative += 1
            elif "2" in item.target:
                num_neutral += 1
            else:
                num_positive += 1

            try:
                connection = redis.StrictRedis(port=6379)
                connection.set("Total", str(total_words))
                connection.set("LeastWords", tweet_least_words)

                if num_negative > num_neutral and num_negative > num_positive:
                    connection.set("Sentiment", "Negative")
                elif num_neutral > num_negative and num_neutral > num_positive:
                    connection.set("Sentiment", "Neutral")
                else:
                    connection.set("Sentiment", "Positive")

                # Printing tweet values to console as a basic logging while testing
                print(item.text)

                # Sleep for some time between 0 and 4 seconds for average of 2 seconds
                time.sleep(random.randint(0, 4))
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    run()
