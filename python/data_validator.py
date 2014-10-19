#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on input data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.  This adds an extra layer of security,
#  especially if the script later is used without a web interface.
import json, sys, magic
from helper import md5_for_file
from helper import duplicate_list_index

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
    self.flag_exit = False

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
      for idx, element in enumerate(self.svm_data['svm_indep_variable']):
        if not isinstance(self.svm_data['svm_indep_variable'][idx], unicode):
          msg = '''Error: The submitted svm_indep_variable[\'%s\'] value, \'%s\' must be a unicode value''' % (idx, self.svm_data['svm_indep_variable'][idx])
          print json.dumps({'error':msg}, separators=(',', ': '))
          self.flag_exit = True
    except:
      msg = '''Error: The required \'svm_indep_variable\' value does not exist'''
      print json.dumps({'error':msg}, separators=(',', ': '))
      sys.exit()
    if self.flag_exit:
      sys.exit()

    # data validation on 'svm_dep_variable'
    if self.svm_data['svm_session'].lower() == 'training':
      try:
        for idx, element in enumerate(self.svm_data['svm_dep_variable']):
          if not isinstance(self.svm_data['svm_dep_variable'][idx], unicode):
            msg = '''Error: The submitted svm_dep_variable[\'%s\'] value, \'%s\' must be a unicode value''' % (idx, self.svm_data['svm_dep_variable'][idx])
            print json.dumps({'error':msg}, separators=(',', ': '))
            self.flag_exit = True
      except:
        msg = '''Error: The required \'svm_dep_variable\' value does not exist'''
        print json.dumps({'error':msg}, separators=(',', ': '))
        sys.exit()
      if self.flag_exit:
        sys.exit()

    # data validation on 'svm_dataset_type'
    print json.dumps({'error':self.svm_data['svm_dataset_type']}, separators=(',', ': '))

  ## file_upload_validation(): validate 'file upload' MIME type, and return JSON object
  #                            with duplicate 'file upload' references removed.
  def file_upload_validation(self, json_file_obj):
    json_data         = json.loads(json_file_obj)
    acceptable_type   = ['application/txt', 'text/plain', 'text/csv']
    list_file_upload  = []

    for index in range(len( json_data['file_upload'] )):
      try:
        # validate file format
        if ( magic.from_file( json_data['file_upload'][index]['file_temp'], mime=True ) not in acceptable_type ):
          msg =  '''Error: Uploaded file, \'''' + json_data['file_upload'][index]['file_temp'] + '''\', must be one of the formats:'''
          msg += '\n       ' + ', '.join(acceptable_type)
          print msg
          sys.exit()
        # add 'hashed' value of file reference(s) to a list
        list_file_upload.insert( index, md5_for_file(json_data['file_upload'][index]['file_temp']) )
      except:
        msg = 'Error: problem with file upload #' + str(index) + '. Please re-upload the file.'
        print msg
        sys.exit()

    # remove duplicate file upload(s)
    duplicate_indexes = duplicate_list_index( list_file_upload )
    for key, index_remove in duplicate_indexes.iteritems():
      for key, value in enumerate(index_remove):
        del json_data['file_upload'][value]
