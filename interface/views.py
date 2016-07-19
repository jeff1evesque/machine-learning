'''@views

This file contains the corresponding views logic. Specifically, the route
decorators are defined, which flask triggers for specific URL's.

@blueprint, organizes the entire application as a series of modules.

    @endpoint, optional attribute defined within (blueprint) route decorators.
        This allows other functions, within the same flask context, to make
        reference of it, via the 'url_for' method:

            @blueprint.route('/example', methods=['POST'], endpoint='sample')

        can be accessed within the same flask context:

            url_for(name.load_data)

'''

import json
from flask import Blueprint, render_template, request
from brain.load_data import Load_Data
from brain.converter.restructure_settings import Restructure_Settings
from brain.database.retrieve_session import Retrieve_Session
from brain.cache.cache_model import Cache_Model
from brain.cache.cache_hset import Cache_Hset


# local variables
blueprint = Blueprint(
    'name',
    __name__,
    template_folder='interface/templates',
    static_folder='interface/static'
)


@blueprint.route('/')
def index():
    '''@index

    This router function renders the 'index.html' template.

    '''

    return render_template('index.html')


@blueprint.route('/load-data/', methods=['POST'], endpoint='load_data')
def load_data():
    '''@load_data

    This method returns the computed data, resulting from one of the following
    implemented session:

        - data_new
        - data_append
        - model_predict
        - model_generate

    '''

    if request.method == 'POST':

        # load programmatic-interface
        if request.get_json():
            # get necessary components from the dataset
            if 'dataset' in request.get_json():
                dataset = request.get_json()['dataset']
            else:
                dataset = None
            settings = request.get_json()['properties']

            # restructure the dataset
            sender = Restructure_Settings(settings, dataset)
            data_formatted = sender.restructure()

            # send reformatted data to brain
            loader = Load_Data(data_formatted)
            if loader.get_session_type()['session_type']:
                session_type = loader.get_session_type()['session_type']

                if session_type == 'data_new':
                    response = loader.load_data_new()
                elif session_type == 'data_append':
                    response = loader.load_data_append()
                elif session_type == 'model_generate':
                    response = loader.load_model_generate()
                elif session_type == 'model_predict':
                    response = loader.load_model_predict()
                else:
                    response = loader.get_errors()

            else:
                response = loader.get_errors()

            # return response
            return json.dumps(response)

        # load web-interface
        else:
            # local variables
            files = None

            # get uploaded form files
        if request.files:
            files = request.files

        # get submitted form data
        if request.form:
            settings = request.form
            sender = Restructure_Settings(settings, files)
            data_formatted = sender.restructure()

            # send reformatted data to brain
            loader = Load_Data(data_formatted)
            if loader.get_session_type()['session_type']:
                session_type = loader.get_session_type()['session_type']

                if session_type == 'data_new':
                    response = loader.load_data_new()
                elif session_type == 'data_append':
                    response = loader.load_data_append()
                elif session_type == 'model_generate':
                    response = loader.load_model_generate()
                elif session_type == 'model_predict':
                    response = loader.load_model_predict()
                else:
                    response = loader.get_errors()

            else:
                response = loader.get_errors()

            # return response
            return json.dumps(response)


@blueprint.route('/retrieve-session/', methods=['POST'])
def retrieve_session():
    '''@retrieve_session

    This router function retrieves all sessions stored in the database.

    '''

    if request.method == 'POST':
        # get all sessions
        session_list = Retrieve_Session().get_all_sessions()

        # return all sessions
        if session_list['result']:
            return json.dumps(session_list['result'])
        else:
            return json.dumps({'error': session_list['error']})


@blueprint.route('/retrieve-sv-model/', methods=['POST'], endpoint='retrieve_sv_model')
def retrieve_sv_model():
    '''@retrieve_sv_model

    The router function retrieves all models stored in the hashed redis cache.

    '''

    if request.method == 'POST':
        # get all models
        model_list = Cache_Model().get_all_titles('svm_rbf_model')

        # return all models
        if model_list['result']:
            return json.dumps(model_list['result'])
        else:
            return json.dumps({'error': model_list['error']})


@blueprint.route('/retrieve-sv-features/', methods=['POST'], endpoint='retrieve_sv_features')
def retrieve_sv_features():
    '''@retrieve_sv_features

    This router function retrieves the generalized features properties that can
    be expected for any given observation within the supplied dataset.

    @label_list, this value will be a json object, since it was originally
        cached into redis using 'json.dumps'.

    '''

    if request.method == 'POST':
        label_list = Cache_Hset().uncache(
            'svm_rbf_feature_labels',
            request.get_json()['session_id']
        )

        # return all feature labels
        if label_list['result']:
            return json.dumps(label_list['result'])
        else:
            return json.dumps({'error': label_list['error']})
