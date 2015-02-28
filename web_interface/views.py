## @views.py
#   This file contains the corresponding views logic. Specifically, the
#       the route decorators are defined, which flask to execute triggers
#       for specific URL's.
from web_interface import app
from flask import render_template, request
from brain.load_data import Load_Data
from brain.converter.converter_data import Convert_Data

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/load-data/', methods=['POST', 'GET'])
def load_data():
  if request.method == 'POST':
    # local variables
    files = None

    # get post data
    if request.files:
      files = request.files
    settings = request.form

    # format post data
    sender         = Convert_Data(settings, files)
    data_formatted = sender.format()

    # send data to brain
    loader = Load_Data(data_formatted)
    if loader.check_json():
      session_type = loader.get_session_type()

      if session_type == 'data_new': response = loader.load_data_new()
      elif session_type == 'data_append': response = loader.load_data_append()
      elif session_type == 'model_generate': response = loader.load_model_generate()
      elif session_type == 'model_use': response = loader.load_model_use()
      else: response = loader.get_errors()

    else: response = loader.get_errors()

    # return response
    return response

@app.route('/retrieve-session/', methods=['POST', 'GET'])
def retrieve_session():
  if request.method == 'POST':
    # get all sessions
    session      = Retrieve_Session()
    session_list = session.get_all_sessions()

    # return all sessions
    if session_list['result']: return session_list['result']
    else: return session_list['error']
