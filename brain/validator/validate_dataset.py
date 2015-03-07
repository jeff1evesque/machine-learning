#!/usr/bin/python

## @validate_dataset.py
#  This script performs validation on the svm data.
import json, sys
from jsonschema import validate
from brain.schema.jsonschema_definition import jsonschema_dataset, jsonschema_dataset_id

## Class: Validate_Dataset, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Validate_Dataset(object):

  ## constructor: saves a subset of the passed-in form data
  def __init__(self, svm_data, svm_session=None):
    self.svm_data    = svm_data
    self.svm_session = svm_session

  ## dataset_validation: each supplied SVM dataset is correctly formatted into a dict,
  #                      then validated in this method.
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
