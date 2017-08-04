#!/usr/bin/python

'''

This script performs validation on correpsonding dataset(s).

'''


class Validator(object):
    '''

    This class provies an interface to validate provided dataset(s) during
    'data_new', and 'data_append' sessions.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, session_type=None):
        '''

        This constructor saves a subset of the passed-in form data.

        '''

        self.session_type = session_type
        self.list_error = []

    def validate_value(self, data):
        '''

        This method validates the independent variable (feature) value(s).

        '''

        try:
            return float(data)
        except Exception, error:
            self.error = str(error)
            self.list_error.append(str(error))
            return False

    def get_error(self):
        '''

        This method gets the last current error.

        '''

        return self.error

    def get_errors(self):
        '''

        This method gets all current errors.

        '''

        return self.list_error
