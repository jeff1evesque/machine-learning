#!/usr/bin/python

## @session_data_add.py
#  This file receives data (i.e. settings), including one or more dataset(s)
#      provided during the current session, and stores them into corresponding
#      database tables. The stored dataset(s) can later be retrieved from
#      'session_data_append.py', or 'session_generate_model.py'.
#
#  Note: this script is executed from 'load_logic.php', using the 'exec( ... )'
#        equivalent method when implemented via the web-interface. Since the
#        web-interface is an AJAX process, the shelled into python script requires
#        print statements, when data is needed to be returned to the client-end.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys, json
from database.data_saver import Training
from validator.validator_dataset import Validate_Dataset
from validator.validator_mime import Validate_Mime
from validator.validator_settings import Validate_Settings
from converter.converter_json import JSON

## Class: Data_Add
class Data_Add:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data       = svm_data
    self.svm_session    = json.loads(self.svm_data)['data']['settings']['svm_session']
    self.response_error = []
    self.flag_validate_mime  = False


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

  ## validate_mime_type: validate mime type for each dataset.
  def validate_mime_type(self):
    validator = Validate_Mime( self.svm_data, self.svm_session )
    self.response_mime_validation = validator.file_upload_validation( self.svm_data)

    if self.response_mime_validation['error'] != None:
      self.response_error.append( self.response_mime_validation['error'] )
      self.flag_validate_mime = True

  ## save_svm_entity: save entity information pertaining to new session.
  def save_svm_entity(self, session_type, session_id=None):
    svm_entity = {'title': json.loads( self.svm_data )['data']['settings'].get('svm_title', None), 'uid': 1, 'id_entity': session_id}
    db_save    = Training( svm_entity, 'save_entity', session_type )

    # save dataset element, append error(s)
    db_return = db_save.db_save_training()
    if not db_return['status']: self.response_error.append( db_return['error'] )
    else: self.id_entity = db_return['id']

  ## set_entity_id: defines the class variable for session id.
  def set_entity_id(self, session_id):
    self.id_entity = session_id

  ## dataset_to_json: convert either csv, or xml dataset(s) to a uniform
  #                   json object.
  def dataset_to_json(self):
    flag_convert = False
    flag_append  = True

    try:
      self.response_mime_validation['json_data']['file_upload']
      flag_convert = True
    except Exception as error:
      self.response_error.append( error )
      return False

    if ( flag_convert ):
      self.json_dataset = []
      svm_property      = self.svm_data

      for val in self.response_mime_validation['json_data']['file_upload']:
        # csv to json
        if val['type'] in ('text/plain', 'text/csv'):
          try:
            for dataset in val['filedata']['file_temp']:
              self.json_dataset.append({'id_entity': self.id_entity, 'svm_dataset': json.loads(JSON(dataset).csv_to_json())})
          except Exception as error:
            self.response_error.append( error )
            flag_append = False

        # xml to json
        elif val['type'] in ('application/xml', 'text/xml' ):
          try:
            for dataset in val['filedata']['file_temp']:
              self.json_dataset.append({'id_entity': self.id_entity, 'svm_dataset': json.loads(JSON(dataset).xml_to_json())})
          except Exception as error:
            self.response_error.append( error )
            flag_append = False

      if ( flag_append == False ): return False

  ## validate_dataset_json: validate each dataset element.
  def validate_dataset_json(self):
    for list in self.json_dataset:
      for val in list['svm_dataset']:
        json_validated = Validate_Dataset( val, self.svm_session )

        if json_validated.dataset_validation()['error'] != None:
          self.response_error.append( json_validated.dataset_validation()['error'] )

  ## save_svm_dataset: save each dataset element into a database table.
  def save_svm_dataset(self, session_type):
    for data in self.json_dataset:
      for dataset in data['svm_dataset']:
        db_save = Training( {'svm_dataset': dataset, 'id_entity': data['id_entity']}, 'save_value', session_type )

        # save dataset element, append error(s)
        db_return = db_save.db_save_training()
        if not db_return['status']: self.response_error.append( db_return['error'] )

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
