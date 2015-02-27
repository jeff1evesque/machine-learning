## @app.py
#   This file loads corresponding logic, and html template file(s), which
#       allows the presentation of (asynchronous) content.
from flask import Flask, render_template, request

# Initialize: create flask instance
app = Flask(__name__)

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
  debug=True
)
