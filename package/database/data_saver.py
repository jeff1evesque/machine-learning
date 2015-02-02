#!/usr/bin/python

## @data_saver.py
import json
from datetime import datetime
import MySQLdb as DB
from database.db_settings import Database
from database.db_query import SQL

## Class: Training
class Training:

  ## constructor: stores an SVM dataset (json object), database configurations
  #               into their own corresponding class variable.
  # 
  #  Note: the SVM dataset, 'self.svm_data' is list of dictionary elements. One
  #        dictionary element, is represented as follows:
  #
  #            { {'uid': xx, 'title': 'yyy'},
  #              {'svm_dataset': [{'dep_variable_label': 'yyy',
  #                                'indep_variable_label': 'yyy',
  #                                'indep_variable_value': zz.zz}]},
  #              {'id_entity': xx} }
  #
  #        where 'xx' denotes an integer value, 'yyy' a unicode string, and 'zz'
  #        representing a float value.
  def __init__(self, svm_data, cmd, session_type):
    # class variables
    self.svm_data     = svm_data
    self.svm_cmd      = cmd
    self.session_type = session_type
    self.db_settings  = Database()

  ## db_save_training: stores an SVM dataset into corresponding 'EAV data model'
  #                    database table.
  #
  #  Note: 'UTC_TIMESTAMP' returns the universal UTC datetime
  def db_save_training(self):
    # local variables
    list_error = []

    # create 'db_machine_learning' database if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password() )
      cursor = conn.cursor()
      sql    = 'CREATE DATABASE IF NOT EXISTS db_machine_learning CHARACTER SET utf8 COLLATE utf8_general_ci'
      cursor.execute( sql )
    except DB.Error, error:
      list_error.append(error)
    finally:
      if conn:
        conn.close()

    # create 'type' table if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()

      if self.svm_cmd == 'save_entity':
        sql    = '''\
                 CREATE TABLE IF NOT EXISTS tbl_dataset_entity (
                   id_entity INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   title VARCHAR (50) NOT NULL,
                   uid_created INT NOT NULL,
                   datetime_created DATETIME NOT NULL,
                   uid_modified INT NULL,
                   datetime_modified DATETIME NULL
                 );
                 '''

      elif self.svm_cmd == 'save_value':
        sql    = '''\
                 CREATE TABLE IF NOT EXISTS tbl_dataset_value (
                   id_attribute INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   id_entity INT NOT NULL,
                   dep_variable_label VARCHAR (50) NOT NULL,
                   indep_variable_label VARCHAR (50) NOT NULL,
                   indep_variable_value FLOAT NOT NULL,
                   CONSTRAINT FK_dataset_entity FOREIGN KEY (id_entity) REFERENCES tbl_dataset_entity (id_entity)
                 );
                 '''
      cursor.execute( sql )

    except DB.Error, error:
      list_error.append(error)
    finally:
      if conn:
        conn.close()

    # insert dataset values
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()

      # sql format string is not a python string, hence '%s' used for all columns
      if self.svm_cmd == 'save_entity':
        if self.session_type == 'data_append':
          sql  = 'UPDATE tbl_dataset_entity SET uid_modified=%s, datetime_modified=UTC_TIMESTAMP() WHERE id_entity=%s'
          cursor.execute( sql, (self.svm_data['uid'], self.svm_data['id_entity']) )

        elif self.session_type == 'data_new':
          sql  = 'INSERT INTO tbl_dataset_entity (title, uid_created, datetime_created) VALUES( %s, %s, UTC_TIMESTAMP() )'
          cursor.execute( sql, (self.svm_data['title'], self.svm_data['uid']) )

      elif self.svm_cmd == 'save_value':
        sql = 'INSERT INTO tbl_dataset_value (id_entity, dep_variable_label, indep_variable_label, indep_variable_value) VALUES( %s, %s, %s, %s )'
        dataset = self.svm_data['svm_dataset']
        cursor.execute( sql, (self.svm_data['id_entity'], dataset['dep_variable_label'], dataset['indep_variable_label'], dataset['indep_variable_value']) )

      conn.commit()
    except DB.Error, error:
      conn.rollback()
      list_error.append(error)
    finally:
      if conn:
        rowid = cursor.lastrowid
        conn.close()
        return { 'status': True, 'error': None, 'id': rowid }

    # return error
    if len(list_error) > 0:
      return { 'status': False, 'error': list_error }
    else:
      return { 'status': True, 'error': None }

## Class: Analysis
class Analysis:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
