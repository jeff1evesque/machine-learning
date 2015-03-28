#!/usr/bin/python

## @base.py
#  This file serves as the superclass for 'data_xx.py', and 'model_xx.py' files.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys
from brain.validator.validate_settings import Validate_Settings

## Class: Base, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'data_xx.py', 'model_xx.py'
class Base(object):

    ## constructor:
    def __init__(self, svm_data):
        self.svm_data    = svm_data
        self.svm_session = self.svm_data['data']['settings']['svm_session']
        self.list_error  = []

    ## validate_arg_none: check if class variable 'svm_data' is defined.
    def validate_arg_none(self):
        if self.svm_data == None: return True
        else: return False

    ## validate_svm_settings: validate svm session settings (not dataset).
    def validate_svm_settings(self):
        validator = Validate_Settings(self.svm_data, self.svm_session)
        validator.validate()

        if validator.validate()['error'] != None:
            self.list_error.append(validator.validate()['error'])

    ## get_errors: return appended error messages.
    def get_errors(self):
        return self.list_error

    ## check: check if the class instance contains any errors appended to the list
    #         'self.list_error'. If any error(s) exists, it is printed, and the
    #         program exits.
    def check(self):
        if len(self.list_error) > 0:
            for error in self.list_error:
                print error
            sys.exit()
