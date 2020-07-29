from flask import Flask
import os
import sys
#ENV=os.getenv("ENV")
app=Flask(__name__)


@app.route("/")
def home():
    return f"hello test 4000"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000, debug=False)
