#!/usr/bin/python

## @load_data.py
#  This file allocates provided input to respective 'session_xxx_xxx.py' script,
#      and generates a return object as required.
import sys
from brain.session.session_data_append import Data_Append
from brain.session.session_data_new import Data_New
from brain.session.session_model_generate import Model_Generate
from brain.session.session_model_use import Model_Use

## Class: Load_Data, explicitly inherit 'new-style' class
class Load_Data(object):

  ## constructor:
  def __init__(self, data):
    self.data         = data
    self.session_list = ['data_new', 'data_append', 'model_generate', 'model_use']
    self.list_error   = []

  ## load_data_new: redirect input to 'session_data_new.py'
  def load_data_new(self):

    # instantiate class
    session = Data_New( self.data )

    # implement class methods
    if not session.validate_arg_none():
      session.validate_svm_settings()
      session.validate_mime_type()
      session.check()

      session_entity = session.save_svm_entity('data_new')
      if session_entity['status']:
        session_id = session_entity['id']
        session.check()

        session.dataset_to_json(session_id)
        session.validate_dataset_json()
        session.check()

        session.save_observation_label('data_new', session_id)
        session.check()

        session.save_svm_dataset('data_new')
        session.check()

      # return
      if session.return_error: return False
      else: return 'Dataset(s) properly uploaded into database'

  ## load_data_append: redirect input to 'session_data_append.py'
  def load_data_append(self):

    # instantiate class
    session = Data_Append( self.data )

    # define current session id
    session_id = self.data['data']['settings']['svm_session_id']

    # implement class methods
    if not session.validate_arg_none():
      session.validate_svm_settings()
      session.validate_mime_type()
      session.check()

      session_entity = session.save_svm_entity('data_append', session_id)
      if session_entity['status']:
        session.check()

        session.dataset_to_json(session_id)
        session.validate_dataset_json()
        session.check()

        session.save_observation_label('data_append', session_id)
        session.check()

        session.save_svm_dataset('data_append')
        session.check()

      # return
      if session.return_error: return False
      else: return 'Dataset(s) properly appended into database'

  ## load_model_generate: redirect input to 'session_model_generate.py'
  def load_model_generate(self):

    # instantiate class
    session = Model_Generate( self.data )

    # define current session id
    session_id = self.data['data']['settings']['svm_session_id']

    # implement class methods
    session.select_dataset(session_id)
    session.format_dataset()

    # return
    if session.return_error: return False
    else: return 'Model properly generated'

  ## load_model_use: redirect input to 'session_model_use.py'
  def load_model_use(self):

    # instantiate class
    session = Model_Use( self.data )

    # implement class methods

  ## get_session_type: returns the current session type.
  def get_session_type(self):
    session_type = self.data['data']['settings']['svm_session']
    if session_type in self.session_list: return {'session_type': session_type, 'error': None}
    else:
      error = 'Error: the provided \'svm_session\' must be \'data_new\', \'data_append\', \'model_generate\', or \'model_use\'.'
      self.list_error.append(error)
      return {'session_type': None, 'error': error}

    # return
    if session.return_error: return False
    else: return 'Model properly generated'

  # get_errors: returns a list of current errors associated with class instance
  def get_errors(self):
    if len(self.list_error) > 0:
      return self.list_error
    else:
      return None
