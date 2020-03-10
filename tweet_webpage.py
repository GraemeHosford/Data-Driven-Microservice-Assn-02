# Name: Graeme Hosford
# Student ID: R00147327

from flask import Flask
import tweet_analytics_client_pb2
import tweet_analytics_client_pb2_grpc
import grpc

app = Flask(__name__)


@app.route('/')
def show_tweets():
    output = ""
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = tweet_analytics_client_pb2_grpc.TweetAnalyticsClientStub(channel)
        response = stub.getTweets(tweet_analytics_client_pb2.TweetRequest())

        for item in response:
            output += item.target + " - " + item.text + " - " + item.username + "<br>"

            return output


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
