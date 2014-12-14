#!/usr/bin/python

## @config.py
#  This file contains python configuration settings.

## Class: Database
class Database:

  ## constructor:
  def __init__(self):
    self.db_host     = 'localhost'
    self.db_username = 'authenticated'
    self.db_passowrd = 'password'

  ## get_db_host:
  def get_db_host(self):
    return self.db_host

  ## get_db_username:
  def get_db_username(self):
    return self.db_username

  ## get_db_password:
  def get_db_password(self):
    return self.db_password

  ## set_db_host:
  def set_db_host(self, host):
    self.db_host = host

  ## set_db_username:
  def set_db_username:
    self.db_username = username

  ## set_db_password:
  def set_db_password:
    self.db_password = password

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
