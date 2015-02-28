#!/usr/bin/python

## @load_data.py
#  This file allocates provided input to respective 'session_xxx_xxx.py' script,
#      and generates a return object as required.
import sys, json
from brain.session.session_data_append import Data_Append
from brain.session.session_data_new import Data_New
from brain.session.session_model_generate import Model_Generate
from brain.session.session_model_use import Model_Use

## Class: Load_Data, explicitly inherit 'new-style' class
class Load_Data(object):

  ## constructor:
  def __init__(self, data):
    self.data = data
    list_error = []

  ## check_json: determine if input is json decodable
  def check_json(self):
    try:
      session_type = json.loads(self.data)['data']['settings']['svm_session']
      return session_type
    except Exception as e:
      error = 'Error: the provided \'svm_session\' is not json decodable, or not defined.'
      self.list_error.append(error)

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

  ## load_data_append: redirect input to 'session_data_append.py'
  def load_data_append(self):

    # instantiate class
    session = Data_Append( self.data )

    # define current session id
    session_id = json.loads(self.data)['data']['settings']['svm_session_id']

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

  ## load_model_generate: redirect input to 'session_model_generate.py'
  def load_model_generate(self):

    # instantiate class
    session = Model_Generate( self.data )

    # define current session id
    session_id = json.loads(self.data)['data']['settings']['svm_session_id']

    # implement class methods
    session.select_dataset(session_id)
    session.format_dataset()

  ## load_model_use: redirect input to 'session_model_use.py'
  def load_model_use(self):

    # instantiate class
    session = Model_Use( self.data )

    # implement class methods

  else:
    error = 'Error: the provided \'svm_session\' must be \'data_new\', \'data_append\', \'model_generate\', or \'model_use\'.'
    self.list_error.append(error)

  # return data
  if len(list_error) > 0:
    print json.dumps({ 'status': False, 'error': self.list_error }, sort_keys=True, indent=2, separators=(',', ': '))
  elif len(list_error) == 0:
    print json.dumps({ 'status': True, 'error': None })
