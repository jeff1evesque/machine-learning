#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on input data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.  This adds an extra layer of security,
#  especially if the script later is used without a web interface.
import json, sys

## Class: Validator
class Validator:

  ## constructor: saves a subset of the passed-in form data
  #
  #  @svm_data    : is the input data, generally a form POST data, if
  #                 the 'session_type' is training.
  #  @session_type: represents the current session type
  def __init__(self, svm_data, session_type):
    self.svm_data = svm_data
    self.svm_session = session_type.lower()

  ## data_validation():
  def data_validation(self):

    try:
      json.loads(self.svm_data)
    except ValueError, e:
      msg = 'Error: The ' + self.svm_session + ' session requires a json formatted dataset as input'
      print json.dumps({'error':msg}, separators=(',', ': '))
      sys.exit()
