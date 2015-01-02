#!/usr/bin/python

## @config.py
#  This file contains various python configuration settings.

## Database: when instantiating this class, or defining any of the class variables,
#            make sure they are defined within the DBMS. This can be achieved via
#            the terminal console (or phpMyAdmin):
#
#                $ mysql -u root -p
#                MariaDB> CREATE USER 'authenticated'@'localhost' IDENTIFIED BY
#                    ->'password';
#                MariaDB> GRANT, CREATE, DELETE, DROP, EXECUTE, SELECT, SHOW
#                    -> DATABASES ON *.* TO 'authenticated'@'localhost';
#                MariaDB> FLUSH PRIVILEGES;
class Database:

  ## constructor:
  def __init__(self):
    self.db_host     = 'localhost'
    self.db_username = 'authenticated'
    self.db_password = 'password'

  ## get_db_host: get the database host
  def get_db_host(self):
    return self.db_host

  ## get_db_username: get the database username
  def get_db_username(self):
    return self.db_username

  ## get_db_password: get the database user password
  def get_db_password(self):
    return self.db_password

  ## set_db_host: define the database host
  def set_db_host(self, host):
    self.db_host = host

  ## set_db_username: define the database user
  def set_db_username(self, user):
    self.db_username = user

  ## set_db_password: define the database user password
  def set_db_password(self, pwd):
    self.db_password = pwd

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

## jsonschema_training(): contains the jsonschema for the 'training' session.
#                         Therefore, this schema validates the properties
#                         describing the session, not the dataset itself.
#
#  Note: This validation schema is used in data_validator.py.
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
              'svm_title': {
                'type': 'string',
                'minLength': 10
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
            }
          }
        }
      }
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
