#!/usr/bin/python

'''

This script performs validation on corresponding dataset(s).

'''

from voluptuous import Schema, Required, All, Any, Length
from voluptuous.humanize import validate_with_humanized_errors


class Validator(object):
    '''

    This class provides an interface to validate provided dataset(s) during
    'data_new', and 'data_append' sessions.

    Note: this class explicitly inherits the 'new-style' class.

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

        schema = Schema({
            Required('dependent-variable'): All(unicode, Length(min=1)),
            Required('independent-variables'): [{
                Required(All(unicode, Length(min=1))): Any(int, float),
            }],
        })

        for instance in data:
            try:
                validate_with_humanized_errors(instance, schema)

            except Exception, error:
                self.list_error.append(str(error).splitlines())

        if self.list_error:
            return self.list_error
        else:
            return False

    def validate_regression(self, data):
        '''

        This method validates svr dataset(s).

        '''

        schema = Schema({
            Required('dependent-variable'): Any(int, float),
            Required('independent-variables'): [{
                Required(All(unicode, Length(min=1))): Any(int, float),
            }],
        })

        for instance in data:
            try:
                validate_with_humanized_errors(instance, schema)

            except Exception, error:
                self.list_error.append(str(error).splitlines())

        if self.list_error:
            return self.list_error
        else:
            return False

    def validate_value(self, data):
        '''

        This method validates the independent variable (feature) value(s).

        '''

        try:
            return float(data)

        except Exception, error:
            self.list_error.append(error)
            return error

    def get_errors(self):
        '''

        This method gets all current errors.

        '''

        return self.list_error
