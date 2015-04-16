#!/usr/bin/python

## @load_data.py
#  This file allocates input to respective 'data_xxx.py', 'model_xx.py',
#      and generates a return object, when required.
import sys
from brain.session.data_append import Data_Append
from brain.session.data_new import Data_New
from brain.session.model_generate import Model_Generate
from brain.session.model_predict import Model_Predict

## Class: Load_Data, explicitly inherit 'new-style' class
class Load_Data(object):

    ## constructor:
    def __init__(self, data):
        self.data         = data
        self.session_list = ['data_new', 'data_append', 'model_generate', 'model_predict']
        self.list_error   = []

    ## load_data_new: redirect input to 'session_data_new.py'
    def load_data_new(self):

        # instantiate class
        session = Data_New(self.data)

        # implement class methods
        if not session.validate_arg_none():
            session.validate_svm_settings()
            session.validate_mime_type()
            session.check()

            session_entity = session.save_svm_entity('data_new')
            if session_entity['status']:
                session_id = session_entity['id']
                session.validate_id(session_id)
                session.check()

                session.dataset_to_dict(session_id)
                session.check()
                session.save_svm_info()
                session.check()

                session.save_observation_label('data_new', session_id)
                session.check()

                session.save_svm_dataset()
                session.check()

            return 'Dataset(s) properly uploaded into database'
        else:
            print session.get_errors()
            return None

    ## load_data_append: redirect input to 'session_data_append.py'
    def load_data_append(self):

        # instantiate class
        session = Data_Append(self.data)

        # define current session id
        session_id = self.data['data']['settings']['svm_session_id']
        session.validate_id(session_id)

        # implement class methods
        if not session.validate_arg_none() and not session.get_errors():
            session.validate_svm_settings()
            session.validate_mime_type()
            session.check()

            session_entity = session.save_svm_entity('data_append', session_id)
            if session_entity['status']:
                session.check()

                session.dataset_to_dict(session_id)
                session.check()

                session.save_observation_label('data_append', session_id)
                session.check()

                session.save_svm_dataset()
                session.check()

            return 'Dataset(s) properly appended into database'
        else:
            print session.get_errors()
            return None

    ## load_model_generate: redirect input to 'session_model_generate.py'
    def load_model_generate(self):

        # instantiate class
        session = Model_Generate(self.data)

        # generate model
        session.generate_model()

        # return
        if session.return_error: return False
        else: return 'Model properly generated'

    ## load_model_predict: redirect input to 'session_model_predict.py'
    def load_model_predict(self):

        # instantiate class
        session = Model_Predict(self.data)

        # implement class methods
        my_prediction = session.svm_prediction()
        if my_prediction['error']: return {'result': None, 'error': my_prediction['error']}
        else: return {'result': my_prediction, 'error': None}

    ## get_session_type: returns the current session type.
    def get_session_type(self):
        session_type = self.data['data']['settings']['svm_session']
        if session_type in self.session_list: return {'session_type': session_type, 'error': None}
        else:
            error = 'Error: the provided \'svm_session\' must be \'data_new\', \'data_append\', \'model_generate\', or \'model_predict\'.'
            self.list_error.append(error)
            return {'session_type': None, 'error': error}

        # return
        if session.return_error: return False
        else: return 'Model properly generated'

    # get_errors: returns a list of current errors associated with class instance
    def get_errors(self):
        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
