#!/usr/bin/python

## @session_data_append.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and appends additional dataset(s) provided during the current session. The
#      new superset of appended dataset(s), is stored into respective database
#      table(s), which later can be retrieved in another instance of this script,
#      or within 'session_model_generate.py'.

## Class: Data_Append
class Data_Append:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data
