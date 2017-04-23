'''

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
from brain.converter.settings import Settings
from brain.database.model_type import ModelType
from brain.database.session import Session
from brain.cache.model import Model
from brain.cache.hset import Hset
from brain.validator.password import validate_password
from brain.database.account import Account
from brain.database.prediction import Prediction
from brain.converter.crypto import hash_pass, verify_pass


# local variables
blueprint = Blueprint(
    'name',
    __name__,
    template_folder='interface/templates',
    static_folder='interface/static'
)


@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def index(path):
    '''

    This router function renders the 'index.html' template, for all requests,
    which do not have corresponding route definitions.

    Note: http://flask.pocoo.org/snippets/57/

    '''

    return render_template('index.html')


@blueprint.route('/load-data', methods=['POST'], endpoint='load_data')
def load_data():
    '''

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
            sender = Settings(settings, dataset)
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
            return response

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
            sender = Settings(settings, files)
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
            return response


@blueprint.route('/login', methods=['POST'])
def login():
    '''

    This router function attempts to fulfill a login request. During its
    attempt, it returns a json string, with two values:

        - username, user attempting to login
        - integer, codified indicator of login attempt:
            - 0, successful login
            - 1, username does not exist
            - 2, username does not have a password
            - 3, supplied password does not match stored password

    '''

    if request.method == 'POST':
        # local variables
        username = request.form.getlist('user[login]')[0]
        password = request.form.getlist('user[password]')[0]
        account = Account()

        # validate: check username exists
        if (
            account.check_username(username)['result'] and
            account.get_uid(username)['result']
        ):

            # database query: get hashed password, and userid
            hashed_password = account.get_password(username)['result']
            uid = account.get_uid(username)['result']

            # notification: verify hashed password exists
            if hashed_password:

                # notification: verify password
                if verify_pass(str(password), hashed_password):
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


@blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    '''

    This route function returns the status of the '/logout' request:

        - 0, indicates successful logout
        - 1, indicates unsuccessful logout

    '''

    if request.method in ['GET', 'POST']:
        # remove session
        session.pop('uid', None)

        # indicate whether user logged out
        if session.get('uid'):
            return json.dumps({'status': 1})
        else:
            return json.dumps({'status': 0})


@blueprint.route('/register', methods=['POST'])
def register():
    '''

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
        account = Account()

        # validate requirements: one letter, one number, and ten characters.
        if (validate_password(password)):

            # validate: unique username
            if not account.check_username(username)['result']:

                # validate: unique email
                if not account.check_email(email)['result']:

                    # database query: save username, and password
                    hashed = hash_pass(str(password))
                    result = Account().save_account(
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
    '''

    This router function retrieves all sessions stored in the database.

    '''

    if request.method == 'POST':
        # get all sessions
        session_list = Session().get_all_sessions()

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
    '''

    The router function retrieves all models stored in the hashed redis cache.

    '''

    if request.method == 'POST':
        # get all models
        svm_list = Model().get_all_titles('svm_model')
        svr_list = Model().get_all_titles('svr_model')
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
    '''

    This router function retrieves the generalized features properties that can
    be expected for any given observation within the supplied dataset.

    @label_list, this value will be a json object, since it was originally
        cached into redis using 'json.dumps'.

    '''

    # get model type
    model_id = request.get_json()['model_id']
    model_type = ModelType().get_model_type(model_id)['result']

    # return all feature labels
    if request.method == 'POST':
        label_list = Hset().uncache(
            model_type + '_feature_labels',
            model_id
        )

        if label_list['result']:
            return json.dumps(label_list['result'])
        else:
            return json.dumps({'error': label_list['error']})


@blueprint.route(
    '/retrieve-prediction-titles',
    methods=['POST'],
    endpoint='retrieve_prediction_titles'
)
def retrieve_prediction_titles():
    '''

    This router function retrieves all prediction titles, stored via the
    'save_prediction' router function. During its attempt, it returns a json
    string, with the following value:

        - integer, codified indicator of database query:
            - 0, successful retrieval of prediction titles
            - 1, unsuccessful retrieval of prediction titles
        - string, array of prediction titles

    '''

    if request.method == 'POST':
        if request.form:
            # local variables
            results = request.form
            args = json.loads(results['args'])
            model_type = args['model_type']

            # query database
            prediction = Prediction()
            response = prediction.get_all_titles(model_type)

            # return results
            if response['status']:
                return json.dumps({
                    'status': 0,
                    'titles': response['result']
                })

            else response['status']:
                return json.dumps({
                    'status': 1,
                    'titles': None
                })


@blueprint.route(
    '/retrieve-prediction',
    methods=['POST'],
    endpoint='retrieve_prediction'
)
def retrieve_prediction():
    '''

    This router function retrieves all prediction parameters.

        - integer, codified indicator of save attempt:
            - 0, successfully stored the prediction result
            - 1, unsuccessfully stored the prediction result
            - 2, status was not 'valid'
            - 3, no form data supplied
        - string, array of prediction titles

    '''

    if request.method == 'POST':
        if request.form:
            # local variables
            results = request.form
            args = json.loads(results['args'])
            id_result = args['id_result']
            model_type = args['model_type']

            # query database and return results
            prediction = Prediction()

            if model_type == 'svm':
                result = prediction.get_result(id_result, model_type)
                classes = prediction.get_value(id_result, model_type, 'class')
                df = prediction.get_value(id_result, model_type, 'decision_function')
                prob = prediction.get_value(id_result, model_type, 'probability')

                if result['status']:
                    return json.dumps({
                        'status': 0,
                        'result': result,
                        'classes': classes,
                        'decision_function': df,
                        'probability': prob
                    })
                else:
                    return json.dumps({'status': 1})

            elif model_type == 'svr':
                coefficient = prediction.get_value(id_result, model_type, 'r2')

                if result['status']:
                    return json.dumps({
                        'status': 0,
                        'r2': coefficient
                    })
                else:
                    return json.dumps({'status': 1})


@blueprint.route(
    '/save-prediction',
    methods=['POST'],
    endpoint='save_prediction'
)
def save_prediction():
    '''

    This router function saves the prediction results generated from a computed
    svm or svr prediction session.  During its attempt, it returns a json
    string, with the following value:

        - integer, codified indicator of save attempt:
            - 0, successfully stored the prediction result
            - 1, unsuccessfully stored the prediction result
            - 2, status was not 'valid'
            - 3, no form data supplied

    '''

    if request.method == 'POST':
        if request.form:
            # local variables
            results = request.form
            data = json.loads(results['data'])
            status = results['status']
            type = results['type']
            title = results['prediction_name']

            # save prediction
            if status == 'valid':
                prediction = Prediction()
                result = prediction.save(data, type, title)['result']

                # notification: prediction status
                if result:
                    return json.dumps({'status': 0})
                else:
                    return json.dumps({'status': 1})

            # notification: status not valid
            else:
                return json.dumps({'status': 2})

        # notification: no form data
        return json.dumps({'status': 3})
