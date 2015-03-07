#!/usr/bin/python

## @validate_settings.py
#  This script performs validation on session settings. 
import sys
from jsonschema import validate
from brain.schema.jsonschema_definition import jsonschema_data_new, jsonschema_data_append, jsonschema_model_generate, jsonschema_model_use

## Class: Validate_Settings, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base.py'
class Validate_Settings(object):

  ## constructor: saves a subset of the passed-in form data
  def __init__(self, svm_data, svm_session=None):
    self.svm_data    = svm_data
    self.svm_session = svm_session

  ## validate: this method validates the SVM settings for the 'data_new',
  #            'data_append', 'model_generate', or 'model_use' sessions.
  #
  #  Note: This method does not validate the associated 'file upload(s)'. The
  #        latter is validated via 'validate_mime.py', and 'validate_dataset.py'.
  def validate(self):
    # local variables
    list_error = []
    svm_settings = self.svm_data['data']['settings']

    # validation on 'data_new' session
    if self.svm_session == 'data_new':
      try:
        validate(self.svm_data['data']['settings'], jsonschema_data_new())
      except Exception, error:
        list_error.append(str(error))

      # validation on 'xml file(s)'
      if ( svm_settings.get('svm_dataset_type', None) == 'upload file' and svm_settings.get('svm_dataset', None) ):
        for index, xmldata in enumerate(svm_settings['svm_dataset']):
          print xmldata

    # validation on 'data_append' session
    if self.svm_session == 'data_append':
      try:
        validate(self.svm_data['data']['settings'], jsonschema_data_append())
      except Exception, error:
        list_error.append(str(error))

    # validation on 'model_generate' session

    # validation on 'model_use' session
    elif self.svm_session == 'model_use':
      try:
        validate(self.svm_data['data']['settings'], jsonschema_model_use())
      except Exception, error:
        list_error.append(str(error))

    # return error
    if len(list_error) > 0:
      return { 'status': False, 'error': list_error }
    else:
      return { 'status': True, 'error': None }
