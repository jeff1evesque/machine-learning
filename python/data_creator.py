#!/usr/bin/python

## @data_creator.py
import json
from datetime import datetime
import MySQLdb as DB
from config import Database

## Class: Training
class Training:

  ## constructor: stores an SVM dataset (json object), database configurations
  #               into their own corresponding class variable.
  # 
  #  Note: the SVM dataset, 'self.svm_data' is list of dictionary elements. One
  #        dictionary element, is represented as follows:
  #
  #            {'dep_variable_label': u'xxx',
  #             'indep_variable_label': u'xxx',
  #             'indep_variable_value': yy.yy}
  #
  #        where 'xxx' denotes a unicode string, and 'yy' denotes a float value.
  def __init__(self, svm_data, cmd=None):
    self.svm_data    = svm_data
    self.svm_cmd     = cmd
    self.db_settings = Database()
    self.uid         = 1

    # create 'db_machine_learning' database if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password() )
      cursor = conn.cursor()
      sql    = 'CREATE DATABASE IF NOT EXISTS db_machine_learning CHARACTER SET utf8 COLLATE utf8_general_ci'
      cursor.execute( sql )
    except DB.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if conn:
        conn.close()

  ## db_save_training: stores an SVM dataset into corresponding 'EAV data model'
  #                    database table.
  #
  #  Note: 'UTC_TIMESTAMP' returns the universal UTC datetime
  def db_save_training(self):

    # create 'type' table if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()

      if self.svm_cmd == 'save_entity':
        sql    = '''\
                 CREATE TABLE IF NOT EXISTS tbl_dataset_entity (
                   id_entity INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   title VARCHAR (50) NOT NULL,
                   uid INT NOT NULL,
                   datetime_saved DATETIME
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
    except DB.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if conn:
        conn.close()

    # insert dataset values
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()

      # sql format string is not a python string, hence '%s' used for all columns
      if self.svm_cmd == 'save_entity':
        sql  = 'INSERT INTO tbl_dataset_entity (title, uid, datetime_saved) VALUES( %s, %s, UTC_TIMESTAMP() )'
        cursor.execute( sql, (self.svm_data['title'], self.svm_data['uid']) )

      elif self.svm_cmd == 'save_value':
        sql = 'INSERT INTO tbl_dataset_value (entity_id, dep_variable_label, indep_variable_label, indep_variable_value) VALUES( %s, %s, %s, %s )'
        cursor.execute( sql, (self.svm_data['id_entity'], self.svm_data['svm_dataset']['dep_variable_label'], self.svm_data['svm_dataset']['indep_variable_label'], self.svm_data['svm_dataset']['indep_variable_value']) )

      conn.commit()
    except DB.Error, e:
      conn.rollback()
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if conn:
        rowid = cursor.lastrowid
        conn.close()
        return rowid

## Class: Analysis
class Analysis:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
