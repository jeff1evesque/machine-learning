#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on input data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.  This adds an extra layer of security,
#  especially if the script later is used without a web interface.
import json, sys, six

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
  #
  #  @self.svm_data: decoded JSON object 
  def data_validation(self):

    # determine if input data is a JSON object
    try:
      self.svm_data = json.loads(self.svm_data)
    except ValueError, e:
      msg = 'Error: The ' + self.svm_data.svm_session + ' session requires a json formatted dataset as input'
      print json.dumps({'error':msg}, separators=(',', ': '))
      sys.exit()

    # data validation on HTML5 'datalist' support
    if self.svm_data['datalist_support'].lower() not in ['true', 'false']:
      msg = '''Error: The submitted \'datalist_support\' value, \'''' + self.svm_data['datalist_support'] + '''\' must be a string value \'true\', or \'false\''''
      print json.dumps({'error':msg}, separators=(',', ': '))
      sys.exit()

    # data validation on 'svm_model_type'
    if self.svm_data['svm_model_type'].lower() not in ['classification', 'regression']:
      msg = '''Error: The submitted \'svm_model_type\' value, \'''' + self.svm_data['svm_model_type'] + '''\' must be a string value \'classification\', or \'regression\''''
      print json.dumps({'error':msg}, separators=(',', ': '))
      sys.exit()

    # data validation on 'svm_session'
    if self.svm_data['svm_session'].lower() not in ['analysis', 'training']:
      msg = '''Error: The submitted \'svm_session\' value, \'''' + self.svm_data['svm_session'] + '''\' must be a string value \'analysis\', or \'training\''''
      print json.dumps({'error':msg}, separators=(',', ': '))
      sys.exit()

    # data validation on 'svm_indep_variable'
    try:
        if not isinstance(self.svm_data['svm_indep_variable'][0], unicode):
          msg = '''Error: The submitted \'svm_indep_variable\' value, \'''' + self.svm_data['svm_indep_variable'][0] + '''\' must be a unicode value'''
          print json.dumps({'error':msg}, separators=(',', ': '))
          sys.exit()
    except:
      msg = '''Error: The required \'svm_indep_variable\' variable does not exist'''
      print json.dumps({'error':msg}, separators=(',', ': '))
