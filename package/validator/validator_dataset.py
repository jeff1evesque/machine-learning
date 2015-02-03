#!/usr/bin/python

## @validator_dataset.py
#  This script performs validation on the svm data.
import json, sys
from jsonschema import validate
from schema.jsonschema_definition import jsonschema_dataset, jsonschema_dataset_id

## Class: Validate_Dataset, explicitly inherit 'new-style' class
class Validate_Dataset(object):

  ## constructor: saves a subset of the passed-in form data
  def __init__(self, svm_data, svm_session=None):
    self.svm_data    = svm_data
    self.svm_session = svm_session

  ## dataset_validation: each supplied SVM dataset is correctly formatted via corresponding
  #                      methods in 'svm_json.py'. After being formatted, each dataset is
  #                      validated in this method.
  #
  #  Note: the SVM dataset is synonymous for the 'file upload(s)'
  def dataset_validation(self):
    # local variables
    list_error = []

    # iterate outer dict
    for key, value in self.svm_data.iteritems():
      try:
        if key == 'svm_dataset':
          for dict in value:
            try:
              validate( dict, jsonschema_dataset() )
            except Exception, error:
              list_error.append(str(error))
        elif key == 'id_entity':
          try:
            validate( {key: value}, jsonschema_dataset_id() )
          except Exception, error:
            list_error.append(str(error))
      except Exception, error:
        list_error.append(str(error))

    # return error
    if len(list_error) > 0:
      return { 'status': False, 'error': list_error }
    else:
      return { 'status': True, 'error': None }
