#!/usr/bin/python

## @validate_settings.py
#  This script performs validation on session settings. 
import sys
from jsonschema.validators import Draft4Validator
from brain.schema.jsonschema_definition import jsonschema_data_new, jsonschema_data_append, jsonschema_model_generate, jsonschema_model_predict

## Class: Validate_Settings, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base.py'
class Validate_Settings(object):

    ## constructor: saves a subset of the passed-in form data
    def __init__(self, svm_data, svm_session=None):
        self.svm_data     = svm_data
        self.svm_settings = self.svm_data['data']['settings']
        self.svm_session  = svm_session

    ## validate: this method validates the SVM settings for the 'data_new',
    #            'data_append', 'model_generate', or 'model_predict' sessions.
    #
    #  Note: This method does not validate the associated 'file upload(s)'. The
    #        latter is validated via 'validate_mime.py', and 'validate_dataset.py'.
    def validate(self):
        # local variables
        list_error = []

        # validation on 'data_new' session
        if self.svm_session == 'data_new':
            try:
                Draft4Validator(jsonschema_data_new()).validate(self.svm_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'data_append' session
        if self.svm_session == 'data_append':
            try:
                Draft4Validator(jsonschema_data_append()).validate(self.svm_settings)
            except Exception, error:
                list_error.append(str(error))

        # validation on 'model_generate' session

        # validation on 'model_predict' session
        elif self.svm_session == 'model_use':
            try:
                Draft4Validator(jsonschema_model_use()).validate(self.svm_settings)
            except Exception, error:
                list_error.append(str(error))

        # return error
        if len(list_error) > 0:
            return {'status': False, 'error': list_error}
        else:
            return {'status': True, 'error': None}
