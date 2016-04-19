#!/usr/bin/python

'''@validate_dataset

This script performs validation on the svm dataset(s).

'''

from jsonschema.validators import Draft4Validator
from brain.schema.jsonschema_definition import jsonschema_string


class Validate_Dataset(object):
    '''Validate_Dataset

    This class provies an interface to validate provided dataset(s) during
    'data_new', and 'data_append' sessions.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, data, svm_session=None):
        '''@__init__

        This constructor saves a subset of the passed-in form data.

        '''

        self.data = data
        self.svm_session = svm_session
        self.list_error = []

    def validate_label(self):
        '''@validate_label

        This method validates either the dependent variable (observation)
        label(s), or the independent variable (feature) label(s).

        '''

        try:
            Draft4Validator(jsonschema_string()).validate({'value': self.data})
        except Exception, error:
            self.list_error.append(str(error))

    def validate_value(self):
        '''@validate_value

        This method validates the independent variable (feature) value(s).

        '''

        try:
            float(self.data)
        except Exception, error:
            self.list_error.append(str(error))

    def get_errors(self):
        '''get_errors

        This method gets all current errors. associated with this class
        instance.

        '''

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
