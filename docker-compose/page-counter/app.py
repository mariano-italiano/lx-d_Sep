from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def count():
    redis.incr('hits')
    number = redis.get('hits').decode('utf-8')
    return "Hey, you visited this page " + number + " time(s)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
