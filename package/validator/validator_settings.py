#!/usr/bin/python

## @validator_settings.py
#  This script performs validation on session settings. 
import json, sys
from jsonschema import validate
from schema.jsonschema_definition import jsonschema_data_new, jsonschema_data_append, jsonschema_model_generate, jsonschema_model_use

## Class: Validate_Settings, explicitly inherit 'new-style' class
class Validate_Settings(object):

  ## constructor: saves a subset of the passed-in form data
  def __init__(self, svm_data, svm_session=None):
    self.svm_data    = svm_data
    self.svm_session = svm_session

  ## data_validation: this method validates the SVM settings for the
  #                   'data_new', 'data_append', 'model_generate', or
  #                   'model_use' sessions.
  #
  #  Note: This method does not validate the associated 'file upload(s)'. The
  #        latter component is validated via 'validator_mime.py', and 
  #        'validator_dataset.py'.
  def data_validation(self):
    # local variables
    flag_json  = False
    list_error = []

    # determine if input data is a JSON object
    try:
      json_data = json.loads(self.svm_data)['data']['settings']
      flag_json = True
    except ValueError, e:
      error     = 'The SVM settings have not been properly configured'
      list_error.append(error)
      flag_json = False

    # validation on 'data_new' session
    if self.svm_session == 'data_new' and flag_json:
      try:
        validate(json.loads(self.svm_data)['data']['settings'], jsonschema_data_new())
      except Exception, error:
        list_error.append(str(error))

      # validation on 'xml file(s)'
      if ( json_data.get('svm_dataset_type', None) == 'upload file' and json_data.get('svm_dataset', None) ):
        for index, xmldata in enumerate(json_data['svm_dataset']):
          print xmldata

    # validation on 'data_append' session

    # validation on 'model_generate' session

    # validation on 'model_use' session
    elif self.svm_session == 'model_use' and flag_json:
      try:
        validate(json.loads(self.svm_data)['data']['settings'], jsonschema_model_use())
      except Exception, error:
        list_error.append(str(error))

    # return error
    if len(list_error) > 0:
      return { 'status': False, 'error': list_error }
    else:
      return { 'status': True, 'error': None }
