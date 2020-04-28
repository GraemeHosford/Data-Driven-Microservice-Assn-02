# Name: Graeme Hosford
# Student ID: R00147327

import redis
from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_tweets():
    output = "<table style=\"border:1px solid black;float:left;\" width=\"42%\">"

    try:
        connection = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
        for key in connection.scan_iter("Total"):
            value = connection.get(key)

            output += "<tr><td><strong>Number of words globally:</strong>\t" + value + "</td></tr>"

        for key in connection.scan_iter("LeastWords"):
            value = connection.get(key)
            output += "<tr><td><strong>Tweet with the least number of words:</strong>\t" + value + "</td></tr>"

        for key in connection.scan_iter("SentimentNegative"):
            value = connection.get(key)
            output += "<tr><td><strong>Negative sentiment in the last 3 minutes:</strong>\t" + value + "%</td></tr>"

        for key in connection.scan_iter("SentimentNeutral"):
            value = connection.get(key)
            output += "<tr><td><strong>Neutral sentiment in the last 3 minutes:</strong>\t" + value + "%</td></tr>"

        for key in connection.scan_iter("SentimentPositive"):
            value = connection.get(key)
            output += "<tr><td><strong>Positive sentiment in the last 3 minutes:</strong>\t" + value + "%</td></tr>"

        for key in connection.scan_iter("Tweets.*"):
            value = connection.get(key)
            output += "<tr><td>" + value + "</td></tr>"

        output += "</table>"

        output += "<table style=\"border:1px solid red;float:right;\" width=\"40%\">"

        for key in connection.scan_iter("RedditPosts"):
            value = connection.get(key)
            output += "<tr><td><strong>Total number of Reddit posts globally: </strong>" + value + "</td></tr>"

        for key in connection.scan_iter("RedditComments"):
            value = connection.get(key)
            output += "<tr><td><strong>Total number of comments across all posts globally: </strong>" + \
                      value + "</td></tr>"

        for key in connection.scan_iter("AverageComment"):
            value = connection.get(key)
            output += "<tr><td><strong>Average number of comments per post: </strong>" + \
                      value + "</td></tr>"

        for key in connection.scan_iter("NSFWPercent"):
            value = connection.get(key)
            output += "<tr><td><strong>Percent of posts which are NSFW: </strong>" + \
                      value + "</td></tr>"

        for key in connection.scan_iter("RedditPost.*"):
            value = connection.get(key)
            output += "<tr><td>" + value + "</td></tr>"

        output += "</table>"

        return output
    except Exception as e:
        print("Error", e)
        return "An error has occurred when reading data from redis"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
