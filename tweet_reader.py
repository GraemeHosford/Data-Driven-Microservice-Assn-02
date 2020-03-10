from concurrent import futures
import grpc

import tweetreader_pb2
import tweetreader_pb2_grpc

tweet_data = None


class TweetReader(tweetreader_pb2_grpc.TweetReaderServicer):
    def getTweets(self, request, context):
        for line in open("training.1600000.processed.noemoticon.csv", "r"):
            line_details = line.split("\",\"")
            yield tweetreader_pb2.Tweet(target=line_details[0], text=line_details[5].replace("\"", ""),
                                        username=line_details[4])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tweetreader_pb2_grpc.add_TweetReaderServicer_to_server(TweetReader(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
