from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

start_time = time.time()


@app.route("/")
def index():
    return "Hello World"


@app.route("/info")
def info():
    data = {
        "app": "Hello DevOps World",
        "author": "MrGyu",
        "version": "1.0.0"
    }
    return jsonify(data)


@app.route("/egeszseg")
def egeszseg():
    uptime_seconds = int(time.time() - start_time)
    return f"OK - uptime: {uptime_seconds} másodperc"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
