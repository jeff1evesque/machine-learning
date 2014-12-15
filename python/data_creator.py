#!/usr/bin/python

## @data_creator.py
import json
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

    # create database if doesn't exist
    try:
      con    = DB.connect( host=self.db_settings.get_db_host(), user=self.db_settings.get_db_username(), passwd=self.db_settings.get_db_password() )
      cursor = con.cursor()
      sql    = 'CREATE DATABASE IF NOT EXISTS db_machine_learning'
      cursor.execute( sql )
    except DB.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      return False
    finally:
      if con:
        con.close()

## Class: Analysis
class Analysis:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
