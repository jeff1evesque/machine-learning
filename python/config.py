#!/usr/bin/python

## @config.py
#  This file contains python configuration settings.

## Class: Database
class Database:

  ## constructor:
  def __init__(self):
    self.db_host     = 'localhost'
    self.db_username = 'authenticated'
    self.db_passowrd = 'passoword'

## jsonschema_training(): contains the jsonschema for the 'training' session.
#                         This validation schema is used in data_validator.py.
def jsonschema_training():
  schema = {
    'type': 'object',
    'properties': {
      'json_creator': { 'type': 'string' },
      'data': {
        'type': 'object',
        'properties': {
          'result': {
            'type': 'object',
            'properties': {
              'datalist_support': {
                'type': 'string',
                'enum': ['true', 'false']
              },
              'svm_dataset_type': { 
                'type': 'string',
                'enum': ['upload file', 'xml file']
              },
              'svm_dataset': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
              },
              'svm_session': { 
                'type': 'string',
                'enum': ['training', 'analysis']
              },
              'svm_model_type': {
                'type': 'string',
                'enum': ['classification', 'regression']
              },
              'svm_dep_variable': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
              },
              'svm_indep_variable': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
              },
            }
          }
        }
      }
    }
  }
  return schema

## jsonschema_analysis(): contains the jsonschema for the 'analysis' session.
#                         This validation schema is used in data_validator.py.
def jsonschema_analysis():
  schema = {
    'type': 'object',
    'properties': {
      'json_creator': { 'type': 'string' },
      'data': {
        'type': 'object',
        'properties': {
          'result': {
            'type': 'object',
            'properties': {
              'datalist_support': {
                'type': 'string',
                'enum': ['true', 'false']
              },
              'svm_session': { 
                'type': 'string',
                'enum': ['training', 'analysis']
              },
              'svm_model_type': {
                'type': 'string',
                'enum': ['classification', 'regression']
              },
              'svm_indep_variable': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
              },
            }
          }
        }
      }
    }
  }
  return schema
