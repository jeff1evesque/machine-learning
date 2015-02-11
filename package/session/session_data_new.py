#!/usr/bin/python

## @session_data_new.py
#  This file receives data (i.e. settings), including one or more dataset(s)
#      provided during the current session, and stores them into corresponding
#      database tables. The stored dataset(s) can later be retrieved from
#      'session_data_append.py', or 'session_generate_model.py'.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys, json
from database.data_saver import Data_Save
from validator.validator_dataset import Validate_Dataset
from validator.validator_mime import Validate_Mime
from validator.validator_settings import Validate_Settings
from converter.converter_json import JSON
from session.session_base import Session_Base

## Class: Data_New, inherit base methods from superclass 'Data_Append'
class Data_New(Session_Base):

  ## constructor: define class properties using the superclass 'Session_Base'
  #               constructor, along with the constructor in this subclass.
  #
  #  @super(), implement 'Session_Base' superclass constructor within this
  #      child class constructor.
  #
  #  Note: the superclass constructor expects the same 'svm_data' argument.
  def __init__(self, svm_data):
    super(Data_New, self).__init__(svm_data)
    self.flag_validate_mime  = False
    self.feature_labels      = []

  ## validate_mime_type: validate mime type for each dataset.
  def validate_mime_type(self):
    validator = Validate_Mime( self.svm_data, self.svm_session )
    self.response_mime_validation = validator.file_upload_validation( self.svm_data)

    if self.response_mime_validation['error'] != None:
      self.response_error.append( self.response_mime_validation['error'] )
      self.flag_validate_mime = True

  ## save_svm_entity: save the current entity into the database, then return
  #                   the corresponding entity id.
  def save_svm_entity(self, session_type):
    svm_entity = {'title': json.loads( self.svm_data )['data']['settings'].get('svm_title', None), 'uid': 1, 'id_entity': None}
    db_save    = Data_Save( svm_entity, 'save_entity', session_type )

    # save dataset element
    db_return  = db_save.db_data_save()

    # return error(s)
    if not db_return['status']:
      self.response_error.append( db_return['error'] )
      return { 'status': False, 'id': None, 'error': self.response_error }

    # return session id
    elif db_return['status'] and session_type == 'data_new':
      return { 'status': True, 'id': db_return['id'], 'error': None }

  ## save_feature_label: save the list of unique independent variable labels
  #                      from a supplied session (entity id) into the database.
  #
  #  @self.feature_labels, list of features (independent variables), defined
  #      after invoking the 'dataset_to_json' method.
  def save_feature_label(self, session_type, session_id):
    if len(self.feature_labels) > 0:
      for label in self.feature_labels:

        db_save = Data_Save( {'label': label, 'id_entity': session_id}, 'save_label', session_type )

        # save dataset element, append error(s)
        db_return = db_save.db_data_save()
        if not db_return['status']: self.response_error.append( db_return['error'] )

  ## dataset_to_json: convert either csv, or xml dataset(s) to a uniform
  #                   json object.
  def dataset_to_json(self, id_entity):
    flag_convert   = False
    flag_append    = True

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
            # conversion
            dataset_converter = JSON(val['filedata']['file_temp'])
            dataset_converted = json.loads(dataset_converter.csv_to_json())

            # check label consistency, append label(s) to 'feature_labels'
            if sorted(dataset_converter.get_feature_labels()) == self.feature_labels: self.response_error.append('The supplied features (independent variables) are inconsistent')
            self.feature_labels = sorted(dataset_converter.get_feature_labels())

             # build new (relevant) dataset
            self.json_dataset.append({'id_entity': id_entity, 'svm_dataset': dataset_converted})
          except Exception as error:
            self.response_error.append( error )
            flag_append = False

        # xml to json
        elif val['type'] in ('application/xml', 'text/xml' ):
          try:
            # conversion
            dataset_converter = JSON(val['filedata']['file_temp'])
            dataset_converted = json.loads(dataset_converter.xml_to_json())

            # check label consistency, append label(s) to 'feature_labels'
            if sorted(dataset_converter.get_feature_labels()) == self.feature_labels: self.response_error.append('The supplied features (independent variables) are inconsistent')
            self.feature_labels = sorted(dataset_converter.get_feature_labels())

             # build new (relevant) dataset
            self.json_dataset.append({'id_entity': id_entity, 'svm_dataset': dataset_converted})
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
        db_save = Data_Save( {'svm_dataset': dataset, 'id_entity': data['id_entity']}, 'save_value', session_type )

        # save dataset element, append error(s)
        db_return = db_save.db_data_save()
        if not db_return['status']: self.response_error.append( db_return['error'] )
