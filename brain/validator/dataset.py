#!/usr/bin/python

'''

This script performs validation on corresponding dataset(s).

'''

from voluptuous import Schema, Required, All, Any, Length, Coerce
from voluptuous.humanize import validate_with_humanized_errors
from six import string_types


class Validator:
    '''

    This class provides an interface to validate provided dataset(s) during
    'data_new', and 'data_append' sessions.

    '''

    def __init__(self):
        '''

        This constructor saves a subset of the passed-in form data.

        '''

        self.list_error = []

    def validate_classification(self, data):
        '''

        This method validates svm dataset(s).

        '''

        current_errors = []
        schema = Schema({
            Required('dependent-variable'): All(string_types[0], Length(min=1)),
            Required('independent-variables'): [{
                Required(All(string_types[0], Length(min=1))): Coerce(float),
            }],
            Required('error'): Any(None, string_types[0]),
        })

        for instance in data:
            try:
                validate_with_humanized_errors(instance, schema)

            except Exception as error:
                split_error = str(error).splitlines()
                current_errors.extend(split_error)
                self.list_error.extend(split_error)

        if current_errors:
            return current_errors
        else:
            return False

    def validate_regression(self, data):
        '''

        This method validates svr dataset(s).

        '''

        current_errors = []
        schema = Schema({
            Required('dependent-variable'): Coerce(float),
            Required('independent-variables'): [{
                Required(All(string_types[0], Length(min=1))): Coerce(float),
            }],
            Required('error'): Any(None, string_types[0]),
        })

        for instance in data:
            try:
                validate_with_humanized_errors(instance, schema)

            except Exception as error:
                split_error = str(error).splitlines()
                current_errors.extend(split_error)
                self.list_error.extend(split_error)

        if current_errors:
            return current_errors
        else:
            return False

    def validate_value(self, data):
        '''

        This method validates the independent variable (feature) value(s).

        '''

        try:
            return float(data)

        except Exception as error:
            self.list_error.append(error)
            return error

    def get_errors(self):
        '''

        This method gets all current errors.

        '''

        return self.list_error
