#!/usr/bin/python

## @data_validator.py
#  This script performs various data sanitation on input data, and 
#  validates the same data to ensure that the SVM algorithm will work
#  on the given dataset.  This adds an extra layer of security,
#  especially if the script later is used without a web interface.
import json, sys, magic
from jsonschema import validate
from helper import md5_for_file
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
    if ( session_type != None ):
      self.svm_session = session_type.lower()

  ## data_validation: this method validates the SVM properties of either
  #                   'training', or 'analysis' sessions.
  #
  #  Note: This method does not validate the associated 'file upload(s)'. The
  #        latter component is validated via 'file_upload_validation', and 
  #        'dataset_validation' methods (see below).
  def data_validation(self):
    # local variables
    flag_json = False
    json_data = json.loads(self.svm_data)['data']['result']

    # determine if input data is a JSON object
    try:
      json.loads(self.svm_data)['data']['result']
      flag_json = True
    except ValueError, e:
      msg = 'Error: The ' + self.svm_data.svm_session + ' session requires a json formatted dataset as input'
      print json.dumps({'error':msg}, separators=(',', ': '))
      return False

    # validation on 'training' session
    if self.svm_session == 'training' and flag_json:
      try:
        validate(json.loads(self.svm_data), jsonschema_training())
      except Exception, e:
        print str(e)
        return False

      # validation on 'xml file(s)'
      if ( json_data.get('svm_dataset_type', None) == 'upload file' and json_data.get('svm_dataset', None) ):
        for index, xmldata in enumerate(json_data['svm_dataset']):
          print xmldata

    # validation on 'analysis' session
    if self.svm_session == 'analysis' and flag_json:
      try:
        validate(json.loads(self.svm_data), jsonschema_analysis())
      except Exception, e:
        print str(e)
        return False

  ## dataset_validation: each supplied SVM dataset is correctly formatted via corresponding
  #                      methods in 'svm_json.py'. After being formatted, each dataset is
  #                      validated in this method.
  #
  #  Note: the SVM dataset is synonymous for the 'file upload(s)'
  def dataset_validation(self):
    try:
      # iterate list for dict elements
      for value in self.svm_data:
        validate( value, jsonschema_dataset())
    except Exception, e:
      print str(e)
      return False

  ## file_upload_validation: this method validates the MIME type of 'file upload(s)',
  #                          provided during a 'training' session. If any of the 'file
  #                          upload(s)' fails validation, this method will return False.
  #                          Otherwise, the method will return a list of unique 'file
  #                          upload(s)', discarding duplicates.
  def file_upload_validation(self, json_file_obj):
    json_data        = json.loads(json_file_obj)['data']['result']
    acceptable_type  = ['text/plain', 'text/csv', 'application/xml']

    unique_hash      = set()
    json_keep        = []

    if (json_data.get('file_upload', None)):

      for index, filedata in enumerate(json_data['file_upload']):
        try:
          mimetype = magic.from_file( filedata['file_temp'], mime=True )
          # validate file format
          if ( mimetype not in acceptable_type ):
            msg =  '''Error: Uploaded file, \'''' + filedata['file_temp'] + '''\', must be one of the formats:'''
            msg += '\n       ' + ', '.join(acceptable_type)
            print json.dumps({'error':msg}, separators=(',', ': '))
            return False

          filehash = md5_for_file(filedata['file_temp'])
          # add 'hashed' value of file reference(s) to a list
          if filehash not in unique_hash:
            unique_hash.add(filehash)
            json_keep.append( {'type': mimetype, 'filedata': filedata} )

        except:
          msg = 'Error: problem with file upload #' + str(index) + '. Please re-upload the file.'
          print json.dumps({'error':msg}, separators=(',', ': '))
          return False

      # replace portion of JSON with unique 'file reference(s)'
      json_data['file_upload'][:] = json_keep
      return json_data

    else: print json.dumps({'Error':'No file(s) were uploaded'}, separators=(',', ': '))
