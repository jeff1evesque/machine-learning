#!/usr/bin/python

## @session_base.py
#  This file serves as the superclass for other 'session_xx_xx.py' files.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys, json
from validator.validator_settings import Validate_Settings

## Class: Session_Base
class Session_Base:

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
