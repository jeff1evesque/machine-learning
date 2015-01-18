#!/usr/bin/python

## @jsonschema_definition.py
#  This file contains various jsonschema definitions.

## jsonschema_dataset(): contains the jsonschema for the SVM dataset. Therefore
#                        this schema validates only the SVM dataset, not the
#                        properties describing the (training, or analysis) session.
#
#  Note: This validation schema is used in data_validator.py.
def jsonschema_dataset():
  schema = {
    'type': 'object',
    'properties': {
      'dep_variable_label': { 'type': 'string' },
      'indep_variable_label': { 'type': 'string' },
      'indep_variable_value': { 'type': 'number' },
    }
  }
  return schema

## jsonschema_dataset_id(): contains the jsonschema for the SVM dataset. Specifically,
#                           this schema complements 'jsonschema_dataset()'.
#
#  Note: This validation schema is used in corresponding validator_xxx.py.
def jsonschema_dataset_id():
  schema = {
    'type': 'object',
    'properties': {
      'id_entity': { 'type': 'integer' },
    }
  }
  return schema

## jsonschema_model_use(): contains the jsonschema for the 'model_use' session.
#
#  Note: This validation schema is used in corresponding validator_xxx.py.
def jsonschema_model_use():
  schema = {
    'type': 'object',
    'properties': {
      'svm_title': { 'type': 'string' },
      'svm_session_id' : { 'type': 'string' },
      'svm_dataset_type': {
        'type': 'string',
        'enum': ['file_upload', 'xml_url']
      },
      'svm_session': {
        'type': 'string',
        'enum': ['data_new', 'data_append', 'model_generate', 'model_use']
      },
    }
  }
  return schema

## jsonschema_analysis(): contains the jsonschema for the 'analysis' session.
#                         Therefore, this schema validates the properties
#                         describing the session, not the dataset itself.
#
#  Note: This validation schema is used in data_validator.py.
def jsonschema_analysis():
  schema = {
    'type': 'object',
    'properties': {
      'svm_title': { 'type': 'string' },
      'svm_model_type': {
        'type': 'string',
        'enum': ['classification', 'regression']
      },
      'svm_session': {
        'type': 'string',
        'enum': ['training', 'analysis']
      },
      'svm_indep_variable': {
        'type': 'array',
        'items': { 'type': 'string' },
        'minItems': 1
      },
    }
  }
  return schema
