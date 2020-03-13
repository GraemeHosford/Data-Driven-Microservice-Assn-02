# Name: Graeme Hosford
# Student ID: R00147327

import tweetreader_pb2_grpc
import tweetreader_pb2
import time
import random
import redis
import grpc


def run():
    with grpc.insecure_channel('tweet_reader:50051') as channel:
        stub = tweetreader_pb2_grpc.TweetReaderStub(channel)
        response = stub.getTweets(tweetreader_pb2.TweetRequest())

        total_words = 0
        prev_least_words = None
        tweet_least_words = ""

        num_positive = 0
        num_negative = 0
        num_neutral = 0

        sentiment_update_time = None

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
                connection = redis.StrictRedis(host="redis", port=6379)
                connection.set("Total", str(total_words))
                connection.set("LeastWords", tweet_least_words)

                # If 3 minutes have passed since last sentiment update to redis then do that update
                # again give updated values
                if sentiment_update_time is None or time.time() >= (sentiment_update_time + 180):
                    sentiment_update_time = time.time()

                    if num_negative > num_neutral and num_negative > num_positive:
                        connection.set("Sentiment", "Negative")
                    elif num_neutral > num_negative and num_neutral > num_positive:
                        connection.set("Sentiment", "Neutral")
                    else:
                        connection.set("Sentiment", "Positive")

                # Sleep for some time between 0 and 4 seconds for average of 2 seconds
                time.sleep(random.randint(0, 4))
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    run()
