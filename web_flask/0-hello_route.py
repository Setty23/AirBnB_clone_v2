#!/usr/bin/python3
"""
The script thats te web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """
    Function Docs
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
