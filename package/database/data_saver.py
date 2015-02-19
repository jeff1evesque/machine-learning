#!/usr/bin/python

## @data_saver.py
#  This file saves SVM related data into corresponding 'EAV data model' database
#      table(s), from the 'db_machine_learning' database.
from datetime import datetime
from database.db_query import SQL

## Class: Data_Save, explicitly inherit 'new-style' class
class Data_Save(object):

  ## constructor: stores an SVM dataset (json object), database configurations
  #               into their own corresponding class variable.
  # 
  #  Note: during the SVM dataset instance, 'self.svm_data' is a list of dictionary
  #        elements. One dictionary element, is represented as follows:
  #
  #            {'svm_dataset': {'dep_variable_label': 'yyy',
  #                               'indep_variable_label': 'yyy',
  #                               'indep_variable_value': zz.zz}},
  #
  #  Note: during the SVM entity instance, 'self.svm_data' is a dictionary with the
  #        following elements:
  #
  #            {'uid': xx, 'id_entity': xx, 'title': yyy}
  #
  #        where 'xx' denotes an integer value, 'yyy' a unicode string, and 'zz'
  #        representing a float value.
  def __init__(self, svm_data, cmd, session_type):
    # class variables
    self.svm_data     = svm_data
    self.svm_cmd      = cmd
    self.session_type = session_type
    self.list_error = []

  ## db_data_save: store, or update SVM dataset(s) into corresponding 'EAV data
  #                model' database table(s).
  #
  #  @sql_statement, is a sql format string, and not a python string. Therefore, '%s'
  #      is used for argument substitution.
  #
  #  Note: 'UTC_TIMESTAMP' returns the universal UTC datetime
  def db_data_save(self):
    # local variables
    sql = SQL()

    # create 'db_machine_learning' database if doesn't exist
    sql.sql_connect()
    sql_statement = 'CREATE DATABASE IF NOT EXISTS db_machine_learning CHARACTER SET utf8 COLLATE utf8_general_ci'
    sql.sql_command( sql_statement, 'create' )

    # retrieve any error(s), disconnect from database
    if sql.return_error(): self.list_error.append( sql.return_error() )
    sql.sql_disconnect()

    # create 'db_machine_learning' database tables if doesn't exist
    if self.svm_cmd == 'save_entity':
      sql_statement = '''\
                      CREATE TABLE IF NOT EXISTS tbl_dataset_entity (
                        id_entity INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR (50) NOT NULL,
                        uid_created INT NOT NULL,
                        datetime_created DATETIME NOT NULL,
                        uid_modified INT NULL,
                        datetime_modified DATETIME NULL
                      );
                      '''
      sql.sql_connect('db_machine_learning')
      sql.sql_command( sql_statement, 'create' )

      # retrieve any error(s), disconnect from database
      if sql.return_error(): self.list_error.append( sql.return_error() )
      sql.sql_disconnect()

    elif self.svm_cmd == 'save_label':
      sql_statement = '''\
                      CREATE TABLE IF NOT EXISTS tbl_observation_label (
                        id_label INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_entity INT NOT NULL,
                        dep_variable_label VARCHAR(75) NOT NULL
                      );
                      '''
      sql.sql_connect('db_machine_learning')
      sql.sql_command( sql_statement, 'create' )

      # retrieve any error(s), disconnect from database
      if sql.return_error(): self.list_error.append( sql.return_error() )
      sql.sql_disconnect()

    elif self.svm_cmd == 'save_value':
      sql_statement = '''\
                      CREATE TABLE IF NOT EXISTS tbl_dataset_value (
                        id_value INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        id_entity INT NOT NULL,
                        dep_variable_label VARCHAR (50) NOT NULL,
                        indep_variable_label VARCHAR (50) NOT NULL,
                        indep_variable_value FLOAT NOT NULL,
                        CONSTRAINT FK_dataset_entity FOREIGN KEY (id_entity) REFERENCES tbl_dataset_entity (id_entity)
                      );
                      '''
      sql.sql_connect('db_machine_learning')
      sql.sql_command( sql_statement, 'create' )

      # retrieve any error(s), disconnect from database
      if sql.return_error(): self.list_error.append( sql.return_error() )
      sql.sql_disconnect()

      # return error(s)
      if len( self.list_error ) > 0:
        return { 'status': False, 'error': self.list_error, 'id': None }

    # insert / update dataset entity value
    if self.svm_cmd == 'save_entity':
      sql.sql_connect('db_machine_learning')
      if self.session_type == 'data_append':
        sql_statement = 'UPDATE tbl_dataset_entity SET uid_modified=%s, datetime_modified=UTC_TIMESTAMP() WHERE id_entity=%s'
        args          = (self.svm_data['uid'], self.svm_data['id_entity'])
        response      = sql.sql_command( sql_statement, 'update', args )

      elif self.session_type == 'data_new':
        sql_statement = 'INSERT INTO tbl_dataset_entity (title, uid_created, datetime_created) VALUES( %s, %s, UTC_TIMESTAMP() )'
        args          = (self.svm_data['title'], self.svm_data['uid'])
        response      = sql.sql_command( sql_statement, 'insert', args )

      # retrieve any error(s), disconnect from database
      response_error = sql.return_error()
      sql.sql_disconnect()

      # return result
      if response_error: return { 'status': False, 'error': response_error, 'id': response['id'] }
      else: return { 'status': True, 'error': None, 'id': response['id'] }

    # insert / update feature label(s)
    elif self.svm_cmd == 'save_label':
      sql.sql_connect('db_machine_learning')

      # add labels (append case)
      if self.session_type in ['data_append', 'data_add']:

        # check if observation label exists in database
        sql_statement = 'SELECT dep_variable_label WHERE id_entity=%s'
        args          = (self.svm_data['id_entity'])
        response      = sql.sql_command( sql_statement, 'select', args )

        # add labels (new, and append case)
        if response['result']:
          sql_statement  = 'INSERT INTO tbl_observation_label (id_entity, dep_variable_label) VALUES( %s, %s )'
          args           = (self.svm_data['id_entity'], self.svm_data['label'])
          response_added = sql.sql_command( sql_statement, 'insert', args )

      # retrieve any error(s), disconnect from database
      response_error = sql.return_error()
      sql.sql_disconnect()

      # return result
      if response_error: return { 'status': False, 'error': response_error, 'id': response_added['id'] }
      else: return { 'status': True, 'error': None, 'id': response_added['id'] }

    # insert / update dataset value(s)
    elif self.svm_cmd == 'save_value':
      sql.sql_connect('db_machine_learning')
      sql_statement = 'INSERT INTO tbl_dataset_value (id_entity, dep_variable_label, indep_variable_label, indep_variable_value) VALUES( %s, %s, %s, %s )'
      dataset       = self.svm_data['svm_dataset']
      args          = (self.svm_data['id_entity'], dataset['dep_variable_label'], dataset['indep_variable_label'], dataset['indep_variable_value'])
      response      = sql.sql_command( sql_statement, 'insert', args )

      # retrieve any error(s), disconnect from database
      response_error = sql.return_error()
      sql.sql_disconnect()

      # return result
      if response: return { 'status': False, 'error': response_error, 'id': response['id'] }
      else: return { 'status': True, 'error': None, 'id': response['id'] }
