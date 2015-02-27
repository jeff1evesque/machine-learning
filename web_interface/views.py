## @views.py
#   This file contains the corresponding views logic. Specifically, the
#       the route decorators are defined, which flask to execute triggers
#       for specific URL's.
from web_interface import app
from flask import render_template, request

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/load-data/', methods=['POST', 'GET'])
def load_data():
  if request.method == 'POST':
    if request.files: files = request.files
    settings = request.form
