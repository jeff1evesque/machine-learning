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
    db_select = Data_Retrieve( self.svm_data )
    db_return = db_select.db_data_retrieve(session_id)

    # return result
    return db_return['result']

  ## format_dataset:
  #
  #  @self.dataset, will have the following structure:
  #
  #      (('dep-variable-1', 'indep-variable-1', 23.45), ('dep-variable-1', 'indep-variable-2', 98.01),
  #       ('dep-variable-1', 'indep-variable-3', 0.432), ('dep-variable-1', 'indep-variable-4', 325.0),
  #       ('dep-variable-1', 'indep-variable-5', 54.64), ('dep-variable-1', 'indep-variable-6', 0.002),
  #       ('dep-variable-1', 'indep-variable-7', 25.0), ('dep-variable-2', 'indep-variable-1', 24.32),
  #       ('dep-variable-2', 'indep-variable-2', 92.22), ('dep-variable-2', 'indep-variable-3', 0.356),
  #       ('dep-variable-2', 'indep-variable-4', 235.0), ('dep-variable-2', 'indep-variable-5', 64.45),
  #       ('dep-variable-2', 'indep-variable-6', 0.001), ('dep-variable-2', 'indep-variable-7', 31.0),
  #       ('dep-variable-3', 'indep-variable-1', 22.67), ('dep-variable-3', 'indep-variable-2', 101.21),
  #       ('dep-variable-3', 'indep-variable-3', 0.832), ('dep-variable-3', 'indep-variable-4', 427.0),
  #       ('dep-variable-3', 'indep-variable-5', 75.45), ('dep-variable-3', 'indep-variable-6', 0.002),
  #       ('dep-variable-3', 'indep-variable-7', 24.0))
  def format_dataset(self):
    dataset_formatted = {}

    for instance in self.dataset:
      if not instance[0] in dataset_formatted:
        dataset_formatted[instance[0]] = []

      dataset_formatted[instance[0]].append( (instance[1], instance[2]) )

    return dataset_formatted

  ## get_observation_labels: return a list of dependent variable labels.
  def get_observation_labels(self):

  ## model_svm: generate an SVM model
  def model_svm(self):
