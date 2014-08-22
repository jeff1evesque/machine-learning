## index.py
#  This file currently tests the basic implementation of the 'Flask',
#  web-framework.

#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
