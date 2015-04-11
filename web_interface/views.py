## @views.py
#   This file contains the corresponding views logic. Specifically, the
#       the route decorators are defined, which flask to execute triggers
#       for specific URL's.
import json
from web_interface import app
from flask import render_template, request
from brain.load_data import Load_Data
from brain.converter.restructure_data import Restructure_Data
from brain.database.retrieve_session import Retrieve_Session
from brain.cache.retrieve_model import Retrieve_Model

## index: render 'index.html'
@app.route('/')
def index():
    return render_template('index.html')

## load_data: return computed data
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
        sender         = Restructure_Data(settings, files)
        data_formatted = sender.restructure()

        # send data to brain
        loader = Load_Data(data_formatted)
        if loader.get_session_type()['session_type']:
            session_type = loader.get_session_type()['session_type']

            if session_type == 'data_new': response = loader.load_data_new()
            elif session_type == 'data_append': response = loader.load_data_append()
            elif session_type == 'model_generate': response = loader.load_model_generate()
            elif session_type == 'model_use': response = loader.load_model_use()
            else: response = loader.get_errors()

        else: response = loader.get_errors()

        # return response
        return json.dumps(response)

## retrieve_session: retrieve all sessions stored in the database
@app.route('/retrieve-session/', methods=['POST', 'GET'])
def retrieve_session():
    if request.method == 'POST':
        # get all sessions
        session      = Retrieve_Session()
        session_list = session.get_all_sessions()

        # return all sessions
        if session_list['result']: return json.dumps(session_list['result'])
        else: return json.dumps({'error': session_list['error']})

## retrieve_model: retrieve all models stored in the hashed redis cache
@app.route('/retrieve_model/', methods=['POST', 'GET'])
def retrieve_model():
    if request.method == 'POST':
        # get all models
        model_list = Retrieve_Models().get_all_models()

        # return all models
        if model_list['result']: return json.dumps(model_list['result'])
        else: return json.dumps({'error': model_list['error']})
