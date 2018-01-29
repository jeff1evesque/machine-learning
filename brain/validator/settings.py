#!/usr/bin/python

'''

This file performs validation on session settings.

'''

from flask import current_app
from voluptuous import Schema, Required, Optional, All, Any, Coerce, In, Length


class Validator(object):
    '''

    This class provides an interface to validate the settings for each
    session.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor saves a subset of the passed-in form data.

        '''

        self.list_error = []

    def validate_settings(self, premodel_settings, session_type):
        '''

        This method validates the premodel settings for the 'data_new',
        'data_append', 'model_generate', or 'model_predict' sessions.

        Note: This method does not validate the associated 'file upload(s)',
              which is the responsibility of the mongodb query process.

        '''

        # local variables
        model_type = current_app.config.get('MODEL_TYPE')
        dataset_type = current_app.config.get('DATASET_TYPE')
        sv_kernel_type = current_app.config.get('SV_KERNEL_TYPE')

        # validation on 'data_new', 'data_append' session
        if session_type in ['data_new', 'data_append']:
            schema = Schema({
                Required('collection'): All(unicode, Length(min=1)),
                Required('dataset_type'): In(dataset_type),
                Required('model_type'): In(model_type),
                Required('session_type'): Any('data_new', 'data_append'),
                Optional('session_name'): All(unicode, Length(min=1)),
                Optional('stream'): Any('True', 'False'),
            })

        # validation on 'model_generate' session
        if session_type == 'model_generate':
            schema = Schema({
                Required('collection'): All(unicode, Length(min=1)),
                Required('model_type'): In(model_type),
                Required('session_type'): 'model_generate',
                Optional('stream'): Any('True', 'False'),
                Required('sv_kernel_type'): In(sv_kernel_type),
            })

        # validation on 'model_predict' session
        elif session_type == 'model_predict':
            schema = Schema({
                Required('collection'): All(unicode, Length(min=1)),
                Optional('stream'): Any('True', 'False'),
                Required('prediction_input[]'): [
                    Any(Coerce(int), Coerce(float)),
                ],
                Required('session_type'): 'model_predict',
            })

        try:
            schema(premodel_settings)

        except Exception, error:
            self.list_error.append(error)
            return error

        return False

    def get_errors(self):
        '''

        This method gets all current errors.

        '''

        return self.list_error
