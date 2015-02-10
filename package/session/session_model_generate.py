#!/usr/bin/python

## @session_model_generate.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and generates an SVM model, respectively. The new SVM model, is stored
#      into respective database table(s), which later can be retrieved within
#      'session_model_use.py'.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys, json
from validator.validator_settings import Validate_Settings
from session.session_base import Session_Base
from database.data_retriever import Data_Retrieve

## Class: Model_Generate, inherit base methods from superclass 'Session_Base'
class Model_Generate(Session_Base):

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data       = svm_data
    self.svm_session    = json.loads(self.svm_data)['data']['settings']['svm_session']
    self.response_error = []

  ## select_dataset: define dataset associated with supplied 'session_id'
  #
  #  @session_id, corresponds to the 'id_entity' column from the
  #      'tbl_dataset_value' database table.
  def select_dataset(self, session_id):
    db_select = Data_Retrieve( self.svm_data, 'select', self.svm_session )
    db_return = db_select.db_data_retrieve(session_id)

    # define class property
    self.dataset = db_return['result']

  ## get_observation_labels: return a list of dependent variable labels.
  def get_observation_labels(self):

  ## model_svm: generate an SVM model
  def model_svm(self):
