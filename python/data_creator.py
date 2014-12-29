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
  #            {u'dep_variable_label': u'xxx',
  #             u'indep_variable_label': u'xxx',
  #             u'indep_variable_value': yy.yy}
  #
  #        where 'xxx' denotes a unicode string, and 'yy' denotes a float value.
  def __init__(self, svm_data):
    self.svm_data    = svm_data
    self.db_settings = Database()
    self.uid         = 1

  ## db_save_dataset: stores an SVM dataset into corresponding 'EAV data model'
  #                   database tables.
  def db_save_dataset(self):

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

    # create 'tbl_dataset_entity' table if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()
      sql    = '''\
               CREATE TABLE IF NOT EXISTS tbl_dataset_entity (
                 id INT NOT NULL AUTOINCREMENT PRIMARY KEY,
                 uid INT NOT NULL,
                 entity VARCHAR (50) NOT NULL,
                 datetime_saved DATETIME
               );
               '''
      cursor.execute( sql )
    except DB.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if conn:
        conn.close()

    # create 'tbl_dataset_attribute' table if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()
      sql    = '''\
               CREATE TABLE IF NOT EXISTS tbl_dataset_attribute (
                 id INT NOT NULL,
                 attribute VARCHAR (50) NOT NULL,
                 CONSTRAINT PK_attribute PRIMARY KEY (id, attribute),
                 CONSTRAINT FK_attribute_entity FOREIGN KEY (id) REFERENCES tbl_dataset_entity (id)
               );
               '''
      cursor.execute( sql )
    except DB.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if conn:
        conn.close()

    # create 'tbl_dataset_value' table if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()
      sql    = '''\
               CREATE TABLE IF NOT EXISTS tbl_dataset_value (
                 attribute VARCHAR (50) NOT NULL PRIMARY KEY,
                 value FLOAT NULL
               );
               '''
      cursor.execute( sql )
    except DB.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if conn:
        conn.close()

    # insert dataset values in 'tbl_dataset'
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      #cursor = conn.cursor()

      for data_instance in self.svm_data:
        # 'UTC_TIMESTAMP' returns the universal UTC datetime
        sql  = 'INSERT INTO tbl_dataset_entity (uid, entity, datetime_saved) VALUES( %d, %s, UTC_TIMESTAMP() )'
        cursor.execute( sql, data_instance['dep_variable_label'], (self.uid) )

        sql = 'INSERT INTO tbl_dataset_attribute (uid, attribute) VALUES( %d, %s )'
        cursor.execute( sql, (self.uid, data_instance['indep_variable_label']) )

        sql = 'INSERT INTO tbl_dataset_value (attribute, value) VALUES( %s, %f )'
        cursor.execute( sql, (data_instance['indep_variable_label'], data_instance['indep_variable_value']) )

        conn.commit()
    except DB.Error, e:
      conn.rollback()
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if conn:
        conn.close()

## Class: Analysis
class Analysis:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
