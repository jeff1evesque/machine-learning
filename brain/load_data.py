#!/usr/bin/python

'''

This file allocates input to respective 'data_xxx.py', 'model_xx.py', and
generates a return object, when required.
json.dumps(
'''

import json
from flask import current_app, session
from brain.session.data_new import DataNew
from brain.session.data_append import DataAppend
from brain.session.model_generate import ModelGenerate
from brain.session.model_predict import ModelPredict
from brain.database.session import Session


class Load_Data(object):
    '''

    This class provides an interface to load the necessary parameters:

        - to store, or append a dataset into a SQL database.
        - generate a model into a NoSQL cache, using a previous stored dataset
              from the SQL database.
        - generate a prediction using a previous cached model.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, data, uid=None):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.data = data
        self.session_list = [
            'data_new',
            'data_append',
            'model_generate',
            'model_predict',
        ]
        self.list_error = []

        # programmatic api: flask jwt-token user
        if uid:
            self.uid = uid

        # web interface: flask session user
        elif (not uid and 'uid' in session and session['uid']):
            self.uid = session['uid']

        # unauthenticated user
        else:
            self.uid = current_app.config.get('USER_ID')

    def load_data_new(self):
        '''

        This method validates the supplied parameters, before being stored as
        new entries, into corresponding tables in the SQL database.

        '''

        # instantiate class
        session = DataNew(self.data, self.uid)

        # implement class methods
        if not session.validate_arg_none():
            session.validate_premodel_settings()
            session.convert_dataset()
            session.save_premodel_dataset()
            session.save_entity('data_new')

        if session.get_errors():
            response = {
                'status': 1,
                'msg': 'Dataset(s) not uploaded into database',
                'type': 'data-new',
                'error': session.get_errors()
            }

        else:
            response = {
                'status': 0,
                'msg': 'Dataset(s) properly uploaded into database',
                'type': 'data-new'
            }

        return json.dumps(response)

    def load_data_append(self):
        '''

        This method validates the supplied parameters, before being appended to
        existing entries, from corresponding tables in the SQL database.

        '''

        # instantiate class
        session = DataAppend(self.data, self.uid)

        # define current session id
        collection = self.data['properties']['collection']
        session_id = Session().get_session_id(collection)['result']
        session.validate_id(session_id)

        # implement class methods
        if not session.validate_arg_none():
            session.validate_premodel_settings()
            session.convert_dataset()
            session.save_premodel_dataset()
            session.save_entity('data_append', session_id)

        if session.get_errors():
            response = {
                'status': 1,
                'msg': 'Dataset(s) not uploaded into database',
                'type': 'data-append',
                'error': session.get_errors()
            }

        else:
            response = {
                'status': 0,
                'msg': 'Dataset(s) properly appended into database',
                'type': 'data-append'
            }

        return json.dumps(response)

    def load_model_generate(self):
        '''

        This method validates the supplied parameters, before generating a
        model into a NoSQL cache, using a chosen stored dataset from the SQL
        database.

        '''

        # instantiate class
        session = ModelGenerate(self.data)

        # generate model
        if not session.validate_arg_none():
            session.validate_premodel_settings()
            session.generate_model()

        # return
        if session.get_errors():
            response = {
                'status': 1,
                'msg': 'Model not generated',
                'type': 'model-generate',
                'error': session.get_errors()
            }
        else:
            response = {
                'status': 0,
                'msg': 'Model properly generated',
                'type': 'model-generate'
            }

        return json.dumps(response)

    def load_model_predict(self):
        '''

        This method validates the supplied parameters, before generating a
        prediction, using a chosen stored model from the NoSQL cache.

        '''

        # instantiate class
        errors = None
        session = ModelPredict(self.data)

        # implement class methods
        if not session.validate_arg_none():
            session.validate_premodel_settings()
            if session.get_errors():
                errors = session.get_errors()

            my_prediction = session.predict()
            if errors or my_prediction['error']:
                response = {
                    'status': 1,
                    'result': my_prediction['error'],
                    'type': 'model-predict',
                    'error': session.get_errors()
                }
            else:
                response = {
                    'status': 0,
                    'result': my_prediction,
                    'type': 'model-predict'
                }

            return json.dumps(response)

    def get_session_type(self):
        '''

        This method returns the following session type, from the corresponding
        supplied parameters:

            - data_new
            - data_append
            - model_generate
            - model_predict

        '''

        session_type = self.data['properties']['session_type']
        if session_type in self.session_list:
            return {'session_type': session_type, 'error': None}
        else:
            error = 'Error: the provided \'svm_type\' must be '\
                '\'data_new\', \'data_append\', \'model_generate\', or'\
                '\'model_predict\'.'
            self.list_error.append(error)
            return {'session_type': None, 'error': error}

    def get_errors(self):
        '''

        This method returns all errors pertaining to the instantiated class.

        '''

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
