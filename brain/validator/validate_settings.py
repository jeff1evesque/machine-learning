#!/usr/bin/python

'''@validate_settings

This file performs validation on session settings.

'''

from jsonschema.validators import Draft4Validator
from brain.schema.jsonschema_definition import jsonschema_data_new
from brain.schema.jsonschema_definition import jsonschema_data_append
from brain.schema.jsonschema_definition import jsonschema_model_generate
from brain.schema.jsonschema_definition import jsonschema_model_predict


class Validate_Settings(object):
    '''@Validate_Settings

    This class provides an interface to validate the settings for each
    session.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, svm_data, svm_session=None):
        '''@__init__

        This constructor saves a subset of the passed-in form data.

        '''

        self.svm_data = svm_data
        self.svm_settings = self.svm_data['data']['settings']
        self.svm_session = svm_session

    def validate(self):
        '''@validate

        This method validates the SVM settings for the 'data_new',
        'data_append', 'model_generate', or 'model_predict' sessions.

        Note: This method does not validate the associated 'file upload(s)'.
              The latter is validated via 'validate_file_extension.py', and
              'validate_dataset.py'.

        '''

        # local variables
        list_error = []

        # validation on 'data_new' session
        if self.svm_session == 'data_new':
            try:
                validate = Draft4Validator(jsonschema_data_new())
                validate.validate(self.svm_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'data_append' session
        if self.svm_session == 'data_append':
            try:
                validate = Draft4Validator(jsonschema_data_append())
                validate.validate(self.svm_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'model_generate' session
        if self.svm_session == 'model_generate':
            try:
                validate = Draft4Validator(jsonschema_model_generate())
                validate.validate(self.svm_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'model_predict' session
        elif self.svm_session == 'model_predict':
            try:
                validate = Draft4Validator(jsonschema_model_predict())

                int(self.svm_settings['svm_model_id'])
                for value in self.svm_settings['prediction_input[]']:
                    float(value)

                validate.validate(self.svm_settings)
            except Exception, error:
                list_error.append(str(error))

        # return error
        if len(list_error) > 0:
            return {'status': False, 'error': list_error}
        else:
            return {'status': True, 'error': None}
