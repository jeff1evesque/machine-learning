#!/usr/bin/python

'''

This file performs validation on session settings.

'''

from jsonschema.validators import Draft4Validator
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

        self.premodel_data = premodel_data
        self.premodel_settings = self.premodel_data['data']['settings']
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
                validate = Draft4Validator(schema_data_new())
                validate.validate(self.premodel_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'data_append' session
        if self.session_type == 'data_append':
            try:
                validate = Draft4Validator(schema_data_append())
                validate.validate(self.premodel_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'model_generate' session
        if self.session_type == 'model_generate':
            try:
                validate = Draft4Validator(schema_model_generate())
                validate.validate(self.premodel_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'model_predict' session
        elif self.session_type == 'model_predict':
            try:
                validate = Draft4Validator(schema_model_predict())

                int(self.premodel_settings['model_id'])
                for value in self.premodel_settings['prediction_input[]']:
                    float(value)

                validate.validate(self.premodel_settings)
            except Exception, error:
                list_error.append(str(error))

        # return error
        if len(list_error) > 0:
            return {'status': False, 'error': list_error}
        else:
            return {'status': True, 'error': None}
