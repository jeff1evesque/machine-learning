#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on the form data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.
import json

## Class: Validator
class Validator:

  ## constructor: saves a subset of the passed-in form data
  #
  #  @svm_data    : is the input data, generally a form POST data, if
  #                 the 'session_type' is training.
  #  @session_type: represents the current session type
  def __init__(self, svm_data, session_type):
    self.svm_data = svm_data
    self.svm_session = session_type

  ## data_validation(): ensure passed in dataset is json formatted
  def data_validation(self):
    try:
      json.loads(self.svm_data)
    except ValueError, e:
      print 'Error:'
