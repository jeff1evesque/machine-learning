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
import pickle
from flask import Blueprint, render_template, request, session
from brain.load_data import Load_Data
from brain.converter.settings import Settings
from brain.database.model_type import ModelType
from brain.database.session import Session
from brain.cache.model import Model
from brain.cache.hset import Hset
from brain.validator.password import validate_password
from brain.validator.email import isValidEmail
from brain.database.account import Account
from brain.database.prediction import Prediction
from brain.converter.crypto import hash_pass, verify_pass
from brain.database.entity import Entity
from brain.database.dataset import Collection
from brain.cache.query import Query
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity
)


# local variables
blueprint = Blueprint(
    'name',
    __name__,
    template_folder='interface/templates',
    static_folder='interface/static'
)

# setup the flask-jwt-extended extension
jwt = JWTManager(blueprint)


@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def index(path):
    '''

    This router function renders the 'index.html' template, for all requests,
    which do not have corresponding route definitions.

    Note: the following resources can be further reviewed:

          http://flask.pocoo.org/snippets/57/
          https://github.com/pallets/flask/tree/master/examples/flaskr

    '''

    return render_template('index.html')


@blueprint.route('/load-data', methods=['POST'], endpoint='load_data')
@jwt_optional
def load_data():
    '''

    This method returns the computed data, resulting from one of the following
    implemented session:

        - data_new
        - data_append
        - model_predict
        - model_generate

    Note: more information on flask-jwt partially protecting routes:

        http://flask-jwt-extended.readthedocs.io/en/latest/optional_endpoints.html

    '''

    if request.method == 'POST':
        # jwt token user
        current_user = get_jwt_identity()

        # programmatic-interface
        if current_user and request.get_json():
            # send data to brain
            loader = Load_Data(request.get_json())
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

        # get uploaded form files
        if request.files:
            files = request.files
        else:
            files = None

        # web-interface: get submitted form data
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
            - 4, generic login failure:
                - https://www.owasp.org/index.php/Authentication_Cheat_Sheet

    Note: token authentication is stateless, since it doesn't require anything
        to be queried from the server, to verify the user. The token is setup,
        in such a way, where it is known, if the token is valid or not, and if
        the token has been tampered with.

    Note: more information on basic flask-jwt token authentication:

        http://flask-jwt-extended.readthedocs.io/en/latest/basic_usage.html

    '''

    if request.method == 'POST':
        account = Account()

        # programmatic-interface: implement flask-jwt token
        if not current_user and request.get_json():
            results = request.get_json()
            if results['session']:
                # initialize redis connector
                redis = Query()
                redis.start_redis()

                # get username
                supplied = results['session']
                pickled = redis.get(supplied)

                username = pickle.loads(pickled)
                # validate: check username exists
                if (
                    account.check_username(username)['result'] and
                    account.get_uid(username)['result']
                ):

                    # database query: get hashed password, and userid
                    hashed_password = account.get_password(username)['result']
                    uid = account.get_uid(username)['result']

                    # create and serialize uid token
                    access_token = create_access_token(identity=uid)

                    # return status
                    return json.dumps({'status': 0, 'access_token': access_token})

        # web-interface: store user session in redis
        elif request.form:
            # local variables
            username = request.form.getlist('user[login]')[0]
            password = request.form.getlist('user[password]')[0]

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
                        return json.dumps({'status': 0})
                    # notification: incorrect password
                    else:
                        return json.dumps({'status': 4})
                # notification: user does not have a password
                else:
                    return json.dumps({'status': 4})

            # notification: username does not exist
            else:
                return json.dumps({'status': 4})


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
            - 4, internal database errors
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
        if (password and validate_password(password)):

            # validate: unique username
            if (
                username and
                not account.check_username(username)['result']
            ):

                # validate: unique email
                if (
                    email and
                    isValidEmail(email) and
                    not account.check_email(email)['result']
                ):

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


@blueprint.route('/retrieve-collections', methods=['POST'])
def retrieve_collections():
    '''

    This router function retrieves all collections stored in the database.

    '''

    if request.method == 'POST':
        # get all sessions
        collections = Session().get_all_collections()

        # return all sessions
        if collections['result']:
            return json.dumps(collections['result'])
        else:
            return json.dumps({'error': collections['error']})


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
    selected_collection = request.get_json()['selected-collection']
    model_type = ModelType().get_model_type(selected_collection)['result']

    # return all feature labels
    if request.method == 'POST':
        label_list = Hset().uncache(
            model_type + '_feature_labels',
            selected_collection
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
            - 2, improper request submitted
        - string, array of prediction titles

    '''

    if request.method == 'POST':
        # programmatic-interface
        if request.get_json():
            results = request.get_json()
            model_type = results['model_type']

        # web-interface
        elif request.form:
            results = request.form
            args = json.loads(results['args'])
            model_type = args['model_type']

        # retrieve all titles
        else:
            model_type = 'all'

        # query database
        prediction = Prediction()
        response = prediction.get_all_titles(model_type)

        # return results: datetime is not serializable, without 'default'
        #                 string serializer, for incompatible objects.
        #
        if response['status']:
            return json.dumps({
                'status': 0,
                'titles': response['result']
            }, default=str)

        else:
            return json.dumps({'status': 1, 'titles': None})


