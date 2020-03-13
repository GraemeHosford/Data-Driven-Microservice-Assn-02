# Name: Graeme Hosford
# Student ID: R00147327

from flask import Flask
import redis

app = Flask(__name__)


@app.route('/')
def show_tweets():
    output = ""

    try:
        connection = redis.StrictRedis(port=6379, decode_responses=True)
        for key in connection.scan_iter("Total"):
            value = connection.get(key)

            # Using regex to make number in format b'XYZ' appear as just XYZ
            output += "Number of words globally:\t" + value + "<br/>"

        for key in connection.scan_iter("LeastWords"):
            value = connection.get(key)
            output += "Tweet with the least number of words:\t" + value + "<br/>"

        for key in connection.scan_iter("Sentiment"):
            value = connection.get(key)
            output += "Sentiment in the last 3 minutes:\t" + value + "<br/>"

        return output
    except Exception as e:
        print("Error", e)
        return "An error has occurred when reading data from redis"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
