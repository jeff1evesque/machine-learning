#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on input data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.  This adds an extra layer of security,
#  especially if the script later is used without a web interface.
import json, sys, magic
from helper import md5_for_file
from helper import duplicate_list_index
from config import jsonschema_training, jsonschema_analysis

## Class: Validator
class Validator:

  ## constructor: saves a subset of the passed-in form data
  #
  #  @svm_data    : is the input data, generally a form POST data, if
  #                 the 'session_type' is training.
  #  @session_type: represents the current session type
  def __init__(self, svm_data=None, session_type=None):
    self.svm_data = svm_data
    self.svm_session = session_type.lower()

  ## data_validation(): the first four validations is used for both 'training',
  #                     and 'analysis' sessions. Since the 'analysis' session
  #                     does not have unique validation(s), an 'ELIF' statement
  #                     is not required for it, and already implied by the first
  #                     four validations.
  #
  #  @self.svm_data: decoded JSON object 
  def data_validation(self):
    # determine if input data is a JSON object
    try:
      self.svm_data = json.loads(self.svm_data)['data']['result']
    except ValueError, e:
      msg = 'Error: The ' + self.svm_data.svm_session + ' session requires a json formatted dataset as input'
      print json.dumps({'error':msg}, separators=(',', ': '))
      return False

    # data validation on HTML5 'datalist' support
    if self.svm_data['datalist_support'].lower() not in ['true', 'false']:
      msg = '''Error: The submitted \'datalist_support\' value, \'''' + self.svm_data['datalist_support'] + '''\' must be a string value \'true\', or \'false\''''
      print json.dumps({'error':msg}, separators=(',', ': '))
      return False

    # data validation on 'svm_session'
    if self.svm_data['svm_session'].lower() not in ['analysis', 'training']:
      msg = '''Error: The submitted \'svm_session\' value, \'''' + self.svm_data['svm_session'] + '''\' must be a string value \'analysis\', or \'training\''''
      print json.dumps({'error':msg}, separators=(',', ': '))
      return False

    # data validation on 'svm_indep_variable'
    try:
      for idx, element in enumerate(self.svm_data['svm_indep_variable']):
        if not isinstance(self.svm_data['svm_indep_variable'][idx], unicode):
          msg = '''Error: The submitted svm_indep_variable[\'%s\'] value, \'%s\' must be a unicode value''' % (idx, self.svm_data['svm_indep_variable'][idx])
          print json.dumps({'error':msg}, separators=(',', ': '))
          return False
    except:
      msg = '''Error: The required \'svm_indep_variable\' value does not exist'''
      print json.dumps({'error':msg}, separators=(',', ': '))
      return False

    # validation on 'training' session
    if self.svm_session == 'training':
      # data validation on 'svm_model_type'
      if self.svm_data['svm_model_type'].lower() not in ['classification', 'regression']:
        msg = '''Error: The submitted \'svm_model_type\' value, \'''' + self.svm_data['svm_model_type'] + '''\' must be a string value \'classification\', or \'regression\''''
        print json.dumps({'error':msg}, separators=(',', ': '))
        return False

      # data validation on 'svm_dep_variable'
      if self.svm_data['svm_session'].lower() == 'training':
        try:
          for idx, element in enumerate(self.svm_data['svm_dep_variable']):
            if not isinstance(self.svm_data['svm_dep_variable'][idx], unicode):
              msg = '''Error: The submitted svm_dep_variable[\'%s\'] value, \'%s\' must be a unicode value''' % (idx, self.svm_data['svm_dep_variable'][idx])
              print json.dumps({'error':msg}, separators=(',', ': '))
              return False
        except:
          msg = '''Error: The required \'svm_dep_variable\' value does not exist'''
          print json.dumps({'error':msg}, separators=(',', ': '))
          return False

      # data validation on 'svm_dataset_type'
      if self.svm_data['svm_dataset_type'].lower() not in ['upload file', 'xml file']:
        msg = '''Error: The submitted \'svm_dataset_type\' value, \'''' + self.svm_data['svm_dataset_type'] + '''\' must be a string value \'file upload\', or \'xml file\''''
        print json.dumps({'error':msg}, separators=(',', ': '))
        return False

  ## file_upload_validation(): validate 'file upload' MIME type, and return JSON object
  #                            with duplicate 'file upload' references removed.
  def file_upload_validation(self, json_file_obj):
    json_data        = json.loads(json_file_obj)['data']['result']
    acceptable_type  = ['application/txt', 'text/plain', 'text/csv']

    unique_hash      = set()
    json_keep        = []

    if (json_data.get('file_upload', None)):

      for index, filedata in enumerate(json_data['file_upload']):
        try:
          # validate file format
          if ( magic.from_file( filedata['file_temp'], mime=True ) not in acceptable_type ):
            msg =  '''Error: Uploaded file, \'''' + filedata['file_temp'] + '''\', must be one of the formats:'''
            msg += '\n       ' + ', '.join(acceptable_type)
            print json.dumps({'error':msg}, separators=(',', ': '))
            return False

          filehash = md5_for_file(filedata['file_temp'])
          # add 'hashed' value of file reference(s) to a list
          if filehash not in unique_hash:
            unique_hash.add(filehash)
            json_keep.append(filedata)
        except:
          msg = 'Error: problem with file upload #' + str(index) + '. Please re-upload the file.'
          print json.dumps({'error':msg}, separators=(',', ': '))
          return False

      # replace portion of JSON with unique 'file reference(s)'
      json_data['file_upload'][:] = json_keep
      return json_data

    else: print json.dumps({'Error':'No file(s) were uploaded'}, separators=(',', ': '))