@blueprint.route(
    '/retrieve-prediction',
    methods=['POST'],
    endpoint='retrieve_prediction'
)
def retrieve_prediction():
    '''

    This router function retrieves a specified prediction parameter.

        - integer, codified indicator of save attempt:
            - 0, successful retrieval of specified prediction parameter
            - 1, unsuccessful retrieval of specified prediction parameter
            - 2, improper request submitted
            - 3, invalid 'model_type'
        - string, prediction parameter

    '''

    if request.method == 'POST':
        # programmatic-interface
        if request.get_json():
            results = request.get_json()
            id_result = results['id_result']

        # web-interface
        elif request.form:
            results = request.form
            id_result = json.loads(results['id_result'])

        # invalid request
        else:
            return json.dumps({'status': 2})

        # query database and return results
        prediction = Prediction()
        result = prediction.get_result(id_result)
        model_type = prediction.get_model_type(id_result)['result']

        if model_type == 'svm':
            classes = prediction.get_value(id_result, model_type, 'class')
            df = prediction.get_value(id_result, model_type, 'decision_function')
            prob = prediction.get_value(id_result, model_type, 'probability')

            if (
                result['status'] and
                classes['status'] and
                df['status'] and
                prob['status']
            ):
                # return results: queried 'decimal' database values, are not
                #                 json serializable, without using the 'default'
                #                 string serializer.
                #
                return json.dumps({
                    'status': 0,
                    'result': result['result'],
                    'classes': classes['result'],
                    'decision_function': df['result'],
                    'probability': prob['result']
                }, default=str)
            else:
                return json.dumps({'status': 1})

        elif model_type == 'svr':
            coefficient = prediction.get_value(id_result, model_type, 'r2')

            if coefficient['status']:
                # return results: queried 'decimal' database values, are not
                #                 json serializable, without using the 'default'
                #                 string serializer.
                #
                return json.dumps({
                    'status': 0,
                    'result': result['result'],
                    'r2': coefficient['result']
                }, default=str)
            else:
                return json.dumps({'status': 1})

        else:
            return json.dumps({'status': 3})


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
            - 3, improper request submitted

    '''

    if request.method == 'POST':
        # programmatic-interface
        if request.get_json():
            results = request.get_json()
            data = results['data']

        # web-interface: double decoder required, since nested encoding
        elif request.form:
            results = request.form
            data = json.loads(json.loads(results['data']))

        # invalid request
        else:
            return json.dumps({'status': 3})

        # local variables
        status = results['status']
        type = results['model_type']
        title = results['title']

        # save prediction
        if status == 'valid':
            prediction = Prediction()
            result = prediction.save(data, type, title)['result']

            # notification: prediction status
            if result == 0:
                return json.dumps({'status': 0})
            else:
                return json.dumps({'status': 1})

        # notification: status not valid
        else:
            return json.dumps({'status': 2})


@blueprint.route(
    '/collection-count',
    methods=['POST'],
    endpoint='collection_count'
)
def collection_count():
    '''

    This router function retrieves the number of collections, saved by a
    specified user.

    '''

    if request.method == 'POST':
        # local variables
        count = None
        entity = Entity()

        # programmatic-interface
        if request.get_json():
            r = request.get_json()
            uid = r['uid']
            count = entity.get_collection_count(uid)

        if count and isinstance(count['result'], (int, long)):
            return json.dumps({'count': count['result']})
        else:
            return json.dumps({'count': -1})


@blueprint.route(
    '/document-count',
    methods=['POST'],
    endpoint='document_count'
)
def document_count():
    '''

    This router function retrieves the number of documents in a specified
    collection.

    '''

    if request.method == 'POST':
        # local variables
        count = None
        collection = Collection()

        # programmatic-interface
        if request.get_json():
            r = request.get_json()
            cname = r['collection']
            count = collection.query(cname, 'count_documents')

        if (
            count and
            count['status'] and
            isinstance(count['result'], (int, long))
        ):
            return json.dumps({'count': count['result']})
        else:
            return json.dumps({'count': -1})


@blueprint.route(
    '/remove-collection',
    methods=['POST'],
    endpoint='remove_collection'
)
def remove_collection():
    '''

    This router function removes a collection, with respect to a database type.

    @collection, indicates a nosql implementation
    @entity, indicates a sql database

    '''

    if request.method == 'POST':
        # local variables
        response = None
        entity = Entity()
        collection = Collection()

        # programmatic-interface
        if request.get_json():
            r = request.get_json()
            uid = r['uid']
            type = r['type']
            cname = r['collection']

            if (cname and type == 'collection'):
                payload = {'properties.uid': uid}
                response = collection.query(cname, 'drop_collection', payload)

            elif (type == 'entity'):
                response = entity.remove_entity(uid, cname)

        # lastrowid returned must be greater than 0
        if response and response['result']:
            return json.dumps({'response': response['result']})
        else:
            return json.dumps({'response': response})
