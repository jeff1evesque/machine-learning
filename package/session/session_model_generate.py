#!/usr/bin/python

## @session_model_generate.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and generates an SVM model, respectively. The new SVM model, is stored
#      into respective database table(s), which later can be retrieved within
#      'session_model_use.py'.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys
from validator.validator_settings import Validate_Settings

## Class: Model_Generate
class Model_Generate:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data       = svm_data
    self.svm_session    = json.loads(self.svm_data)['data']['settings']['svm_session']
    self.response_error = []

  ## validate_arg_none: check if class variable 'svm_data' is defined.
  def validate_arg_none(self):
    if self.svm_data == None: return True
    else: return False

  ## validate_svm_settings: validate svm session settings (not dataset).
  def validate_svm_settings(self):
    validator = Validate_Settings( self.svm_data, self.svm_session )
    validator.data_validation()

    if validator.data_validation()['error'] != None:
      self.response_error.append( validator.data_validation()['error'] )

  ## return_error: return appended error messages.
  def return_error(self):
    return self.response_error

  ## check: check if the class instance contains any errors appended to the list
  #         'self.response_error'. If any error(s) exists, it is printed, and the
  #         program exits.
  def check(self):
    if len(self.response_error) > 0:
      for error in self.response_error:
        print error
      sys.exit()
