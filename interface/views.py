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
from flask import Blueprint, render_template, request, session
from brain.load_data import Load_Data
from brain.converter.restructure_settings import Restructure_Settings
from brain.database.retrieve_model_type import Retrieve_Model_Type as M_Type
from brain.database.retrieve_session import Retrieve_Session
from brain.cache.cache_model import Cache_Model
from brain.cache.cache_hset import Cache_Hset
from brain.validator.validate_password import validate_password
from brain.database.retrieve_account import Retrieve_Account
from brain.database.save_account import Save_Account
from brain.converter.crypto import hashpass, verifypass


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


@blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


@blueprint.app_errorhandler(405)
def method_not_allowed(e):
    return render_template('index.html'), 405


@blueprint.route('/load-data', methods=['POST'], endpoint='load_data')
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


@blueprint.route('/login', methods=['POST'])
def login():
    '''@login

    This router function attempts to fulfill a login request. During its
    attempt, it returns a json string, with two values:

        - boolean, inidicates if account exists
        - integer, codified indicator of registration attempt:
            - 0, successful login
            - 1, username does not exist
            - 2, username does not have a password
            - 3, supplied password does not match stored password

    '''

    if request.method == 'POST':
        # local variables
        username = request.form.getlist('user[login]')[0]
        password = request.form.getlist('user[password]')[0]
        account = Retrieve_Account()
        uid = account.get_uid(username)['result']

        # validate: check username exists
        if account.check_username(username)['result']:

            # database query: get hashed password
            hashed_password = account.get_password(username)['result']

            # notification: verify hashed password exists
            if hashed_password:

                # notification: verify password
                if verifypass(str(password), hashed_password):
                    # set session: uid corresponds to primary key, from the
                    #              user database table, and a unique integer
                    #              representing the username.
                    session['uid'] = uid

                    # return user status
                    return json.dumps({
                        'status': 0,
                        'username': username
                    })
                else:
                    return json.dumps({
                        'status': 3,
                        'username': username
                    })

            # notification: user does not have a password
            else:
                return json.dumps({
                    'status': 2,
                    'username': username
                })

        # notification: username does not exist
        else:
            return json.dumps({
                'status': 1,
                'username': username
            })


@blueprint.route('/logout', methods=['POST'])
def logout():
    '''

    This route function returns the status of the '/logout' request:

        - 0, indicates successful logout
        - 1, indicates unsuccessful logout

    '''

    if request.method == 'POST':
        # remove session
        session.pop('uid', None)

        # indicate whether user logged out
        if session['uid']:
            return json.dumps({'status': 1})
        else:
            return json.dumps({'status': 0})


@blueprint.route('/register', methods=['POST'])
def register():
    '''@register

    This router function attempts to register a new username. During its
    attempt, it returns a json string, with three possible values:

        - integer, codified indicator of registration attempt:
            - 0, successful account creation
            - 1, password doesn't meet minimum requirements
            - 2, username already exists in the database
            - 3, email already exists in the database
            - 4, internal database error
        - username, string value of the user
        - email, is returned if the value already exists in the database, or
            the registration process was successful

    '''

    if request.method == 'POST':
        # local variables
        username = request.form.getlist('user[login]')[0]
        email = request.form.getlist('user[email]')[0]
        password = request.form.getlist('user[password]')[0]
        account = Retrieve_Account()

        # validate requirements: one letter, one number, and ten characters.
        if (validate_password(password)):

            # validate: unique username
            if not account.check_username(username)['result']:

                # validate: unique email
                if not account.check_email(email)['result']:

                    # database query: save username, and password
                    hashed = hashpass(str(password))
                    result = Save_Account().save_account(
                        username,
                        email,
                        hashed
                    )

                    # notification: attempt to store account
                    if result:
                        return json.dumps({
                            'status': 0,
                            'username': username,
                            'email': email
                        })

                    else:
                        return json.dumps({
                            'status': 4,
                            'username': username,
                        })

                # notification: email already exists
                else:
                    return json.dumps({
                        'status': 3,
                        'username': username,
                        'email': email
                    })

            # notification: account already exists
            else:
                return json.dumps({
                    'status': 2,
                    'username': username
                })

        # notification: password doesn't meet criteria
        else:
            return json.dumps({
                'status': 1,
                'username': username
            })


@blueprint.route('/retrieve-session', methods=['POST'])
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


@blueprint.route(
    '/retrieve-sv-model',
    methods=['POST'],
    endpoint='retrieve_sv_model'
)
def retrieve_sv_model():
    '''@retrieve_sv_model

    The router function retrieves all models stored in the hashed redis cache.

    '''

    if request.method == 'POST':
        # get all models
        svm_list = Cache_Model().get_all_titles('svm_model')
        svr_list = Cache_Model().get_all_titles('svr_model')
        svm_result = []
        svr_result = []
        error_result = []

        # get svm model(s)
        if svm_list['result']:
            svm_result = svm_list['result']
        elif svm_list['error']:
            error_result.extend(svm_list['error'])

        # get svr model(s)
        if svr_list['result']:
            svr_result = svr_list['result']
        elif svr_list['error']:
            error_result.extend(svr_list['error'])

        # return combined model(s)
        combined_result = svm_result + svr_result
        if combined_result:
            return json.dumps(combined_result)
        elif error_result:
            return json.dumps({'error': error_result})


@blueprint.route(
    '/retrieve-sv-features',
    methods=['POST'],
    endpoint='retrieve_sv_features'
)
def retrieve_sv_features():
    '''@retrieve_sv_features

    This router function retrieves the generalized features properties that can
    be expected for any given observation within the supplied dataset.

    @label_list, this value will be a json object, since it was originally
        cached into redis using 'json.dumps'.

    '''

    # get model type
    model_id = request.get_json()['model_id']
    model_type = M_Type().get_model_type(model_id)['result']

    # return all feature labels
    if request.method == 'POST':
        label_list = Cache_Hset().uncache(
            model_type + '_feature_labels',
            model_id
        )

        if label_list['result']:
            return json.dumps(label_list['result'])
        else:
            return json.dumps({'error': label_list['error']})
