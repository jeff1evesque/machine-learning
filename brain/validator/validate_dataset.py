#!/usr/bin/python

## @validate_dataset.py
#  This script performs validation on the svm data.
import json
import sys
from jsonschema.validators import Draft4Validator
from brain.schema.jsonschema_definition import jsonschema_dataset, jsonschema_dataset_id

## Class: Validate_Dataset, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Validate_Dataset(object):

    ## constructor: saves a subset of the passed-in form data
    def __init__(self, svm_data, svm_session=None):
        self.svm_data    = svm_data
        self.svm_session = svm_session
        self.list_error  = []

    ## dataset_validation: each supplied SVM dataset is correctly formatted into a dict,
    #                      then validated in this method.
    #
    #  Note: the SVM dataset is synonymous for the 'file upload(s)'
    def validate(self):
        # iterate outer dict
        for key, value in self.svm_data.iteritems():
            try:
                if key == 'svm_dataset':
                    for dict in value:
                        try:
                            Draft4Validator(jsonschema_dataset()).validate(dict)
                        except Exception, error:
                            list_error.append(str(error))
                elif key == 'id_entity':
                    try:
                        Draft4Validator(jsonschema_id()).validate({key: value})
                    except Exception, error:
                        list_error.append(str(error))
            except Exception, error:
                list_error.append(str(error))

        # return error
        if len(list_error) > 0:
            return {'status': False, 'error': list_error}
        else:
            return {'status': True, 'error': None}
