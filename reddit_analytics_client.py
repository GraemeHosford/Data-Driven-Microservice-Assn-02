import random
import time

import grpc
import redis

import redditreader_pb2
import redditreader_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50055") as channel:
        stub = redditreader_pb2_grpc.RedditReaderStub(channel)
        response = stub.getRedditPosts(redditreader_pb2.RedditRequest())

        total_posts = 0
        total_comments = 0
        num_nsfw = 0

        update_time = None

        for item in response:
            print(item.title)
            total_posts += 1
            total_comments += item.num_comments

            if item.nsfw:
                num_nsfw += 1

            try:
                connection = redis.StrictRedis(port=6379)

                if update_time is None or time.time() >= (update_time + 180):
                    update_time = time.time()
                    connection.set("RedditPosts", total_posts)
                    connection.set("RedditComments", total_comments)
                    connection.set("AverageComment", total_comments / total_posts)
                    connection.set("NSFWPercent", (num_nsfw / total_posts) * 100)

                    total_posts = 0
                    total_comments = 0
                    num_nsfw = 0

                # Sleep for random time between 0 and 6 seconds for average of update very 3 seconds
                time.sleep(random.randint(0, 6))
            except Exception as e:
                print("Reddit Analytics Error", e)


if __name__ == "__main__":
    run()
