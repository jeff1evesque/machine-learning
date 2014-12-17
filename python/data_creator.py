#!/usr/bin/python

## @data_creator.py
import json, time
import MySQLdb as DB
from config import Database

## Class: Training
class Training:

  ## constructor
  def __init__(self, svm_data):
    self.svm_data    = svm_data
    self.db_settings = Database()

  ## db_save_dataset
  def db_save_dataset(self):
    print self.svm_data

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

    # create 'tbl_dataset' table if doesn't exist
    try:
      conn   = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password(), db='db_machine_learning' )
      cursor = conn.cursor()
      sql    = '''\
               CREATE TABLE IF NOT EXISTS tbl_dataset (
                 id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                 uid TEXT,
                 dep_variable TEXT,
                 indep_variables TEXT,
                 datetime TEXT
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
      cursor = conn.cursor()

      for dep_variable, indep_variables in self.svm_data.iteritems():
        sql  = "INSERT INTO tbl_dataset (dep_variable, indep_variables, datetime) VALUES( '%s', '%s', '%s' );"
        cursor.execute( sql % ( dep_variable, ','.join(indep_variables), string(datetime.datetime.now()) ) )
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
