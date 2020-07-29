from flask import Flask
import os
import sys
NAME=os.getenv("NAME")
PORT=int(os.getenv("PORT"))
#ENV=os.getenv("ENV")
app=Flask(__name__)


@app.route("/")
def home():
    return f"hello {NAME} test {PORT}"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=PORT, debug=False)