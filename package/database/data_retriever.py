#!/usr/bin/python

## @data_retriever.py
from database.db_query import SQL

## Class: Data_Retrieve, explicitly inherit 'new-style' class
class Data_Retrieve(object):

  ## constructor:
  def __init__(self, svm_data, cmd, session_type):
    # class variables
    self.svm_data     = svm_data
    self.svm_cmd      = cmd
    self.session_type = session_type

  ## db_data_retrieve: retrieve an SVM dataset from corresponding 'EAV data
  #                    model' database table(s).
  def db_data_retrieve(self):
