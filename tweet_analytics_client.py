# Name: Graeme Hosford
# Student ID: R00147327

import random
import time

import grpc
import redis

import tweetreader_pb2
import tweetreader_pb2_grpc


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

        num_tweets = 0

        sentiment_update_time = None

        for item in response:
            print(item.text)
            tweet_words = len(item.text.split())
            total_words += tweet_words
            num_tweets += 1

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
                connection.set("Tweets." + item.id, "Username: {} - {}".format(item.username, item.text))

                # If 3 minutes have passed since last sentiment update to redis then do that update
                # again give updated values
                if sentiment_update_time is None or time.time() >= (sentiment_update_time + 180):
                    sentiment_update_time = time.time()

                    negative_percent = (num_negative / num_tweets) * 100
                    neutral_percent = (num_neutral / num_tweets) * 100
                    positive_percent = (num_positive / num_tweets) * 100

                    connection.set("SentimentNegative", negative_percent)
                    connection.set("SentimentNeutral", neutral_percent)
                    connection.set("SentimentPositive", positive_percent)

                    # Set all back to 0 so old results aren't affecting further 3 minute metric groups
                    num_negative = 0
                    num_neutral = 0
                    num_positive = 0
                    num_tweets = 0

                # Sleep for some time between 0 and 4 seconds for average of 2 seconds
                time.sleep(random.randint(0, 4))
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    run()
