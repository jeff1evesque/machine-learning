#!/usr/bin/python

## @session_model_use.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored SVM model, generated from 'session_model_generate.py'.
#      The determined SVM Model is then used for analysis based on the input data
#      provided during the current session.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys, json
from database.data_saver import Analysis
from validator.validator_settings import Validate_Settings

## Class: Model_Use
class Model_Use:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data    = svm_data
    self.svm_session = json.loads(self.svm_data)['data']['settings']['svm_session']

  ## CHANGE_METHOD: we will adjust the logic below
  def CHANGE_METHOD(self):
    if len(sys.argv) > 1:
      # validate input data is json format
      validator = Validate_Settings( sys.argv[1], self.svm_session )

      # validate, and set SVM properties to 'data_creator.py'
      if ( json.loads(sys.argv[1])['json_creator'] == 'load_logic.php' ):
        if ( json.loads(sys.argv[1])['data'].get('result', None) ):
          validator.data_validation()

    else:
      msg = 'Please provide a training dataset in json format'
      print json.dumps({'error':msg}, separators=(',', ': '))
      sys.exit()
