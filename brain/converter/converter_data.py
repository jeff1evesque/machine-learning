#!/usr/bin/python

## @converter_json.py
#  This file contains methods needed to correctly format input data.

## Class: Convert_Data, explicitly inherit 'new-style class
class Convert_Data(object):

  ## constructor
  def __init__(self, settings, files=None):
    self.settings   = settings
    self.files      = files

    self.flag_validator = True
    self.list_error     = []

    self.list_model_type   = ['classification', 'regression']
    self.list_dataset_type = ['file_upload', 'xml_url']
    self.list_session_type = ['data_new', 'data_append', 'model_generate', 'model_use']

    self.list_upload   = []
    self.list_response = []

  ## format: restructure input data
  def format(self):

    # local variables
    formatted_settings = {}
    formatted_files    = {}

    # restructure settings
    try:
      for key, value in self.settings.items():
        formatted_settings[key.lower()] = value.lower()
    except Exception as error:
      self.list_error.append( error )
      return {'data': None, 'error': self.list_error}

    # restructure files: not all sessions involve files
    if self.files:
      try:
        for file in self.files.getlist('svm_dataset[]'):
          formatted_files[file.filename] = file

        dataset = {'upload_quantity': len(self.files.getlist('svm_dataset[]')), 'file_upload': formatted_files}
      except Exception as error:
      self.list_error.append( error )
      return {'data': None, 'error': self.list_error}
    else: dataset = None

    # build JSON structure
    structure = {'data': {'settings': formatted_settings, 'dataset': dataset}}

    # return new structured data
    return structure

  ## get_errors: returns all errors corresponding to this class instance
  def get_errors(self):
    if len(self.list_error) > 0: return { 'error': self.list_error }
    else: return { 'error': None }
