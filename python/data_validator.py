#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on input data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.  This adds an extra layer of security,
#  especially if the script later is used without a web interface.
import json, sys, magic
from jsonschema import validate
from helper import md5_for_file
from jsonschema_definition import jsonschema_training, jsonschema_analysis, jsonschema_dataset, jsonschema_dataset_id

## Class: Validator
class Validator:

  ## constructor: saves a subset of the passed-in form data
  #
  #  @svm_data    : is the input data, generally a form POST data, if
  #                 the 'session_type' is training.
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
