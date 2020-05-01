import random
import time

import grpc
import redis

import redditreader_pb2
import redditreader_pb2_grpc


def run():
    with grpc.insecure_channel("reddit-reader:50055") as channel:
        stub = redditreader_pb2_grpc.RedditReaderStub(channel)
        response = stub.getRedditPosts(redditreader_pb2.RedditRequest())

        total_posts = 0
        total_comments = 0
        num_nsfw = 0

        for item in response:
            print(item.title)
            total_posts += 1
            total_comments += item.num_comments

            # Checking NSFW this way as using bool(nsfw_string) in reddit-reader.py was
            # always giving true when string was not empty
            if item.nsfw.lower().replace("\n", "") == "true":
                num_nsfw += 1

            try:
                connection = redis.StrictRedis(host="redis", port=6379)
                connection.set("RedditPosts", total_posts)
                connection.set("RedditComments", total_comments)
                connection.set("RedditPost." + item.id, "Title: {}\nAuthor: {}\nNum Comments: {}\nNSFW: {}\n"
                               .format(item.title, item.author, item.num_comments, item.nsfw))

                connection.set("AverageComment", total_comments / total_posts)
                connection.set("NSFWPercent", (num_nsfw / total_posts) * 100)

                # Sleep for random time between 0 and 4 seconds for average of update very 2 seconds
                time.sleep(random.randint(0, 4))
            except Exception as e:
                print("Reddit Analytics Error", e)


if __name__ == "__main__":
    run()
