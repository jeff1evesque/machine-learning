#!/usr/bin/python

## @session_model_generate.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and generates an SVM model, respectively. The new SVM model, is stored
#      into respective database table(s), which later can be retrieved within
#      'session_model_use.py'.

## Class: Model_Generate
class Model_Generate:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data       = svm_data
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
