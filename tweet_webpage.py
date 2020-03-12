# Name: Graeme Hosford
# Student ID: R00147327

from flask import Flask
import grpc
import redis

app = Flask(__name__)


@app.route('/')
def show_tweets():
    output = ""
    with grpc.insecure_channel("localhost:50052") as channel:
        try:
            connection = redis.StrictRedis(port=6379)
            for key in connection.scan_iter("*"):
                value = connection.get(key)
                output += str(key) + str(value) + "<br/>"
            return output
        except Exception as e:
            print("Error", e)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
