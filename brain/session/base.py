#!/usr/bin/python

'''

This file serves as the superclass for 'data_xx.py', and 'model_xx.py' files.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from flask import current_app
from brain.validator.settings import Validator


class Base(object):
    '''

    This class provides a general base class, used for the following sessions,
    and within their corresponding classes:

        - data_new
        - data_append
        - model_generate
        - model_predict

    Note: this class is invoked within 'data_xx.py', 'model_xx.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.list_error = []
        self.premodel_data = premodel_data
        self.list_model_type = current_app.config.get('MODEL_TYPE')
        self.session_type = self.premodel_data['properties']['session_type']

    def validate_arg_none(self):
        '''

        This method checks if the class variable 'premodel_data' is defined.

        '''

        if self.premodel_data is None:
            return True
        else:
            return False

    def validate_premodel_settings(self):
        '''

        This method validates the provided settings (not the dataset), that
        describe the session.

        '''

        settings = self.premodel_data['properties']
        error = Validator().validate_settings(
            self.premodel_data['properties'],
            self.session_type
        )

        session_type = settings.get('session_type', None)
        stream = settings.get('stream', None)
        if stream == 'True' and session_type in ['data_add', 'data_append']:
            location = settings['session_name']
        else:
            location = session_type

        if not self.list_error and error:
            self.list_error.append({
                'error': {
                    'validation': [{
                        'location': location,
                        'message': error
                    }]
                }
            })

        elif self.list_error and error:
            if not self.list_error['error']:
                self.list_error.append({
                    'error': {
                        'validation': [{
                            'location': location,
                            'message': error
                        }]
                    }
                })

            elif not self.list_error['error']['validation']:
                self.list_error['error']['validation'] = [{
                    'location': location,
                    'message': error
                }]

            else:
                self.list_error['error']['validation'].append({
                    'location': location,
                    'message': error
                })

    def get_errors(self):
        '''

        This method returns all current errors associated with this class.

        '''

        if self.list_error:
            return self.list_error
        else:
            return None
