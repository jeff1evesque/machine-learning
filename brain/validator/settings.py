#!/usr/bin/python

'''

This file performs validation on session settings.

'''

from brain.schema.session import schema_data_new
from brain.schema.session import schema_data_append
from brain.schema.session import schema_model_generate
from brain.schema.session import schema_model_predict


class Validator(object):
    '''

    This class provides an interface to validate the settings for each
    session.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data, session_type=None):
        '''

        This constructor saves a subset of the passed-in form data.

        '''

        self.premodel_settings = premodel_data
        self.session_type = session_type

    def validate(self):
        '''

         This method validates the premodel settings for the 'data_new',
        'data_append', 'model_generate', or 'model_predict' sessions.

        Note: This method does not validate the associated 'file upload(s)',
              which is the responsibility of the mongodb query process.

        '''

        # local variables
        list_error = []

        # validation on 'data_new' session
        if self.session_type == 'data_new':
            try:
                schema_data_new(self.premodel_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'data_append' session
        if self.session_type == 'data_append':
            try:
                schema_data_append(self.premodel_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'model_generate' session
        if self.session_type == 'model_generate':
            try:
                schema_model_generate(self.premodel_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'model_predict' session
        elif self.session_type == 'model_predict':
            try:
                schema_model_predict(self.premodel_settings)
                for value in self.premodel_settings['prediction_input[]']:
                    float(value)
            except Exception, error:
                list_error.append(str(error))

        # return error
        if len(list_error) > 0:
            return {'status': False, 'error': list_error}
        else:
            return {'status': True, 'error': None}
