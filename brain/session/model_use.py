#!/usr/bin/python

## @model_use.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored SVM model, generated from 'model_generate.py'. The
#      determined SVM Model is then used for analysis based on the input data
#      provided during the current session.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys
from brain.validator.validator_settings import Validate_Settings

## Class: Model_Use, explicitly inherit 'new-style' class
class Model_Use(object):

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data    = svm_data
    self.svm_session = self.svm_data['data']['settings']['svm_session']

  ## CHANGE_METHOD: we will adjust the logic below
  def CHANGE_METHOD(self):
    # validate input data is json format
    validator = Validate_Settings( sys.svm_data, self.svm_session )

    # validate, and set SVM properties to 'data_creator.py'
    if ( sys.svm_data['json_creator'] == 'load_logic.php' ):
      if ( sys.svm_data['data'].get('result', None) ):
        validator.data_validation()

    else:
      msg = 'Please provide a training dataset in json format'
      print {'error':msg}
      sys.exit()
