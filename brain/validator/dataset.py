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

    def __init__(self, data, session_type=None):
        '''

        This constructor saves a subset of the passed-in form data.

        '''

        self.data = data
        self.session_type = session_type
        self.list_error = []

    def validate_value(self):
        '''

        This method validates the independent variable (feature) value(s).

        '''

        try:
            float(self.data)
        except Exception, error:
            self.list_error.append(str(error))

    def get_errors(self):
        '''

        This method gets all current errors. associated with this class
        instance.

        '''

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return False
