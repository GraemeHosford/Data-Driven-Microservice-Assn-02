from concurrent import futures

import grpc

import redditreader_pb2
import redditreader_pb2_grpc


class RedditReader(redditreader_pb2_grpc.RedditReaderServicer):
    def getRedditPosts(self, request, context):
        file = open("r_dataisbeautiful_posts.csv", "r")

        # Skip Headers
        next(file)

        for line in file:
            line_details = line.split(",")

            # File does not use quotes in rows consistently. Can't find any solution which
            # works to still read these rows correctly. Skipping them to make program work
            if len(line_details) == 12:
                yield redditreader_pb2.RedditInfo(id=line_details[0], title=line_details[1],
                                                  author=line_details[3], num_comments=int(line_details[10]),
                                                  nsfw=line_details[11])
            else:
                continue


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    redditreader_pb2_grpc.add_RedditReaderServicer_to_server(RedditReader(), server)
    server.add_insecure_port("[::]:50055")
    server.start()
    print("Reddit Server started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
