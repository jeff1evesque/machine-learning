#!/usr/bin/python

'''@load_data

This file allocates input to respective 'data_xxx.py', 'model_xx.py', and
generates a return object, when required.
json.dumps(
'''

import json
from brain.session.data_append import Data_Append
from brain.session.data_new import Data_New
from brain.session.model_generate import Model_Generate
from brain.session.model_predict import Model_Predict


class Load_Data(object):
    '''@Load_Data

    This class provides an interface to load the necessary parameters:

        - to store, or append a dataset into a SQL database.
        - generate a model into a NoSQL cache, using a previous stored dataset
              from the SQL database.
        - generate a prediction using a previous cached model.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, data):
        '''@__init__

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

    def load_data_new(self):

        '''@load_data_new

        This method validates the supplied parameters, before being stored as
        new entries, into corresponding tables in the SQL database.

        '''

        # instantiate class
        session = Data_New(self.data)

        # implement class methods
        if not session.validate_arg_none():
            session.validate_premodel_settings()
            session.validate_file_extension()
            session.check()

            session_entity = session.save_entity('data_new')
            if session_entity['status']:
                session_id = session_entity['id']
                session.validate_id(session_id)
                session.check()

                session.dataset_to_dict(session_id)
                session.check()
                session.save_feature_count()
                session.check()

                session.save_observation_label('data_new', session_id)
                session.check()

                session.save_premodel_dataset()
                session.check()

            response = {
                'status': 0,
                'msg': 'Dataset(s) properly uploaded into database'
            }

        else:
            print session.get_errors()
            response = {
                'status': 1,
                'msg': 'Dataset(s) not uploaded into database'
            }

        return json.dumps(response)

    def load_data_append(self):
        '''@load_data_append

        This method validates the supplied parameters, before being appended to
        existing entries, from corresponding tables in the SQL database.

        '''

        # instantiate class
        session = Data_Append(self.data)

        # define current session id
        session_id = self.data['data']['settings']['session_id']
        session.validate_id(session_id)

        # implement class methods
        if not session.validate_arg_none() and not session.get_errors():
            session.validate_premodel_settings()
            session.validate_file_extension()
            session.check()

            session_entity = session.save_entity('data_append', session_id)
            if session_entity['status']:
                session.check()

                session.dataset_to_dict(session_id)
                session.check()

                session.save_observation_label('data_append', session_id)
                session.check()

                session.save_premodel_dataset()
                session.check()

            response = {
                'status': 0,
                'msg': 'Dataset(s) properly appended into database'
            }

        else:
            print session.get_errors()
            response = {
                'status': 1,
                'msg': 'Dataset(s) not uploaded into database'
            }

        return json.dumps(response)

    def load_model_generate(self):
        '''@load_model_generate

        This method validates the supplied parameters, before generating a
        model into a NoSQL cache, using a chosen stored dataset from the SQL
        database.

        '''

        # instantiate class
        session = Model_Generate(self.data)

        # generate model
        if not session.validate_arg_none():
            session.validate_premodel_settings()
            session.check()
            session.generate_model()

        # return
        if session.return_error():
            response = {
                'status': 1,
                'msg': 'Model not generated'
            }
        else:
            response = {
                'status': 0,
                'msg': 'Model properly generated'
            }

        return json.dumps(response)

    def load_model_predict(self):
        '''@load_model_predict

        This method validates the supplied parameters, before generating a
        prediction, using a chosen stored model from the NoSQL cache.

        '''

        # instantiate class
        session = Model_Predict(self.data)

        # implement class methods
        if not session.validate_arg_none():
            session.validate_premodel_settings()
            session.check()

            my_prediction = session.predict()
            if my_prediction['error']:
                response = {
                    'status': 1,
                    'result': my_prediction['error'],
                }
            else:
                response = {
                    'status': 0,
                    'result': my_prediction,
                }

            return json.dumps(response)

    def get_session_type(self):
        '''@load_model_predict

        This method returns the following session type, from the corresponding
        supplied parameters:

            - data_new
            - data_append
            - model_generate
            - model_predict

        '''

        session_type = self.data['data']['settings']['session_type']
        if session_type in self.session_list:
            return {'session_type': session_type, 'error': None}
        else:
            error = 'Error: the provided \'svm_type\' must be '\
                '\'data_new\', \'data_append\', \'model_generate\', or'\
                '\'model_predict\'.'
            self.list_error.append(error)
            return {'session_type': None, 'error': error}

        # return
        if self.return_error:
            return False
        else:
            return 'Model properly generated'

    def get_errors(self):
        '''@get_errors

        This method returns all errors pertaining to the instantiated class.

        '''

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
